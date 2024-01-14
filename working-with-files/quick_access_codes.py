''' quick access codes '''

# changing the current working directory
import os
print(os.listdir()) # check which files are there in the cwd
dir1 = os.getcwd() # or print cwd
dir1 += '/working-with-files'
os.chdir(dir1)
dir1 = os.getcwd()

# (finding maximums in dictionary)
for _ in range(int(input())):
    N,K = map(int, input().split()) # split string code
    str2 = list(map(int, input().split())) # split string to list

    word_counter = {}

    disqulified_stud = []
    for item in str2:
        if item == str2.index(item)+1:
            disqulified_stud.append(item)
        word_counter[item] = word_counter.get(item, 0) + 1

    # find maximum in dict e.g. {'a':2, 'b':3, 'c':3} then ['b','c']
    maximum_keys = [key for key, value in word_counter.items() if (
        value >= K and key not in disqulified_stud)]

    print(len(maximum_keys))
