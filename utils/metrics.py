import numpy as np


def levenshtein_distance(seq1, seq2):
    if len(seq1) < len(seq2):
        return levenshtein_distance(seq2, seq1)
    prev_row = np.asarray(range(0, len(seq1) + 1))
    cur_row = np.zeros((len(seq1) + 1, ), dtype=np.uint8)

    for idx, letter in enumerate(seq2):
        cur_row[0] = idx + 1
        for idx1, letter1 in enumerate(seq1):
            add = 1
            if letter == letter1:
                add = 0
            cur_row[idx1 + 1] = min(cur_row[idx1] + 1, prev_row[idx1 + 1] + 1,
                                    prev_row[idx1] + add)
        prev_row[:] = cur_row[:]
    return cur_row[-1]


def pl_levenshtein_distance(seq1, seq2):
    pass


if __name__ == '__main__':
    print(pl_levenshtein_distance('telefon', 'teleofn'))
