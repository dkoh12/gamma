import requests
import re
import urllib.parse

#collect email addresses from website

# email regexp:
# letter/number/dot/comma @ letter/number/dot/comma . /letter/number
email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')

# HTML <a> regexp
# matches href=""
link_re = re.compile(r'href="(.*?)"')

def crawl(url, depth):
	if depth == 0:
		return

	# get webpage
	req = requests.get(url)
	result = []

	# check if successful
	if(req.status_code != 200):
		return []

	# find and follow all links
	links = link_re.findall(req.text)
	for link in links:
		# get absolute URL for a link
		link = urllib.parse.urljoin(url, link)
		result += crawl(link, depth - 1)

	# find all emails on current page
	result += email_re.findall(req.text)
	return result

emails = crawl('https://www.nfl.com', 5)

print("scrapped email addresses:")
for e in emails:
	print(e)



