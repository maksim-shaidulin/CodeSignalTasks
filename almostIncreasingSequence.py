def almostIncreasingSequence(sequence):
    def increasingSequence(sequence):
        
        for i in range(len(sequence) - 1):
            if sequence[i] >= sequence[i+1]:
                return False, i
        return True, 0

    res, idx = increasingSequence(sequence)
    if res:
        return True

    for i in range(idx, len(sequence)):
        cpy = sequence.copy()
        del cpy[i]
        if increasingSequence(cpy)[0]:
            return True

    return False
