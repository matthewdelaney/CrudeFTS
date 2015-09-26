from Document import Document

class Corpus:
    def __init__(self, raw_documents):
        self.documents = [Document(raw_doc) for raw_doc in raw_documents]

    def get_documents(self):
        return self.documents