def words_longer_than_n(word_list, n):
    return [word for word in word_list if len(word) > n]

sample_words = ["apple", "banana", "kiwi", "orange", "grape"]
n = 5
result = words_longer_than_n(sample_words, n)
print("Words longer than", n, "characters:", result)
