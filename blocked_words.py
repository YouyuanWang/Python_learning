# coding: utf-8

# read the blocked words
def load_blocked():
    with open('test.txt') as f:
        global blocked_words
        blocked_words = [word.strip() for word in f.readlines() if f]

#  检测屏蔽词汇
def word_filter(text, charset = 'utf-8', symbol = '*'):
    for w in blocked_words:
        text = text.replace(w, symbol*len(w.decode(charset)))
    return text

if __name__ == '__main__':
    load_blocked()
    while True:
        test = raw_input('words to be test:\n')
        if not test:
            break
        print word_filter(test)




