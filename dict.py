import string

def word_frequency(sentence):
    frequency_dict = {}
    words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

# Testing
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
