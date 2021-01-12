


def run():
    sentence = ""
    with open("data.txt", "r") as file:
        sentence = file.read().replace("\n", "")

    print(sentence)
    print("\n")

    print("There are "+str(len(sentence))+" characters")

    words = sentence.split(" ")

    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    
    print("There are "+str(len(words))+" words")

    print("\n")

    for word in words:
        print(word)
        print(str(len(word))+" characters")
        print(str(counts[word])+" repeated times")
        print("\n")

run()