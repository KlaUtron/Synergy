word = input("Введите слово: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
all_vowels_present = True
for vowel in vowels:
    if vowel not in word:
        all_vowels_present = False
        break
if not all_vowels_present:
    print(False)
else:
    for char in word:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    print(f"Гласные: {vowel_count}")
    print(f"Согласные: {consonant_count}")