from os import listdir
from os.path import join
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.io_utils import load_corpus, read_file


def build_n_grams(n, corpus_path):
    vectors = {}
    files = listdir(corpus_path)
    languages = [f.split('_')[0] for f in files]

    paths = [join(corpus_path, f) for f in files]
    corpus = load_corpus(paths)

    ngram_vectorizer = CountVectorizer(ngram_range=(n, n),
                                     token_pattern=r'\w', min_df=1)
    res = ngram_vectorizer.fit_transform(corpus).toarray()
    for lan, vec in zip(languages, res):
        if lan not in vectors.keys():
            vectors[lan] = vec
        else:
            vectors[lan] += vec
    return ngram_vectorizer, vectors


def check_language(vectorizer, vectors, text):
    text_vector = vectorizer.transform([text]).toarray()
    closest = None
    lower_dist = -1

    for lang, vec in vectors.items():
        dist = cosine_similarity(vec, text_vector)
        if dist > lower_dist:
            closest = lang
            lower_dist = dist
    return closest, lower_dist
