from random import *

file = open("Syfy Channel Movies.txt", "r")
lines = file.readlines()
file.close()

numberOfMovies = sum(1 for line in open('Syfy Channel Movies.txt'))
movieToWatch = randint(0, numberOfMovies - 1)
print(lines[movieToWatch])

file = open("Syfy Channel Movies.txt", "w")
for line in lines:
    if line != lines[movieToWatch]:
        file.write(line)
file.close()
