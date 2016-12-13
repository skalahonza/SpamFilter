import os

from Ukoly.SpamFilter.corpus import Corpus
from Ukoly.SpamFilter.utils import read_classification_from_file


class TrainingCorpus(Corpus):
    def __init__(self, folder):
        self.folder = folder
        self.spams = []
        self.hams = []
        corp = Corpus(folder)
        for fname, content in corp.emails():
            if self.is_ham(fname):
                self.hams.append((fname, content))
            else:
                self.spams.append((fname, content))

    def get_class(self, email_file):
        classification = read_classification_from_file(self.folder + os.path.sep + "!truth.txt")
        return classification[email_file]

    def is_ham(self, email_file):
        return self.get_class(email_file) == "HAM"

    def is_spam(self, email_file):
        return self.get_class(email_file) == "SPAM"
