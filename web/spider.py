from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

# http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/


class LinkParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		# links normally begin <a href="www.someurl.com"></a>
		if tag == 'a':
			for (key, value) in attrs:
				if key == 'href':
					# get an absolute URL like
					# www.netinstructions.com/somepage.html
					newUrl = parse.urljoin(self.baseUrl, value)
					self.links += [newUrl]


	'''
	getLinks returns web page (useful for searching the word)
	and we return set of links from that web page
	(useful for where to go next)
	'''
	def getLinks(self, url):
		self.links = []
		self.baseUrl = url
		response = urlopen(url)
		# look only at html
		if response.getheader('Content-Type') =='text/html':
			htmlBytes = response.read()
			htmlString = htmlBytes.decode('utf-8')
			# feed handles strings well but not bytes
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "", []

'''
url = takes in url
word = word to find
maxPages = depth limit
'''
def spider(url, word, maxPages):
	pagesToVisit = [url]
	numberVisited = 0
	foundWord = False
	while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
		numberVisited += 1
		url = pagesToVisit[0]
		pagesToVisit = pagesToVisit[1:]
		try:
			print(numberVisited, "Visiting:", url)
			parser = LinkParser()
			data, links = parser.getLinks(url)
			if (data.find(word) > -1):
				foundWord = True
				# add pages we visited to end of our collection of pages to visit
				pagesToVisit += links
				print("Success!")
		except:
			print("Failed!")
	if foundWord:
		print("The word", word, "was found at", url)
	else:
		print("word was never found")


if __name__ == "__main__":
	spider("https://www.dreamhost.com", "secure", 200)