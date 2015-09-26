from Corpus import Corpus
from Document import Document

class Searcher:
    def __init__(self, raw_documents):
        self.corpus = Corpus(raw_documents)
    
    def search(self, query):
        results = []
        query_document = Document(query)
        query_stems = query_document.get_stems()
        documents = self.corpus.get_documents()
        for doc in documents:
            score = 0.0
            stemmed_document = doc.get_stems()
            for qstem in query_stems:
                if qstem in stemmed_document:
                    score += len(qstem)
            if score > 0.0:
                results.append({"score": score, "text": doc.get_text()})
        return results

    def get_corpus(self):
        return self.corpus