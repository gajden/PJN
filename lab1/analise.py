from os import listdir
from os.path import join

from lab1.build_n_grams_for_language import build_n_grams, load_corpus, check_language


def accuracy(predictions, true_labels):
    correct = 0
    for pred, lab in zip(predictions, true_labels):
        if pred == lab:
            correct += 1
    return correct / float(len(predictions))


def eval(vectorizer, vectors, text):
    predicted = []
    scores = []
    for t in text:
        pred, score = check_language(vectorizer, vectors, t)
        predicted.append(pred)
        scores.append(score)
    return predicted, scores


if __name__ == '__main__':
    corpus_path = '../data/utf/'
    dump_path = '../data/n-grams/'
    test_dir = '../data/test/'

    test_files = listdir(test_dir)
    labels = [f.split('_')[0] for f in test_files]

    test_files = [join(test_dir, f) for f in test_files]
    test_corpus = load_corpus(test_files)

    values = {}
    for n in range(2, 8):
        print('Evaluating n-grams for n: %d' % n)
        vectorizer, vectors = build_n_grams(n, corpus_path, dump_path)
        predicted, scores = eval(vectorizer, vectors, test_corpus)

        for p, t, s in zip(predicted, labels, scores):
            print('Predicted: %s, true: %s, score: %f' % (p, t, s))

