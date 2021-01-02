#can read a file with the open function
# open returns a file object to you
# filevar.read() will automatically default to -1
# can read once only
# when readingfile, a cursor is used
# after file is read, cursor is at the end
#seek can move the cursor
# file.seek(0) moves cursor to the beginning
# file.readline() reads line by line
# file.readline() returns a list of al the lines
# close file using file.close() and can check to see if it has closed attribute
# file.closed returns True or False
# cannot read if file is closed 

# with open (name) as file:
#     file.read()
# file.closed

# equivalent to code:
# file = open(name)
# file.read()
# file.close()
# file.closed

#f.__exit__() closed the file, f.__enter__() can open it

#writing to files
# have to open the file first
# with open(hakiu,"w") as file:
#     file.write()
# r+ can write
# a,nw creates a new file
# w with a file that doesnt exist will automatically create one