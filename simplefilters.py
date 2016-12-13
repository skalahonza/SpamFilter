import os
from random import randint

from Ukoly.SpamFilter.basefilter import BaseFilter
from Ukoly.SpamFilter.corpus import Corpus
from Ukoly.SpamFilter.utils import write_classification_to_file


class NaiveFilter(BaseFilter):
    def test(self, email_dir):
        corpus = Corpus(email_dir)
        dictionary = {}
        for fname, content in corpus.emails():
            dictionary[fname] = "OK"
        write_classification_to_file(email_dir + os.path.sep + "!prediction.txt", dictionary)


class ParanoidFilter(BaseFilter):
    def test(self, email_dir):
        corpus = Corpus(email_dir)
        dictionary = {}
        for fname, content in corpus.emails():
            dictionary[fname] = "SPAM"
        write_classification_to_file(email_dir + os.path.sep + "!prediction.txt", dictionary)


class RandomFilter(BaseFilter):
    def test(self, email_dir):
        corpus = Corpus(email_dir)
        dictionary = {}
        for fname, content in corpus.emails():
            if randint(0, 1) == 1:
                dictionary[fname] = "SPAM"
            else:
                dictionary[fname] = "OK"
        write_classification_to_file(email_dir + os.path.sep + "!prediction.txt", dictionary)
