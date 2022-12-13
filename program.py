#Importing the system to clear the screen, as well as the waiting system
import os, time
load = "loading..."
#Variables for the login system
correct_username = "Cturland"
correct_password = "Big Bird"

#Booleen created for the login while loop
log_in = False
user_name = input("Enter Username: ")
user_password = input("Enter Password: ")
#makes the user wait 5 painful seconds for the program to start
print(load)
time.sleep(5)
#good scenario when the user is right
while log_in!= True:
    if user_name == correct_username and user_password == correct_password:
        print("Login successful ")
        log_in = True
        #else in case the long in is wrong
    else:
        print("User name or password is not correct")
        user_name = input("Enter Username: ")
        user_password = input("Enter Password: ")
#booleen created for another while loop
run = True
while run:
    #user choice system
    choice = int(input("------------------------------------\n" +
                   "1. Test Assessment\n" +
                   "2. MYP Assessment\n"+
                   "3. Quit\n"+
                   "-----------------------------------\n"+
                       ": "))
    while choice<1 or choice>3:
        choice = int(input("Chose the correct option(1-3): "))
        # choice 1 scenario
    if choice == 1:
        #system created to see in case the user enters a wrong number
        while True:
            try:
                print(load)
                time.sleep(5)
                #clears the screen
                os.system("clear")
                student_name = input(" Enter student name: ")
                max_score = int(input(" Enter maximum score of test: "))
                user_score = float(input(" Enter user score: "))
                #calculates the score
                percentage_score = (user_score/max_score)*100
                percentage_score = round(percentage_score,1)
                if percentage_score>=90:
                    print(student_name+"s", "score is an 8 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=80 and percentage_score<90:
                    print(student_name+"s", "score is a 7 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=70 and percentage_score<80:
                    print(student_name+"s", "score is a 6 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=60 and percentage_score<70:
                    print(student_name+"s", "score is a 5 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=50 and percentage_score<60:
                    print(student_name+"s", "score is a 4 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=40 and percentage_score<50:
                    print(student_name+"s", "score is a 3 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=30 and percentage_score<40:
                    print(student_name+"s", "score is a 2 and their percentage grade is", str(percentage_score) + "%")
                    break
                elif percentage_score>=0 and percentage_score<30:
                    print(student_name+"s", "score is a 1 and their percentage grade is", str(percentage_score) + "%")
                    break
                    #tells the user to enter an actual number
            except ValueError:
                print("Enter the number using numbers, not letters.")
    elif choice == 2:
        print(load)
        time.sleep(5)
        os.system("clear")
        student_name = input("Enter student name: ")
        points = 0
        dos = True
        for i in range(4):
            while dos:
                try:
                    myp_score = int(input("Enter strand: "))
                    if myp_score>8 or myp_score<1:
                        print("Enter a number grade between one and 8")
                    elif myp_score<=8 and myp_score >= 1:
                        points += myp_score
                        break

                except ValueError:
                    print("Enter using numbers, not letters")
        if points >= 24:
            dos = False
            print(student_name + "'s", "final MYP score is 7")
        elif points >= 19 and points < 24:
            dos = False
            print(student_name + "'s", "final MYP score is 6")
        elif points >= 15 and points < 19:
            dos = False
            print(student_name + "'s", "final MYP score is 5")
        elif points >= 10 and points < 15:
            dos = False
            print(student_name + "'s", "final MYP score is 4")
        elif points >= 6 and points < 10:
            dos = False
            print(student_name + "'s", "final MYP score is 3")
        elif points >= 1 and points < 6:
            dos = False
            print(student_name + "'s", "final MYP score is 2")
        elif points == 0:
            dos = False
            print(student_name + "'s", "final MYP score is 1")
    elif choice == 3:
        print(load)
        time.sleep(5)
        os.system("clear")
        print("Terminating program...")
        os.system("clear")
        quit()
