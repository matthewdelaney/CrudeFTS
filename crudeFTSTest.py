#-*-coding:utf8;-*-
#qpy:2
#qpy:console

import unittest
from CrudeFTS import Document

class DocumentTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_document_text_is_stored(self):
        someText = "This is a test"
        document = Document(someText)
        self.assertEqual(document.get_text(), someText)

if __name__ == "__main__":
    unittest.main()