import re

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
