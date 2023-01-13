from random import randint

# categories = ['Entertainment', 'Polities', 'Sport', 'Beauty', 'Lifestyle']
print("Please Enter Your Name:")
# error handling for username
while True:
    user_name = input(">>").title().strip()
    while user_name.isalpha() is not True or len(user_name) <=2 or len(user_name) >= 16:
        print("Enter only Alphabets and Name must be more than 2 letters and less that 16 letters")
        user_name = input(">>").title().strip()

    while user_name.isalpha() is True and len(user_name) >=3 and len(user_name) <= 15:
        print(f"Hello {user_name}, Welcome to the Ultimate Quiz App"
              f"\n[1] Entertainment"
              f"\n[2] Polities"
              f"\n[3] Sport"
              f"\n[4] Beauty"
              f"\n[5] Lifestyle")
        break
    break

print(f"Please select three options from above to play from using their numbers")

# Error handling for picking questions
while True:
    try:
        user_pick1 = int(input(">>"))
        if user_pick1 < 1 or user_pick1 > 5:
            print("Enter any number between 1 - 5")
            continue
        else:
            break
    except ValueError:
        print("Enter any number from the option above")
# user_pick2 = int(input(">>"))
# user_pick3 = int(input(">>"))

Q_numbers = 1
score = 0


def entertainment():
      print(f"There are 3 Questions in this Entertainment Session")
      def question1():
          global Q_numbers
          print(f"Question {Q_numbers}\n"
                f"=============================\n"
                f"Davido is a Musician?\n"
                f"[A] True \n[B] False\n"
                f"=============================")
          q1 = input(">>").upper()

          global score
          if q1 == "A":
                score += 10
                print(f"========================\n"
                      f"CORRECT\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          else:
                print(f"========================\n"
                      f"WRONG\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          Q_numbers+=1
      def question2():
          global Q_numbers
          print(f"Question {Q_numbers}\n"
                f"=============================\n"
                f"Who made this viral statement 'E Choke!' ?\n"
                f"[A] Portable \n[B] Davido\n"
                f"=============================")
          q2 = input(">>").upper()

          global score
          if q2 == "B":
                score += 10
                print(f"========================\n"
                      f"CORRECT\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          else:
                print(f"========================\n"
                      f"WRONG\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          Q_numbers +=1

      def question3():
            global Q_numbers
            print(f"Question {Q_numbers}\n"
                  f"=============================\n"
                  f"Reekado Banks won the next rated Award in what year?\n"
                  f"[A] 2021 \n[B] 2019\n[C] 2013 \n[D] 2015\n"
                  f"=============================")
            q3 = input(">>").upper()
            global score
            if q3 == "D":
                score += 10
                print(f"========================\n"
                      f"CORRECT\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
            else:
                print(f"========================\n"
                      f"WRONG\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
            Q_numbers +=1
      def question4():
          global Q_numbers
          print(f"Question {Q_numbers}\n"
                f"=============================\n"
                f"Who is the CEO/Owner of YBNL record Label? \n"
                f"[A] Ycee \n[B] Olamide\n[C] Davido \n[D] Dj Xclusive\n"
                f"=============================")
          q4 = input(">>").upper()

          global score
          if q4 == "B":
                score += 10
                print(f"========================\n"
                      f"CORRECT\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          else:
                print(f"========================\n"
                      f"WRONG\n"
                      f"Your Current Score is {score}\n"
                      f"========================\n")
          Q_numbers += 1
      rand_list= []
      for i in range(3):
            while True:
                random_number = randint(1, 4)
                print(random_number)
                if random_number not in rand_list:
                    rand_list.append(random_number)
                    break
                else:
                    continue
            if random_number == 1:
                  question1()
            elif random_number == 2:
                  question2()
            elif random_number == 3:
                  question3()
            elif random_number == 4:
                  question4()
            # elif random_number == 5:
            #       question5()
            # else:
            #       question6()

# categoriesq = [entertainment(), 'Polities', 'Sport', 'Beauty', 'Lifestyle']
def polities():
    print(f"There are 3 Questions in this Entertainment Session")
    print(f"Question\n"
          f"=============================\n"
          f"Davido is a Musician?\n"
          f"[A] True \n[B] False"
          f"=============================\n")
    q1 = input(">>").upper()
    if q1 == "A":
        print("Correct")
        # score += 10
    else:
        print("Wrong")

def sport():
    print(f"There are 3 Questions in this Entertainment Session")
    print(f"Question\n"
          f"=============================\n"
          f"Davido is a Musician?\n"
          f"[A] True \n[B] False"
          f"=============================\n")
    q1 = input(">>").upper()
    if q1 == "A":
        print("Correct")
        # score += 10
    else:
        print("Wrong")


def beauty():
    print(f"There are 3 Questions in this Entertainment Session")
    print(f"Question\n"
          f"=============================\n"
          f"Davido is a Musician?\n"
          f"[A] True \n[B] False"
          f"=============================\n")
    q1 = input(">>").upper()
    if q1 == "A":
        print("Correct")
        # score += 10
    else:
        print("Wrong")

def lifestyle():
    print(f"There are 3 Questions in this Entertainment Session")
    print(f"Question\n"
          f"=============================\n"
          f"Davido is a Musician?\n"
          f"[A] True \n[B] False"
          f"=============================\n")
    q1 = input(">>").upper()
    if q1 == "A":
        print("Correct")
        # score += 10
    else:
        print("Wrong")


if user_pick1 == 1:
      entertainment()
elif user_pick1 == 2:
      polities()
elif user_pick1 == 3:
      sport()
elif user_pick1 == 4:
      beauty()
elif user_pick1 == 5:
      lifestyle()


if user_pick2 == 1:
      entertainment()
elif user_pick2 == 2:
      polities()
elif user_pick2 == 3:
      sport()
elif user_pick2 == 4:
      beauty()
elif user_pick2 == 5:
      lifestyle()

if user_pick3 == 1:
      entertainment()
elif user_pick3 == 2:
      polities()
elif user_pick3 == 3:
      sport()
elif user_pick3 == 4:
      beauty()
elif user_pick3 == 5:
      lifestyle()