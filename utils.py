def read_classification_from_file(file):
    dictionary = {}
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            data = line.split(' ')
            dictionary[data[0]] = data[1]
    return dictionary


if __name__ == "__main__":
    path = "data\\1\\!truth.txt"
    print(read_classification_from_file(path))
