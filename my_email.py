import email.parser

from utils import compute_word_frequencies_from_text


class MessageBody:
    def __init__(self, content, content_type):
        self.content = content
        # key - word, word, number of occurrences
        # is html ?
        # compare html signatures - clickbaits etc
        # clear html entities nd extract pure text
        # examine words formations and occurrences
        self.sentences = []
        self.urls = []
        self.words = compute_word_frequencies_from_text(content)


class Email:
    def __init__(self, file_id, string):
        self.file_id = file_id
        self.text = string
        msg = email.message_from_string(string)
        # properties that are not defined will be None
        self.subject = msg['Subject']
        self.From = msg['From']
        self.sender = msg['Sender']
        self.content_type = msg['Content-Type']
        self.precedence = msg['Precedence']
        # can contain valuable information - for example - suspicious domain differences
        self.x_authentication_warning = msg['X-Authentication-Warning']
        # serialize received history
        self.received = []
        for header in msg._headers:
            if header[0] == 'Received':
                self.received.append(header[1])
        self.payloads = []
        if msg.is_multipart():
            for payload in msg.get_payload():
                self.payloads.append(payload.get_payload())
        else:
            self.payloads.append(msg.get_payload())
        pass

    def compare_emails(self, email, learned_data):
        # Compare subject
        # Compare from
        # Compare sender
        # compare precedence
        # compare X authentication warning
        # compare receive history chain
        # compare payloads
        pass
