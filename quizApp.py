from random import randint

categories = ['Entertainment', 'Polities', 'Sport', 'Beauty', 'Lifestyle']
print("Please Enter Your Name:")
user_name = input(">>")
print(f"Hello {user_name.title()}, Welcome to the Ultimate Quiz App"
      f"\n[1] Entertainment"
      f"\n[2] Polities"
      f"\n[3] Sport"
      f"\n[4] Beauty"
      f"\n[5] Lifestyle")

print(f"Please select three options from above to play from using their numbers")
user_pick1 = int(input(">>"))
user_pick2 = int(input(">>"))
user_pick3 = int(input(">>"))
Q_numbers = 1

score = 0


def entertainment():
      print(f"There are 3 Questions in this Entertainment Session")
      def question1():
          print(f"Question1\n"
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
                      f"Your Currect Score is {score}\n"
                      f"========================\n")

      def question2():
          print(f"Question2\n"
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
                      f"Your Currect Score is {score}\n"
                      f"========================\n")
      for i in range(2):
            random_number = randint(1, 3)
            if random_number == 1:
                  question1()
            elif random_number == 2:
                  question2()
            # elif random_number == 3:
            #       question3()
            # elif random_number == 3:
            #       question4()
            # elif random_number == 3:
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