import sys								#System Library: To get the Command Line Parameter
import urllib2							#Website Reader Library
from HTMLParser import HTMLParser		#HTML Parser Library
from datetime import datetime			#Date/Time Library

print "START: " + datetime.now().strftime("%d-%B-%Y %H:%M:%S")

# create a subclass and override the handler methods
class SimpleHTMLParser(HTMLParser):

	#Start Container
    def handle_starttag(self, tag, attrs):
    	global html
    	global isParsed

    	#Tabel Jadwal
    	if  (tag == "table") or (tag == "tr") or (tag == "td"):
			isParsed = 1

			html += "<" + tag
			print "Found a START TAG:", tag
			for attr in attrs:
				html += " " + attr[0] + "='" + attr[1] + "'"
				print "		with", attr[0], "=", attr[1]

				#Table Navigasi Kota
				if (attr[0] == "class") and (attr[1] == "table_navigasi"):
					html += " style='display:none;'"

			html += ">"
 
	#Data Container
    def handle_data(self, data):
    	global html
    	if (isParsed == 1):
        	html += data
	        print "Found some DATA  :", data

	#End Container
    def handle_endtag(self, tag):
    	global html
    	global isParsed

    	if  (tag == "table") or (tag == "tr") or (tag == "td"):
        	html += "</" + tag + ">"
        	print "Found an END TAG :", tag
        	isParsed = 0

# instantiate the parser and fed it some HTML
html = ""
isParsed = 0

parser = SimpleHTMLParser()

# Parse the HTML to A new HTML Table
parser.feed(urllib2.urlopen(str(sys.argv[1])).read())
with open("JadwalSholatPKPU.html", 'w') as writer:
	writer.write(html)

print "END: " + datetime.now().strftime("%d-%B-%Y %H:%M:%S")
