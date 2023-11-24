'''poem.txt contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in your python program and find out words with maximum occurance.'''

with open('poem.txt','r', encoding="utf-8") as file:
    word_counter = {}
    # reading each line
    for line in file:

        # reading each word
        for word in line.split():
            word_counter[word] = word_counter.get(word, 0) + 1
            # displaying the words
            # print(word)
    print(word_counter)

    #find maximum value in dictionary
    maximum_value = max(word_counter.values())

    #get keys with maximum value using list comprehension
    maximum_keys = [key for key, value in word_counter.items() if value==maximum_value]

    #print the maximum keys
    print(maximum_keys)
