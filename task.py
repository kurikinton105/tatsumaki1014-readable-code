import sys


def main(args):
    with open('dictionary-data.txt', 'r', encoding='utf-8') as f:
        word_list = f.readlines()

    #辞書の作成
    id_dict = dict()
    #変数wordは辞書内に登録されてる単語
    for i in range(len(word_list)):
        word_list[i] = word_list[i].replace('\n', '')
        kanji_tmp, hiragana_tmp = word_list[i].split(' ')
        id_dict[i + 1] = {'kanji': kanji_tmp, 'hiragana': hiragana_tmp}

    #辞書の単語を出力
    if len(args) == 0:
        args = id_dict.keys()
    for id_args in args:
        print(id_args, ":", id_dict[int(id_args)]['kanji'],
        id_dict[int(id_args)]['hiragana'])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))