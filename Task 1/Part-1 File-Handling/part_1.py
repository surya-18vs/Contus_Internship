f = open("Titanic-Dataset.csv", "r")

lines = f.readlines()

for line in lines[:6]:
    print(line.strip())

f.close()