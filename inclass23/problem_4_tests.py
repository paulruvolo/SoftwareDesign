# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def in_language(s):
    # TODO: need to write this code!!!
    return True

class InLanguageTests(unittest.TestCase):
    def test_in_language_basic(self):
        self.assertFalse(in_language('aaab'))
        self.assertFalse(in_language('aaaccc'))
        self.assertTrue(in_language(''))
        self.assertTrue(in_language('aaaabbbb'))

if __name__ == '__main__':
    unittest.main()