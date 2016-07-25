"""
    Class to parse DBLP XML data from the file downloaded from http://dblp.uni-trier.de/xml/
"""

import codecs, collections, json, gzip, os, sys, xml.sax, gzip


class DBLPHandler(xml.sax.ContentHandler):
    """
        The handler class is taken and modified from http://projects.csail.mit.edu/dnd/DBLP/DBLP2json.py
    """
    papertypes = ['article', 'book', 'inproceedings', 'incollection', 'www', 'proceedings', 'phdthesis', 'mastersthesis']

    def __init__(self, out):
        self.out = out
        self.paper = None
        self.authors = []
        self.year = None
        self.text = ''
        self.papercount = 0
        self.edgecount = 0

    def startElement(self, name, attrs):

        attr_list = attrs.values()
        if(len(attr_list) > 0):
            if("ijcai" in attr_list[0]):
                self.papercount+=1

        if name in self.papertypes:
            self.paper = str(attrs['key'])
            self.authors = []
            self.year = None

        elif name in ['author', 'year', 'title','booktitle']:
            self.text = ''


    def endElement(self, name):
        if name == 'author':
            self.authors.append(self.text)

        if name == 'year':
            self.year = int(self.text.strip())
        elif name in self.papertypes:
            # self.write_paper()
            self.paper = None

    # def write_paper(self):
    #     if self.papercount:
    #         self.out.write(',\n')
    #     self.papercount += 1
    #     self.edgecount += len(self.authors)
    #     json.dump([self.paper, self.authors, self.year], self.out)

    def characters(self, chars):
        self.text += chars

class DBLPXMLParser(object):

    def __init__(self):
        self.description = "Parse DBLP XML downloaded from the website."




if __name__ == '__main__':

    xmlfile = gzip.GzipFile('/home/arun/data/dblp/dblp.xml.gz', 'r')
    out = gzip.GzipFile('/tmp/data.out', 'w')
    dblp = DBLPHandler(out)
    parser = xml.sax.parse(xmlfile, dblp)
    print(dblp.papercount)




