from random import *

file = open("Bottom 100 Movies.txt", "r")
lines = file.readlines()
file.close()

numberOfMovies = sum(1 for line in open('Bottom 100 Movies.txt'))
movieToWatch = randint(0, numberOfMovies - 1)
print(lines[movieToWatch])

file = open("Bottom 100 Movies.txt", "w")
for line in lines:
    if line != lines[movieToWatch]:
        file.write(line)
file.close()
