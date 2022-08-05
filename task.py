
import sys


def main(args):
    #辞書に単語を登録
    dictionary = ['上手', '一時', '市場']

    id_dict = dict()

    #変数wordは辞書内に登録されてる単語
    for number in range(len(dictionary)):
        id_dict[number+1] = dictionary[number] #見出し語の最初の単語のIDを1に


    #辞書の単語を出力
    if len(args) == 0:
        for key in id_dict:
            print(key, ":", id_dict[key])
    else:
        for id_args in args:
            print(id_args, ":", id_dict[int(id_args)])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))