import string
import numpy as np


def answer_six(s: string):
    # clean punctuations
    s = s.translate(str.maketrans('', '', string.punctuation))

    # create list from non-empty words' length and return list average
    tokens = s.split()
    list_tokens = [len(t) for t in tokens if len(t) > 0]
    return np.mean(list_tokens)


print(answer_six("Elma, portakal, armut"))
