import re

def count_sentences(file1_path, file2_path):
    # Чтение текста из первого файла
    with open(file1_path, 'r', encoding='utf-8') as file1:
        text1 = file1.read()

    # Чтение текста из второго файла
    with open(file2_path, 'r', encoding='utf-8') as file2:
        text2 = file2.read()

    # Разделение текста на предложения
    sentences1 = re.split(r'(?<=[.!?])\s+', text1)
    sentences2 = re.split(r'(?<=[.!?])\s+', text2)

    # Инициализация счетчика одинаковых предложений
    sentence_count = 0

    # Сравнение предложений из двух файлов
    for sentence1 in sentences1:
        for sentence2 in sentences2:
            if sentence1 == sentence2:
                sentence_count += 1

    return sentence_count


file1_path = 'file1.txt'
file2_path = 'file2.txt'
matching_count = count_sentences(file1_path, file2_path)
print(f'Количество одинаковых предложений: {matching_count}')
