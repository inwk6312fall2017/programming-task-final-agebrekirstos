import string


def length_of_word(filename):
    """returns the length of the longest word in the file"""
    with open(filename,'r') as f:
        p = string.punctuation
        w = string.whitespace
        t1 = []
        for line in f:
            for word in line.split():
                word = word.strip(p + w)
                word = word.lower()
                t1.append(len(word))
        return max(t1)


def longest_word(filename):
    """returns the longest word in the file"""
    m = length_of_word(filename)
    with open (filename) as f:
        p = string.punctuation
        w = string.whitespace
        for line in f:
            for word in line.split():
                word = word.strip(p)
                word = word.lower()
                if len(word) ==m:
                    return word


print(longest_word("Book1.txt"))
print(longest_word("Book2.txt"))
print(longest_word("Book3.txt"))