


def get_words(file_name):
    n = open(file_name)
    lines = n.readlines()
    words = []
    for line in lines:
        words.append(line.strip())
    n.close()
    return words
