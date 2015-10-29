from Corpus import Corpus
from TermFrequency import TermFrequency

class Metrics:
    def __init__(self, corpus = Corpus([])):
        self.term_frequencies = dict()
        documents = corpus.get_documents()
        for document in documents:
            stems = document.get_stems()
            for stem in stems:
                document_id = document.get_id()
                if document_id not in self.term_frequencies.keys():
                    self.term_frequencies[document_id] = dict()
                self.term_frequencies[document_id][stem] = TermFrequency(document, stem)

    def get_term_frequency(self, document_id, term):
        return self.term_frequencies[document_id][term].get_frequency()
