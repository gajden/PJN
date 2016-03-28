
def read_file(path):
    with open(path, 'r') as f:
        text = f.read()
    return text


def load_corpus(files):
    corpus = []
    for f in files:
        corpus.append(read_file(f))
    return corpus
