import urllib2
import re

question_pat = r"\.\./\.\./questions/.*.html"

qlocs = []

for url_num in xrange(60):
    try:
        rawpage = urllib2.urlopen("http://dwite.ca/home/contest/%d.html" % (url_num)).read()
        qlocs += re.findall(question_pat, rawpage)
    except:
        pass

for i in xrange(len(qlocs)):
    question_name = qlocs[i][16:]
    try:
        location = "http://dwite.ca/questions/" + question_name
        print "GETTING", location,
        rfile = open("2007-2013/%s" % question_name, 'w')
        rfile.write(urllib2.urlopen(location).read())
        rfile.close()
        print "GOT"
    except:
        print "!!!!!!!!!!!!!!!!!!!!!!!"
        print "NOT GOT"
        print "!!!!!!!!!!!!!!!!!!!!!!!"