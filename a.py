import urllib
import urllib2
from HTMLParser import HTMLParser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

downloaded = []
urll = []
pageno =1
def extract(params):
	print "download"
	url = params[0][1]
	title = params[1][1]+".jpg"
	if downloaded.count(title)==0:
		filedata = urllib2.urlopen(url).read()
		with open(title,'wb') as d:
			d.write(filedata)
		d.close()
		downloaded.append(title)	




class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print attrs
        global pageno
        if len(attrs) ==1 and attrs[0][1].count('?page='+str(pageno+1)):
        	print attrs[0][1]
        	filedataa1 = urllib2.urlopen('http://brookeshaden.com/gallery/'+attrs[0][1]).read()
        	pageno += 1
        	self.feed(filedataa1)
        if len(attrs) == 4:
        	print attrs[1][1]
        	extract(attrs)

        if len(attrs)==2 and attrs[0][0]=='href' and attrs [1][0]=='title':
 
        	global urll
        	if urll.count(attrs) == 0 and attrs[0][1].count('http')!=0:
				print "add"
				print attrs[1][1]
				urll.append(attrs)
				filedataa = urllib2.urlopen(attrs[0][1]).read()
				self.feed(filedataa)


    #def handle_endtag(self, tag):
    #    print "Encountered an end tag :", tag

 #   def handle_data(self, data):
#        print "Encountered some data  :", data



# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
url = 'https://brookeshaden.com'
filedata = urllib2.urlopen(url).read()
parser.feed(filedata)	
