"""
    Class to parse DBLP XML data from the file downloaded from http://dblp.uni-trier.de/xml/
"""

import codecs, collections, json, gzip, os, sys, xml.sax, gzip


class DBLPHandler(xml.sax.ContentHandler):
    """
        The handler class is taken and modified from http://projects.csail.mit.edu/dnd/DBLP/DBLP2json.py
    """
    #papertypes = ['article', 'book', 'inproceedings', 'incollection', 'www', 'proceedings', 'phdthesis', 'mastersthesis']
    papertypes = ['article', 'book', 'inproceedings', 'proceedings']

    def __init__(self, filter):
        self.filter  = filter
        self.paper = None
        self.authors = []
        self.year = None
        self.text = ''
        self.papercount = 0
        self.title = ''
        self.booktitle = ''
        self.ee = ''
        self.paper_list = []
        self.paper_active = False

    def startElement(self, name, attrs):

        if name in self.papertypes:
            self.paper = str(attrs['key'])
            if (self.filter in self.paper):
                print(self.paper)
                self.authors = []
                self.year = None
                self.paper_active = True
                self.text = ''
                self.booktitle = ''
                self.ee = ''
                self.title = ''

    def endElement(self, name):
        if (self.paper_active):
            if name == 'author':
                self.authors.append(self.text.strip())
            elif name == 'year':
                self.year = int(self.text.strip())
            elif name =='title':
                self.title = self.text.strip()
            elif name =='booktitle':
                self.booktitle = self.text.strip()
            elif name =='ee':
                self.ee = self.text.strip()

            elif name in self.papertypes:
                paper_data = [self.paper,self.authors,self.year,self.title,self.booktitle,self.ee]
                print(paper_data)
                self.paper_list.append(paper_data)
                self.paper = None
                self.paper_active = False

            self.text = ''

    def characters(self, chars):
        if (self.paper_active):
            self.text += chars

class DBLPXMLParser(object):

    def __init__(self):
        self.description = "Parse DBLP XML downloaded from the website."




if __name__ == '__main__':

    xmlfile = gzip.GzipFile('/Users/adminnobel/Downloads/dblp.xml.gz', 'r')

    dblp = DBLPHandler("conf/kdd")
    parser = xml.sax.parse(xmlfile, dblp)
    import pandas as pd

    pd.DataFrame(dblp.paper_list)

    print(pd)




