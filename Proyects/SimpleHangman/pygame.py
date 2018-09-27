import random
def print_scaffold(guesses, wd):
    if (guesses == 0):
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guesses == 1):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guesses == 2):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 3):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 4):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif (guesses == 5):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif (guesses == 6):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\nПетля затягується навколо шиї... ГРА ЗАВЕРШЕНА!")
        print("\nЗагадане слово: %s." %wd)
        again = input("Якщо бажаєте зіграти ще раз, натисніть 1, якщо ні, то натисніть будь що інше: ")
        again = again.lower()
        if again == "1":
            hangMan()
        return

def selectWord():
    file = open("words.txt","r")
    words = file.read()
    words= words.split(' ')
    myword = 'a'
    while len(myword) < 4 : # makes sure word is at least 4 letters long
        myword = random.choice(words)
        myword = myword.strip("\n")
        myword = myword.lower()
    return myword

def print_history():
    print("\nНатовп зібрався біля ешафоту і не може чекати на правосуддя. Суд відбувся і Вас засуджено!")
    print("Звісно, Ви не злочинець. Ні, ні. Ви просто опинились у невдалий час не в тому місці.")
    print("Ви напевно думаєте, що смерті не уникнути, але це не зовсім так.")
    print("Так, так. Ви отримали шанс на життя. Все, що вам потрібно зробити, ")
    print("це вгадати правильне слово, і ви зможите жити, щоб побачити новий день.")
    print("Але це ще не все. Якщо ви зробите 6 помилок, ВИ - ТРУП! УПЕРЕД!")
    print("Ось Ваше слово:")


def hangMan():
    guesses = 0	
    word = selectWord()
    word_list = list(word)	
    blanks = "_"*len(word)	
    blanks_list = list(blanks) 
    new_blanks_list = list(blanks)
    guess_list = []
    print_scaffold(guesses, word)
    print_history()
    print("" + ' '.join(blanks_list))
    while guesses < 6:
        guess = input("\nВгадайте букву:")
        guess = guess.lower()
        if len(guess) > 1:
            print("Припиніть, так не можна! Введіть лиш одну літеру.")
        elif guess == "":
            print("Ви не хочете грати? Введіть одну літеру.")
        elif guess in guess_list:
            print("Ви вже називали цю букву! Ось що ви набирали:")
            print(' '.join(guess_list))
        elif guess in "abcdefghijklmnopqrstuvwxyz":
            print("Ви набрали букву латиницею, перейдіть на український алфавіт!")
        elif guess not in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя":
            print("Набраний вами символ не є українською буквою! Будьте уважні!")
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i+1
            if new_blanks_list == blanks_list:                   
                print("О ні!!! Ви не вгадали.")
                guesses = guesses + 1
                print_scaffold(guesses, word)
                if guesses < 6:
                    print("Вгадуйте ще раз.")
                    print(' '.join(blanks_list))
            elif word_list != blanks_list:                      
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))                      
                if word_list == blanks_list:
                    print("\nВІТАЮ! Ви виграли.")
                    again = input("Якщо бажаєте зіграти ще раз, натисніть 1, якщо ні, то натисніть будь що інше: ")
                    if again == "1":
                        hangMan()
                    exit()
                else:
                    print("Ви вгадали!")
hangMan()



	







