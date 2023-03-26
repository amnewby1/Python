"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    def __init__(self, path):
      self.read_file(path)

    def read_file(self, path):
        file = open(path, 'r')  
        self.words = file.readlines()
        print(f"{len(self.words)} words read")

    def random(self):
       return random.choice(self.words).strip()