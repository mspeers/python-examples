


'''Complementary DNA

Given a string representing a DNA sequence, return its complementary strand using the following rules:

    DNA consists of the letters "A", "C", "G", and "T".
    The letters "A" and "T" complement each other.
    The letters "C" and "G" complement each other.

For example, given "ACGT", return "TGCA".
'''
def complementary_dna(strand):
    convert ={"A": "T", "T": "A","C":"G","G":"C"}
    result = ""
    for index, letter in enumerate(strand):
        result += convert[letter]

    return result

if __name__ == "__main__":
    print(complementary_dna("ACGT"))



