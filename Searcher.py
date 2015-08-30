from Document import Document

class Searcher:
    def __init__(self, raw_documents):
        self.documents = [Document(raw_doc) for raw_doc in raw_documents]
    
    def search(self, query):
        results = []
        query_document = Document(query)
        query_stems = query_document.get_stems()
        for doc in self.documents:
            score = 0.0
            stemmed_document = doc.get_stems()
            for qstem in query_stems:
                if qstem in stemmed_document:
                    score += 1.0
            score = score / doc.get_length()
            if score > 0.0:
                results.append({"score": score, "text": doc.get_text()})
        return results