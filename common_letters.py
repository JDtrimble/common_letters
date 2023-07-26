import time

def common_letters_function(words):
    if not words:
        return ""

    common = set(words[0])
    for word in words[1:]:
        common.intersection_update(set(word))

    return "".join(sorted(common))

if __name__ == "__main__":
    words = []
    while True:
        try:
            word = input()
            words.append(word)
        except EOFError:
            break
    # words = ['apple', 'peach']
    result = common_letters_function(words)
    print(result)
