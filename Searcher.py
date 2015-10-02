from Corpus import Corpus
from Document import Document
from Metrics import Metrics

class Searcher:
    def __init__(self, raw_documents):
        self.corpus = Corpus(raw_documents)
        self.metrics = Metrics(self.corpus)
    
    def search(self, query):
        results = []
        query_document = Document(query)
        query_stems = query_document.get_stems()
        documents = self.corpus.get_documents()
        for doc in documents:
            document_id = doc.get_id()
            score = 0.0
            stemmed_document = doc.get_stems()
            for qstem in query_stems:
                if qstem in stemmed_document:
                    term_frequency = self.metrics.get_term_frequency(document_id, qstem)
                    score += term_frequency
            if score > 0.0:
                results.append({"id": doc.get_id(), "score": score, "text": doc.get_text()})
        return results

    def get_corpus(self):
        return self.corpus
