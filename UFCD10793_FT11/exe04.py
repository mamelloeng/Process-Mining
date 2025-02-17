def n_vogais(s):
    """Counts the number of vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

