import re

class Corpus:
    def __init__(self, raw_documents):
        self.documents = [Document(raw_doc) for raw_doc in raw_documents]

    def get_documents(self):
        return self.documents


class Document:
    next_id = 0
    
    def __init__(self, raw_document, min_word_length = 3):
        self.text = raw_document
        self.min_word_length = min_word_length
        self.length = len(raw_document)
        self.stems = self._stem(self.text)
        self.id = Document.get_next_id()
    
    @staticmethod
    def get_next_id():
        next_id = Document.next_id
        Document.next_id += 1
        return next_id
    
    # Crude, pseudo-stemming algorithm to see what we can
    # get away with.
    def _stem(self, text):
        stems = []
        words = re.split("\W+", text)
        for word in words:
            lc_word = word.lower()
            word_length = len(lc_word)
            if word_length >= self.min_word_length:
                stem = lc_word[:word_length/2]
                stems.append(lc_word[:word_length/2])
            else:
                stems.append(lc_word)
        return stems

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text
    
    def get_length(self):
        return self.length
    
    def get_stems(self):
        return self.stems


class Metrics:
    def __init__(self, corpus = Corpus([])):
        self.term_frequencies = dict()
        documents = corpus.get_documents()
        for document in documents:
            document_id = document.get_id()
            if document_id not in self.term_frequencies.keys():
                self.term_frequencies[document_id] = dict()
            stems = document.get_stems()
            for stem in stems:
                self.term_frequencies[document_id][stem] = TermFrequency(document, stem)

    def get_term_frequency(self, document_id, term):
        return self.term_frequencies[document_id][term].get_frequency()


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


class TermFrequency:
    def __init__(self, document, term):
        self.frequency = document.get_stems().count(term)

    def get_frequency(self):
        return self.frequency
