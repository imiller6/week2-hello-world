# Ian Miller

print('Hello!')
print('What is your prefered language? \n A. English \n B. German \n C. Russian')
# the next line allows the user to input their prefered language
favL = input()
# here I used an if statement to print a greeting based on what the user inputs as their prefered lagnguage.
if favL == str('A'):
    print('Greetings')
elif favL == str('B'):
    print('Guten Tag')
else:
    print('Privetstvuyu')
quit()


