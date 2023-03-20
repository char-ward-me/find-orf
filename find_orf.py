# -*- coding: utf-8 -*-
'''Search a string of text representing a DNA sequence for open reading frames (genes)'''
import argparse

##TODO:move DNA class to separate module
##TODO:remove argparse


class DNA:
    '''DNA Class representing physical molecule of DNA. Sequence can be circular or linear.'''
    def __init__(self, sequence, circular=True):
        self.sequence = sequence
        self.circular = circular

    def __repr__(self) -> str:
        return self.sequence
    
    def dnaLower(self):
        self.sequence = self.sequence.lower()
        return self




def main():
    '''Function to search for open reading frames (sequences bounded by 'ATG' and 'TAA/TAG/TGA') '''

    ##Parse input arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sequence",
        type=str,
        help="Enter the DNA sequence you wish to search for open reading frames"
        )

    parser.add_argument(
        "reverse",
        type=bool,
        help="Enter a boolean (True or False) indicating whether to search the reverse compliment of the sequence"
        )

    args = parser.parse_args()
    print(args.sequence)
    if args.reverse is True:
        print(
            "The DNA sequence will be searched for open reading frames in both "
            + "the forward and reverse directions")
    else:
        print("The DNA sequence will be searched for open reading frames in the forward direction only")

    
    seq = DNA(args.sequence, circular=args.reverse)
    seq = seq.dnaLower()

    if seq.circular == False:
        start_codon = 'atg'
        orfs = []
        if start_codon not in seq.sequence:
            print("No open reading frames in input sequence")
        else:
            print(seq.sequence.index(start_codon))

    




if __name__ == "__main__":
    main()
