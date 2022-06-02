def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    ans_str = list(s)
    vowels = ["a", "e", "i", "o", "u"]
    vowel_indices = []
    for index in range(len(s)):
        if s[index].lower() in vowels:
            vowel_indices.append(index)
    for value in range(int(len(vowel_indices) / 2)):
        index1, index2 = vowel_indices[value], vowel_indices[-1-value]
        ans_str[index1], ans_str[index2] = ans_str[index2], ans_str[index1]
    return "".join(ans_str)
