def nlp(*args):
    for arg in args:
        print(arg)

def get_words_en():
    words = open('words.txt').readlines()
    return tuple([word.strip() for word in words])
