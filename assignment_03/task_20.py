# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# Ввод: ноутбук
# Вывод: 12
# Ввод: laptop
# Вывод: 9
# Ввод: Zimbabwe
# Вывод: 26
import functions

dictRu = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
          2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
          3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
          4: ['Й', 'Ы'],
          5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
          8: ['Ш', 'Э', 'Ю'],
          10: ['Ф', 'Щ', 'Ъ']}

dictEn = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
          2: ['D', 'G'],
          3: ['B', 'C', 'M', 'P'],
          4: ['F', 'H', 'V', 'W', 'Y'],
          5: ['K'],
          8: ['J', 'X'],
          10: ['Q', 'Z']}
word = input("Введите слово на русском или английском языке: ")
lang = functions.detectRuEn(word[0])
count = 0

while lang != '':
    if lang == 'ru':
        for i in range(len(word)):
            if word[i].upper() in dictRu[1]:
                count += 1
            elif word[i].upper() in dictRu[2]:
                count += 2
            elif word[i].upper() in dictRu[3]:
                count += 3
            elif word[i].upper() in dictRu[4]:
                count += 4
            elif word[i].upper() in dictRu[5]:
                count += 5
            elif word[i].upper() in dictRu[8]:
                count += 8
            elif word[i].upper() in dictRu[10]:
                count += 10
    elif lang == 'en':
        for i in range(len(word)):
            if word[i].upper() in dictEn[1]:
                count += 1
            elif word[i].upper() in dictEn[2]:
                count += 2
            elif word[i].upper() in dictEn[3]:
                count += 3
            elif word[i].upper() in dictEn[4]:
                count += 4
            elif word[i].upper() in dictEn[5]:
                count += 5
            elif word[i].upper() in dictEn[8]:
                count += 8
            elif word[i].upper() in dictEn[10]:
                count += 10
    print(f"Введённое слово \"{word}\" стоит {count} тугриков.")
    break
if lang == '':
    print("Инопланетные языки распознавать ещё не умеем.\nСмените раскладку.")
