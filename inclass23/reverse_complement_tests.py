# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

def reverse_complement(s):
    return ""

class ReverseComplementTests(unittest.TestCase):
    def test_reverse_complement_basic(self):
        self.assertEqual(reverse_complement('ACGG'),'CCGT')

if __name__ == '__main__':
    unittest.main()