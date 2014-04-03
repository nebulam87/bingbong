#!/usr/bin/python

# Author: nebulam87 (nebulam87@linuxmail.org) 
# Version: 1.0.1 

import urllib
import urllib2
import json
import sys
import re
 
def main():
	if len(sys.argv)==2:
		if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
			print "Usage: " + str(sys.argv[0]) + " [your search]\n\n   If your search string contains spaces, quotes need to be added."
			print "   Example: " + str(sys.argv[0]) + " \'cute cats\'\n"
			exit(0)
		else:
			searchQuery = sys.argv[1]
			bingResults = bing_search(searchQuery)
			for line in bingResults:
				line=str(line)
				urls=re.findall(r'(https?://[^\s\'"<>]+)', line)
		
# Search and group as a raw string anything that starts as http(s?):// and followed by anything that is not a whitespace (\s) nor a quote or double-quote. It searches it on the string contained in variable "line"

				if urls:
					for i in urls:
						if not "datamarket" in i:
							print i	

	else:
		print "Usage: " + str(sys.argv[0]) + " [your search]\n\n   If your search string contains spaces, quotes need to be added."
		print "   Example: " + str(sys.argv[0]) + " \'cute cats\'\n"
		exit(0)

def bing_search(query):
	#search type: Web
	bingkey = '[insert Bing API key here]'
	query = urllib.quote(query)
	# create request for authentication
	userAgent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
	credentials = (':%s' % bingkey).encode('base64')[:-1]
	auth = 'Basic %s' % credentials
	url = 'https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27'+query+'%27&$top=200&$format=json'
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

 
if __name__ == "__main__":
    main()

