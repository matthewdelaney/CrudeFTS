from Document import Document

class TermFrequency:
    def __init__(self, document, term):
        self.frequency = document.get_stems().count(term)

    def get_frequency(self):
        return self.frequency
