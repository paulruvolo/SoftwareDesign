# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:02:04 2014

@author: pruvolo
"""

from os import path

def load_seq(fasta_file):
    """ Reads a FASTA file and returns the DNA sequence as a string.

    fasta_file: the path to the FASTA file containing the DNA sequence
    returns: the DNA sequence as a string
    """
    retval = ""
    f = open(fasta_file)
    lines = f.readlines()
    for l in lines[2:]:
        retval += l[0:-1]
    f.close()
    return retval
    
def load_salmonella_genome():
    f = open(path.join('.','data','salmonella_all_proteins'))
    lines = f.readlines()
    retval = []
    gene = []
    is_amino_acid_seq = False
    
    for line in lines:
        if line[5:].find("CDS") == 0:
            coords = line[21:-1]
            if len(gene) == 3:
                retval.append(gene)
            gene = [coords]
        elif line[21:].find("/protein_id") == 0:
            gene.append(line[34:-2])
        elif line[21:].find("/translation") == 0:
            if line[-2] != '"':
                amino_acid_seq = line[35:-1]
                is_amino_acid_seq = True
            else:
                amino_acid_seq = line[35:-2]
                gene.append(amino_acid_seq)
        elif is_amino_acid_seq:
            if line[-2] != '"':
                amino_acid_seq += line[21:-1]
            else:
                amino_acid_seq += line[21:-2]
                is_amino_acid_seq = False
                gene.append(amino_acid_seq)
    if len(gene) == 3:
         retval.append(gene)
    f.close()
    return retval
