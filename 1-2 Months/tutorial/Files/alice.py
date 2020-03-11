def count_words(filename):
    """Used to count the approx number of words"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry we could not find the file: {filename}")
    else:
        #Count the approximate number of words in alice in wonderland
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} contained {num_words} words!")

filenames = ['alice.txt', 'moby_dick.txt', 'siddharta.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)