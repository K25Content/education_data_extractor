# We can also make this as extracting all the rows first and then extracting data from each row

import urllib2
from lxml import html
import xlwt

schoolnames = []
schooltype = []
address = []
phoneno = []
book = xlwt.Workbook()

for x in range(1, 23):
	page = urllib2.urlopen("http://www.mypaathshala.in/list-of-schools.php?page="+str(x))

	page_content = page.read()

	with open('page'+str(x)+'.html', 'w') as fid:
		fid.write(page_content)
		tree = html.fromstring(page_content)
		schoolnames.extend(tree.xpath('//span[@class="big-normal-text"]/strong/text() | //span[@class="big-normal-text"]/a/strong/text()'))
		schooltype.extend(tree.xpath('//span[@class="big-normal-text"]/text()'))
		address.extend(tree.xpath('//td[@class="big-normal-text"]/text()'))
		phoneno.extend(tree.xpath('//p[@class="big-normal-text"]/text()'))


		sh = book.add_sheet(str(x))

		for m, e1 in enumerate(schoolnames):
			sh.write(m, 0, e1)

		for n, e2 in enumerate(address):
			sh.write(n, 1, e2)

		for o, e3 in enumerate(phoneno):
			sh.write(o, 2, e3)

book.save('data.xls')