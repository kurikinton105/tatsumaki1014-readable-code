#テキストファイルに書き込み
dictionary_file = open('dictionary-data.txt', 'w', encoding='UTF-8')
dictionary_file.write('上手\n')
dictionary_file.write('一時\n')
dictionary_file.write('市場\n')
dictionary_file.close()

#wordsはテキストファイルに保存されている単語
dictionary_file = open('dictionary-data.txt', 'r', encoding='UTF-8')
words = dictionary_file.read()
print(words)
dictionary_file.close()
