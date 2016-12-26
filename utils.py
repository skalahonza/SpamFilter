def read_classification_from_file(file):
    dictionary = {}
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            data = line.split(' ')
            dictionary[data[0]] = data[1]
    return dictionary


def write_classification_to_file(file, dictionary):
    with open(file, 'a', encoding='utf-8') as f:
        for key, value in dictionary.items():
            f.write("%s %s\n" % (key, value))


def compute_word_frequencies_from_text(text):
    """
    Creates the dictionary of words with the number of occurrences for each
    :type text: str
    """
    text = text.translate(str.maketrans('.', ' '))
    text = text.translate(str.maketrans(',', ' '))
    text = text.lower()
    from collections import Counter
    return Counter(text.split())


def extract_sentences_from(text):
    return text.split('.')


def make_coefficient(number):
    if number > 1:
        return 1 / number
    else:
        return number


def compare_dicts(first, second):
    """Compares two dictionaries and returns sameness"""
    sameness = 0
    items = max(len(first), len(second))
    for key, value in first.items():
        if key in second:
            equality = first[key] / second[key]
            sameness += equality / items
    return sameness


def compare_payloads(first, second):
    return 0


def not_empty(first, second):
    if first is None or second is None:
        return False
    else:
        return True


if __name__ == "__main__":
    path = "data\\1\\!truth.txt"
    print(read_classification_from_file(path))
