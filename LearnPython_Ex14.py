from sys import argv

script,user_name=argv
prompt='>'

print ("\033[0;37;45m Hi, {},I'm the '{}' script.\033[0m".format(user_name,script))
print("\033[0;37;45m I'd like to ask you a few question.\033[0m")
print("\033[0;37;45m Do you like me {}?\033[0m".format(user_name))
likes=input(prompt)

print("\033[0;37;45m Where do you live {}？\033[0m".format(user_name))
lives=input(prompt)

print("\033[0;37;45m What kind of computer do you have?\033[0m")
computer=input(prompt)

print("""\033[0;37;45m 
Alright,so you said {} about liking me.
you live in {}.Not sure where that is.
And you have a {} computer.Nice.\033[0m
""".format(likes,lives,computer))