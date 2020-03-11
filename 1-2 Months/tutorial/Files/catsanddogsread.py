def read_files(filename):

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry we could not find the file: {filename}\n")
    else:
        lists = contents.split()
        for list in lists:
            print(list)


filename = ['cats.txt', 'dogs.txt']

for file in filename:
    read_files(file)
