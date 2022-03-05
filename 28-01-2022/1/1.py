def file_read(file):
    with open(file) as f:
        a = f.readlines()
        print(a)
file_read("ex.txt")