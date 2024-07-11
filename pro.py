questions = [
    ["Which language was used to create Facebook?", "Python", "JavaScript", "PHP",
     "Ruby", "None", 1],
    ["What is your name?", "Python", "JavaScript", "PHP", "None", 1],
    ["What is your age?", "Python", "JavaScript", "PHP", "None", 1],
    ["What is your gender?", "Python", "JavaScript", "PHP", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
    ["What is your gender?", "python", "javascript", "php", "None", 1],
]

''' Question numbers '''

number = "first>second>third>fourth>fifth>sixth>seventh>eighth>ninth>tenth>eleventh>twelfth>thirteenth>fourteenth>fifteenth>sixteenth>seventeenth>eighteenth>nineteenth>twentieth>twenty-first>twenty-second>twenty-third>twenty-fourth>twenty-fifth"



q_number = number.split('>')
# print(number_list)


# print(len(questions))
levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

# while len(levels) < 25:
#     levels.append(levels[-1] * 2)


print("Welcome To My Game\n")

def welcome():
    global money
    try:
        for i in range(len(questions)):
            print(f"Your question for: Rs {levels[i]}\n")
            question = questions[i]
            print(f"Your {q_number[i]} Question is \"{question[0]}\" \n")
            print(f"Your options are: \n")
            print(f"{question[1]}   {question[2]}\n")
            print(f"{question[3]}   {question[4]}\n")
            reply = int(input("Would you like to answer [1-4]? or 0 to quit :\n"))


            while len(levels) < 25:
                levels.append(levels[-1] * 2)


            if reply == 0:
                print("you have quit the Game")
                money += levels[i]
                print(f"Your won is {money}")
                break

            if (reply == question[-1]):
                print(f"correct answer you have won {levels[i]}\n")
                print("---------------------------------------------")
                if i ==4:
                    money += levels[5]
                elif i ==9:
                    money += levels[9]

            else:
                print(f"Incorrect answer! You have lost Rs.{levels[i]}")
                break

    except ValueError as e:
        print("Something happend to your programme")

welcome()


print("Thank you for playing\n")

user = int(input("If you want to play again ptrss 100\n"))


def play():
    global user
    if user == 100:
        welcome()

    if user != 100:
        print("Have a nice day")
        break

play()