import email.parser

from utils import compute_word_frequencies_from_text
from utils import compare_dicts
from utils import extract_email_address

# Coefficients for comparing
SUBJECT_PRIORITY = 0.1
FROM_PRIORITY = 0.1
RECEIVED_PRIORITY = 0.1
WARNING_PRIORITY = 0.1
PRECEDENCE_PRIORITY = 0.1
PAYLOAD_PRIORITY = 0.1


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

    def compare_emails(self, first, second):
        """
        Compares two emails and returns match as a decimal value or 1 if they are same
        :type first: Email
        :type second: Email
        """
        match = 0
        # Compare subject
        if first.subject == second.subject:
            match += SUBJECT_PRIORITY
        else:
            match += compare_dicts(compute_word_frequencies_from_text(first.subject),
                                   compute_word_frequencies_from_text(second.subject)) * SUBJECT_PRIORITY / 2
            # they are not equal, only some words occurrences

        # Compare from
        if extract_email_address(first.From) == extract_email_address(second.From):
            match += FROM_PRIORITY

        # compare precedence
        if first.precedence == second.precedence:
            match += PRECEDENCE_PRIORITY

        # compare X authentication warning
        if first.x_authentication_warning == second.x_authentication_warning:
            match += WARNING_PRIORITY

        # compare receive history chain
        length = max(len(first.received), len(second.received))
        receive_match = set(first.received).intersection(second.received)
        match += (len(receive_match) / length) * RECEIVED_PRIORITY

        # compare payloads
        return match
