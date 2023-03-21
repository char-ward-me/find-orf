'''Methods and attributes of DNA class'''

class DNA:
    '''DNA Class representing physical molecule of DNA'''

    def __init__(self, sequence, circular=True):
        self.sequence = sequence
        self.circular = circular

    def __repr__(self) -> str:
        return self.sequence

    def reverse_complement(self):
        '''Produces the reverse complement of the DNA sequence'''
        reverse_complement = ''
        base_pairs = {'A':'T','T':'A','G':'C','C':'G'}
        for char in self.sequence:
            try:
                reverse_complement = reverse_complement + base_pairs[char]
            except KeyError:
                reverse_complement = reverse_complement + 'N'
        return reverse_complement
