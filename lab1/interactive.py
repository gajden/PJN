from lab1.build_n_grams_for_language import build_n_grams, check_language

if __name__ == '__main__':
    corpus_path = '../data/utf'
    dump_path = '../data/n-grams'

    print('Choose n size: ')
    n = int(input())

    print('Building n-grams.')
    vectorizer, language_vectors = build_n_grams(n, corpus_path)

    user_input = None
    while user_input != 'q':
        print('Type your sentence:')
        user_input = input()
        language, score = check_language(vectorizer, language_vectors, user_input)
        print('Language: %s, with score: %f' % (language, score))
