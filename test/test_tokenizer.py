import unittest
import ngrams

class TokenizerTest(unittest.TestCase):

    def test_lowercase_and_remove_punctuation(self):
        sentence = "Hi Mark! I hope this message finds you well."
        tokenized = ngrams.tokenize(sentence)

        self.assertEqual(tokenized, [ "hi", "mark", "i", "hope", "this", "message", "finds", "you", "well" ])

    def test_apostrophe(self):
        sentence = "Hi Mark! I hope this message don't find you upset."
        tokenized = ngrams.tokenize(sentence)

        self.assertEqual(tokenized, [ "hi", "mark", "i", "hope", "this", "message", "don't", "find", "you", "upset" ])

    def test_apostrophe2(self):
        sentence = "have been summoned here not to discuss whether it’s best for the empire"
        tokenized = ngrams.tokenize(sentence)

        self.assertEqual(tokenized, [ "have", "been", "summoned", "here", "not", "to", "discuss", "whether", "it’s", "best", "for", "the", "empire" ])

if __name__ == '__main__':
    unittest.main()