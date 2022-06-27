import numpy as np


class WordFormOut(object):
    def __init__(self, word: str, normal_form: str, pos: str, tag: str, vector: np.array, score: float):
        self.word = word
        self.normal = normal_form
        self.pos = pos
        self.tag = tag
        self.vector = vector
        self.score = score
        self.weighted_vector = np.zeros_like(self.vector)
        self.possible_forms = []

    def __repr__(self):
        return "<normal={}; word={}; pos={}; tag={}; score={}>"\
            .format(self.normal, self.word, self.pos, self.tag, "%0.4f" % self.score)

    def __eq__(self, other):
        return (self.normal, self.word, self.pos, self.tag) == \
               (other.normal, other.word, other.pos, other.tag)

    def __hash__(self):
        return hash((self.normal, self.word, self.pos, self.tag))
