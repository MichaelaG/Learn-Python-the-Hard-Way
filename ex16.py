# Exercise 16

# List of commands that are important for dealing with files:
# close() - closes the file
# read() - reads the content of the file
# readline() - reads only one of the lines of the file
# truncate() - empties the file
# write('stuff') - creates a file with 'stuff'

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line1: ")
line3 = raw_input("line1: ")

print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
