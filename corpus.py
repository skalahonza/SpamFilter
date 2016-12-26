import os

from my_email import Email


class Corpus:
    def __init__(self, folder):
        self.folder = folder
        self.files = os.listdir(folder)

    def emails(self):
        # ignore some file
        for file in self.files:
            if file[0] == '!':
                continue
            filePath = self.folder + os.path.sep + file
            with open(filePath, 'rt', encoding='utf-8') as f:
                yield file, f.read()


if __name__ == "__main__":
    path = "data\\2"
    corpus = Corpus(path)
    count = 0
    # Go through all emails and print the filename and the message body
    for fname, body in corpus.emails():
        print(fname)
        print(body)
        print('-------------------------')
        count += 1
        email = Email(fname, body)
    print('Finished: ', count, 'files processed.')
