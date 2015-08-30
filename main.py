#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from Document import Document
from Searcher import Searcher

if __name__ == "__main__":
    searcher = Searcher(["This is a test", \
                         "These are some longer words in a sentence", \
                         "The quick, brown fox jumped over the lazy hen"])
    for doc in searcher.documents:
        print "%s\n" % doc.get_stems()
    search_results = searcher.search("these")
    for idx, result in enumerate(search_results):
        print idx
        print "%s\n" % result