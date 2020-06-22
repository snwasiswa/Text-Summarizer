""" The file test whether the class Summary works as expected"""

import unittest
from textsummary import Summary

class MyTestCase(unittest.TestCase):
    """ Tests for the class Summary"""
    def test_get_summary(self):
        """Test whether the code summarizes input given or not"""
        sum = Summary(
            "There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar.")

        # Test the condition
        self.assertTrue(sum.get_summary)

if __name__ == '__main__':
    unittest.main()
