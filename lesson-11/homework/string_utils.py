def reverse_string(text):
    return text[::-1]

print(reverse_string('HelloUzbekistan'))


def vowel_count(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example usage
print("Vowel count:", vowel_count("HelloUzbekistan"))
                   