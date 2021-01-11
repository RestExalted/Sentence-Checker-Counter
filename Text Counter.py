def run():
    #this is for asking the user to input the text
    sentence = input("Please enter a text:")

    print("\n")
    print(sentence)
    print("\n")

    print("There are "+str(len(sentence))+" characters")

    #we search for the words words first.
    words = sentence.split(" ")

    #we count the repeating words
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    print("There are "+str(len(words))+" words")

    print("\n")

    #we then attempt to observe the words
    for word in words:
        print(word+" ("+str(len(word))+" characters) (repeated "+str(counts[word])+" times)")

run()
