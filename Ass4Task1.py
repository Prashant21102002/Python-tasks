try:
    with open('sample.txt', 'r') as file1:
        for line in file1:
            print(line, end='')  # end='' to avoid double newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")