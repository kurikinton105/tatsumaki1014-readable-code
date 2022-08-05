#辞書に単語を登録
dictionary = ['上手', '一時', '市場']

id_dict = dict()

#変数wordは辞書内に登録されてる単語
for number in range(len(dictionary)):
    id_dict[dictionary[number]] = number + 1 #見出し語の最初の単語のIDを1に

print(id_dict)
