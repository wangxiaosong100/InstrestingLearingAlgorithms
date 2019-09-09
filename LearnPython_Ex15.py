from sys import argv
script,filename=argv
txt=open(filename)
print("Here's your file {}:".format(filename))
print("\033[0;35;47m "+txt.read()+"\033[0m")

print("Type the filename again:")
file_again=input('>')
txt_again=open(file_again)
print("\033[0;35;47m "+txt_again.read()+"\033[0m")