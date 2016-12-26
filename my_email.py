import email.parser
from email.message import Message

from utils import compute_word_frequencies_from_text
from utils import compare_dicts
from utils import compare_payloads
from utils import not_empty

# Coefficients for comparing
TOTAL_PRIORITIES = 11
SUBJECT_PRIORITY = 3 / TOTAL_PRIORITIES
FROM_PRIORITY = 3 / TOTAL_PRIORITIES
RECEIVED_PRIORITY = 1 / TOTAL_PRIORITIES
WARNING_PRIORITY = 1 / TOTAL_PRIORITIES
SECONDARY_PRIORITY = 1 / TOTAL_PRIORITIES
PAYLOAD_PRIORITY = 2 / TOTAL_PRIORITIES


class Email:
    def __init__(self, file_id, string):
        self.file_id = file_id
        self.text = string
        msg = email.message_from_string(string)
        self.AllHeaders = msg._headers
        # properties that are not defined will be None
        self.subject = msg['Subject']
        if self.subject is not None:
            self.subject_dict = compute_word_frequencies_from_text(self.subject)
        self.From = msg['From']
        # can contain valuable information - for example - suspicious domain differences
        self.x_authentication_warning = msg['X-Authentication-Warning']
        # serialize received history
        self.received = []
        for header in msg._headers:
            if header[0] == 'Received':
                self.received.append(header[1])
        self.payloads = []
        self.payloads_dicts = []
        self.payloads = list(serialize_payload(msg.get_payload()))
        for payload in self.payloads:
            if payload is not None:
                self.payloads_dicts = compute_word_frequencies_from_text(payload)

    @staticmethod
    def compare_emails(first, second):
        """
        Compares two emails and returns match as a decimal value or 1 if they are same
        :type first: Email
        :type second: Email
        """
        match = 0
        ignored = ['Subject', 'From', 'X-Authentication-Warning', 'Received']
        # Compare subject
        if first.subject == second.subject:
            match += SUBJECT_PRIORITY
        elif not_empty(first.subject, second.subject):
            match += compare_dicts(first.subject_dict,
                                   second.subject_dict) * SUBJECT_PRIORITY / 2
            # they are not equal, only some words occurrences

        # Compare from
        if first.From == second.From:
            match += FROM_PRIORITY

        # compare X authentication warning
        if first.x_authentication_warning == second.x_authentication_warning:
            match += WARNING_PRIORITY

        # compare receive history chain
        length = max(len(first.received), len(second.received))
        receive_match = set(first.received).intersection(second.received)
        if length > 0:
            match += (len(receive_match) / length) * RECEIVED_PRIORITY

        MatchedHeaders = 0
        # compare secondary headers
        for header in first.AllHeaders:
            if header[0] not in ignored:
                if header in second.AllHeaders:
                    MatchedHeaders += 1

        match += SECONDARY_PRIORITY * MatchedHeaders / max(len(first.AllHeaders), len(second.AllHeaders))
        # compare payloads
        payloads_max_count = max(len(first.payloads_dicts), len(second.payloads_dicts))
        if payloads_max_count > 0:
            for dict1 in first.payloads_dicts:
                for dict2 in second.payloads_dicts:
                    match += compare_dicts(dict1, dict2) * PAYLOAD_PRIORITY / payloads_max_count
        return match


def serialize_payload(payload):
    if payload is Message:
        serialize_payload(payload.get_payload())
    elif payload is str:
        yield payload
