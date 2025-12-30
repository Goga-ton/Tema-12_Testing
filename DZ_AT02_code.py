def count_vowels(text):
    vowels = 'aeiouyаеёиоуыэюя'
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    # print(count)
    return count


