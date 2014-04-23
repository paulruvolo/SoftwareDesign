# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def pair_list_to_dictionary(L):
    # TODO: need to write this code!!!
    return True

class PairListToDictionaryTests(unittest.TestCase):
    def test_pair_list_to_dictionary_basic(self):
        self.assertEqual(pair_list_to_dictionary([1,'a',5]),{1:'a'})
        self.assertEqual(pair_list_to_dictionary(['hello','a','test','b']),{'hello':'a','test':'b'})

if __name__ == '__main__':
    unittest.main()