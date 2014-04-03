# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 10:40:40 2014

@author: pruvolo
"""

import unittest

class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ initializes a DNASequence with the specified nucleotides.
            nucleotides: the nucleotides represented as a string of capital letters
            in { ’A’ , ’C’ , ’G’ , ’T’} """
        pass

    def get_reverse_complement(self):
        """ Computes the reverse complement of the DNA sequence .
            returns: the reverse complement DNA sequence represented
            as an object of type DNASequence """
        pass

    def get_proportion_ACGT(self) :
        """ Computes the proportion of nucleotides in the DNA sequence
            that are ’A’, ’C’, ’G’, and ’T’
            returns: a dictionary where each key is a nucleotide and the
            corresponding value is the proportion of nucleotides in the DNA
            sequence that are that nucleotide. """
        pass
    
class DNASequenceTests(unittest.TestCase):
    def test_DNASequence_init(self):
        pass
    
    def test_DNASequence_get_reverse_complement(self):
        # note, to test equality of two object by attributes use:
        # obj1.__dict__ == obj2.__dict__
        pass
    
    def test_DNASequence_get_proportion_ACGT(self):
        pass

if __name__ == '__main__':
    unittest.main()