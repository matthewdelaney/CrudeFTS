#-*-coding:utf8;-*-
#qpy:2
#qpy:console

from CrudeFTS import Document, Searcher

if __name__ == "__main__":
    searcher = Searcher(["This is a test", \
                         "These are some longer words in a sentence and these are additional words", \
                         "The quick, brown fox jumped over the lazy hen"])
    documents = searcher.get_corpus().get_documents()
    for doc in documents:
        print "Document %d => %s\n" % (doc.get_id(), doc.get_stems())
    search_results = searcher.search("these")
    for idx, result in enumerate(search_results):
        print idx
        print "%s\n" % result
