import unittest
import ngrams

class CounterTest(unittest.TestCase):

    def test_one_word(self):
        sentence = [ "hi", "mark", "i", "hope", "this", "message", "finds", "you", "well", "see", "you" ]
        counter1 = ngrams.NgramCounter(1)
        for word in sentence:
            counter1.process_word(word)

        self.assertEqual(counter1.top(3)[0], (" you", 2))

    def test_3_words(self):
        sentence = [ "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c" ]
        counter1 = ngrams.NgramCounter(3)
        for word in sentence:
            counter1.process_word(word)
        top = counter1.top(4)
        self.assertEqual(top[0], ("a b c", 4))
        self.assertEqual(top[1], ("b c a", 3))
        self.assertEqual(top[2], ("c a b", 3))
        self.assertEqual(len(top), 3) # no more 3 sequences
        
if __name__ == '__main__':
    unittest.main()