#!/usr/bin/python

# Author: nebulam87 (nebulam87@linuxmail.org) 
# Version: 1.0 

import urllib2
import json
import sys
import re
import optparse

def bing_search(query, topValue=50):
        #search type: Web
        bingkey = '[insert Bing API key here]'
        query = urllib2.quote(query)
        # create request for authentication
        userAgent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        credentials = (':%s' % bingkey).encode('base64')[:-1]
        auth = 'Basic %s' % credentials
        url = 'https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27'+query+'%27&$top='+str(topValue)+'&$format=json'
	print "[>] Sending request with URL address: " + url + "\n"
	request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', userAgent)
        request_opener = urllib2.build_opener()
        try:
                response = request_opener.open(request)
        except Exception, e:
                print "[!] Error: " + str(e) + "\n"
                exit(0)
        responseData = response.read()
        jsonRes = json.loads(responseData)
        resultList = jsonRes['d']['results']
        return resultList


def main():
# Help menu and option parsing

	print "##################################################"
	print "##################################################"
	print "##                                              ##"
	print "##  |    _)             |                       ##"
	print "##  __ \  | __ \   _` | __ \   _ \  __ \   _` | ##"
	print "##  |   | | |   | (   | |   | (   | |   | (   | ##"
	print "## _.__/ _|_|  _|\__, |_.__/ \___/ _|  _|\__, | ##"
	print "##               |___/                   |___/  ##"
	print "##                                              ##"
	print "##################################################"
	print "##################################################"
	print "  *                                               ***********"
	print "  * Version 1.1                                             *"
	print "  * For bug report and suggestions: nebulam87@linuxmail.org *"
	print "  * Please check and download upgrades from:                *"
	print "  *        https://github.com/nebulam87/bingbong            *"
	print "  *                                                         *"
	print "  ***********************************************************"

	parser = optparse.OptionParser()

	parser.add_option('-q', '--query', dest='squery', type='string', metavar='<search query>', help='Specify the search string to send to Bing')
	parser.add_option('-f', '--file', dest='openfile', type='string', metavar='<file name>', help='Specify the file from which to retrieve the search queries')
	parser.add_option('-n', '--results', dest='resultNum', metavar='<number of results>', help='Specify the number of results to be retrieved')

	(options, args) = parser.parse_args()
	
# Check if search query or file name were given

	if (options.squery == None) and (options.openfile == None):
		print parser.print_help()
		exit(0)

	else:
		# If option -q given
		if options.openfile == None:
			if options.resultNum != None:
				topResults=options.resultNum
				
			searchQuery = options.squery
			if options.resultNum != None:
				bingResults = bing_search(searchQuery,topResults)
			else:
				bingResults = bing_search(searchQuery)
			
			for line in bingResults:
                                line=str(line)
                                urls=re.findall(r'(https?://[^\s\'"<>]+)', line)
                                if urls:
                                        for i in urls:
                                                if not "datamarket" in i:
							print i
			print "\n"

		# If option -f given
		elif options.squery == None:
			if options.resultNum != None:
				topResults=options.resultNum
				
			queryFile = options.openfile
			try:
				filevar = open(queryFile, 'r')
				for line in filevar.readlines():
					searchQuery = line.strip('\n')
                        		if options.resultNum != None:
						bingResults = bing_search(searchQuery,topResults)
                        		else:
						bingResults = bing_search(searchQuery)
					for z in bingResults:
                                		z=str(z)
                                		urls=re.findall(r'(https?://[^\s\'"<>]+)', z)
                                		if urls:
                                        		for i in urls:
                                                		if not "datamarket" in i:
									print i
					print "\n"


			except Exception, e:
				print "[-] Error " + queryFile + ": " + str(e)
				exit(0)


if __name__ == "__main__":
    main()

