import os

from corpus import Corpus
from my_email import Email
from trainingcorpus import TrainingCorpus
from utils import write_classification_to_file


class MyFilter:
    def __init__(self):
        self.spams = []
        self.hams = []
        self.trained = False
        self.blacklist = []
        # Load black list
        # Google open source blacklist used for non trained filter only
        with open('blacklist.txt', 'rt', encoding='utf-8') as f:
            for line in f.readlines():
                line.replace('\n','')
                self.blacklist.append(line)

    def train(self, directory):
        trainer = TrainingCorpus(directory)
        self.spams = trainer.spams
        self.hams = trainer.hams
        self.trained = True

    def test(self, directory):
        corp = Corpus(directory)
        result = {}
        if self.trained:
            for fname, body in corp.emails():
                SpamSum = 0
                HamSum = 0
                examined = Email(fname, body)
                for spam in self.spams:
                    SpamSum += Email.compare_emails(examined, spam)
                for ham in self.hams:
                    HamSum += Email.compare_emails(examined, ham)
                if SpamSum / len(self.spams) > HamSum / len(self.hams):
                    result[fname] = 'SPAM'
                else:
                    result[fname] = 'OK'
            write_classification_to_file(directory + os.path.sep + '!prediction.txt', result)
        else:
            for fname, body in corp.emails():
                counter = 0
                for word in self.blacklist:
                    if word in body:
                        counter += 1
                if counter > 3:
                    result[fname] = 'SPAM'
                else:
                    result[fname] = 'OK'
            write_classification_to_file(directory + os.path.sep + '!prediction.txt', result)
