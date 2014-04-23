# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def split_dictionary(D):
    # TODO: need to write this code!!!
    return True

class SplitDictionaryTests(unittest.TestCase):
    def test_split_dictionary_basic(self):
        self.assertEqual(split_dictionary({'a':2,'B':'hello','c':'t'}), [{'B': 'hello'}, {'a':  2, 'c':  't'}])

if __name__ == '__main__':
    unittest.main()