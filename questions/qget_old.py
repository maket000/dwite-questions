import urllib2

months = ["Oct", "Nov", "Dec", "Jan", "Feb"]

for year in xrange(2003, 2007):
    for month in months:
        for problem in xrange(1,6):
            fname = "Problem%d%s%d.pdf" % (problem, month, year)
            saveloc = "2002-2006/%d-%s-%d.pdf" % (year, month, problem)
            loc = "http://dwite.ca/old/%s" % (fname)
            print loc
            try:
                response = urllib2.urlopen(loc)
                pdffile = open(saveloc, 'w')
                pdffile.write(response.read())
                pdffile.close()
            except:
                print "NOT FOUND"
