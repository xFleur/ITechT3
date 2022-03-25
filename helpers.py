import nltk

# Check if the answer is a yes.
def answer_is_yes(answer):
    lowercase_answer = answer.lower()
    if "yes" in lowercase_answer or "okay" in lowercase_answer or "sure" in lowercase_answer:
        return True
    else:
        return False


# Turns an array into a proper text list. example ["1", "2", "3"] => 1, 2 or 3
def array_to_sum_of_words(array_of_strings):
    return ", ".join(array_of_strings[:-2] + [" or ".join(array_of_strings[-2:])])


# Turns a string into tokens
def tokenize_string(string):
    tknzr = nltk.tokenize.TweetTokenizer()
    return tknzr.tokenize(string)


# Casts numbers in letters to actual numbers, like "seventeen" => 17
def text2int(textnum, numwords={}):
    if type(textnum) == "Int":
        return textnum
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            return None

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
