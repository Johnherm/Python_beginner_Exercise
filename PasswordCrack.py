import random, pyautogui 
char = "1234567890abcdefghijklmnopqrstutvwxz"
char_list = list(char)
password = pyautogui.password("Enter your password")
guess_password = ''
while (guess_password!=password):
    guess_password = random.choices(char_list, k= len(password))
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{6{6{6{6{6{6{680}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}"+str(guess_password)+"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
    if (guess_password == list(password)):
        print("Your Cracked Password is : "+"".join(guess_password))
        break