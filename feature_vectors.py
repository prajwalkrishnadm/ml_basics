import string
import nltk


def word2features(sentence, index):
    word = sentence[index]

    features = {
        'word': word,
        'lowercase': word.lower(),
        'is_capitalized': word[0].isupper(),
        'is_all_caps': word.isupper(),
        'is_all_lower': word.islower(),
        'is_digit': word.isdigit(),
        'prefix-1': word[:1],
        'prefix-2': word[:2],
        'suffix-1': word[-1:],
        'suffix-2': word[-2:],
        'is_punctuation': word in string.punctuation
    }

    if index > 0:
        prev_word = sentence[index - 1]
        features.update({
            'prev_word': prev_word,
            'prev_is_capitalized': prev_word[0].isupper()
        })
    else:
        features['BOS'] = True  # Beginning of sentence

    if index < len(sentence) - 1:
        next_word = sentence[index + 1]
        features.update({
            'next_word': next_word,
            'next_is_capitalized': next_word[0].isupper()
        })
    else:
        features['EOS'] = True  # End of sentence

    return features


# import nltk
nltk.download('averaged_perceptron_tagger')

tokens = ["Prajwal", "Krishna", "visited", "Paris", "."]
pos_tags = nltk.pos_tag(tokens)

for word, tag in pos_tags:
    print(f"{word} → {tag}")

