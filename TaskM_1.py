s = input().split()
with open("DataFile.txt", "w") as file:
    for line in s:
        file.write(line + "\n")