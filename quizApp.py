from random import randint
import time

print("Please Enter Your Name:")
# error handling for username

while True:
    user_name = input(">>").title().strip()
    while user_name.isalpha() is not True or len(user_name) <= 2 or len(user_name) >= 16:
        print(f"Please Enter only Alphabets with no spaces\n"
              f"and Name must be more than 2 letters and less than 16 letters")
        user_name = input(">>").title().strip()

    while user_name.isalpha() is True and len(user_name) >= 3 and len(user_name) <= 15:
        # Question Sections
        print(f"Hello {user_name}, Welcome to the Lawson's Ultimate Quiz App\n"
              f"Here's the rule of the Game\n"
              f"One wrong answer is -5\n"
              f"One correct answer is 5\n"
              f"Winning the Ultimate golden price depends on getting every single question correctly\n"
              f"\n[1] Entertainment"
              f"\n[2] Polities"
              f"\n[3] Sport"
              f"\n[4] Beauty")
        break
    break

print(f"Please select one section from above to play from using their numbers")


# Error handling for picking questions
def userPickFunction():
    while True:
        try:
            global user_pick
            user_pick = int(input(">>"))
            if user_pick < 1 or user_pick > 4:
                print("Enter any number between 1 - 4")
                continue
            else:
                break
        except ValueError:
            print("Enter any number from the option above")
    return user_pick


Q_numbers = 1
score = 0


# For Questions with two Options only
def two_options():
    while True:
        try:
            global q1
            q1 = int(input(">>"))
            if q1 < 1 or q1 > 2:
                print("Please Enter from the options above (1 or 2)")
                continue
            else:
                break
        except ValueError:
            print("Please a numeric value")
    return q1


# For Questions with Four Options only
def four_options():
    while True:
        try:
            global quest1
            quest1 = int(input(">>"))
            if quest1 < 1 or quest1 > 4:
                print("Please Enter from the options above (1 or 4)")
                continue
            else:
                break
        except ValueError:
            print("Please a numeric value")
    return quest1


# Functions of containing the questions
def entertainment():
    print(f"There are 3 Questions in this Entertainment Section")

    def question1():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Davido is a Musician?\n"
              f"[1] True \n[2] False\n"
              f"=============================")

        q1 = two_options()

        global score
        if q1 == 1:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [1] True\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question2():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Who made this viral statement 'E Choke!' ?\n"
              f"[1] Portable \n[2] Davido\n"
              f"=============================")

        q2 = two_options()

        global score
        if q2 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] Davido\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question3():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Reekado Banks won the next rated Award in what year?\n"
              f"[1] 2021 \n[2] 2019\n[3] 2013 \n[4] 2015\n"
              f"=============================")
        q3 = four_options()

        global score
        if q3 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] 2015\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question4():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Who is the CEO/Owner of YBNL record Label? \n"
              f"[1] Ycee \n[2] Olamide\n[3] Davido \n[4] Dj Xclusive\n"
              f"=============================")
        q4 = four_options()

        global score
        if q4 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] Olamide\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question5():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Who was the first black person to win an Oscar for acting? \n"
              f"[1] Ini Edo \n[2] Yvonne Nelson \n[3] William Miles \n[4] Hattie McDonald\n"
              f"=============================")
        q5 = four_options()

        global score
        if q5 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] Hattie McDonald\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question6():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"How many James Bond films did Roger Moore star in? \n"
              f"[1] 7 \n[2] 8\n[3] 9 \n[4] 3\n"
              f"=============================")
        q6 = four_options()

        global score
        if q6 == 1:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [1] 7\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    rand_list = []
    for i in range(3):
        while True:
            random_number = randint(1, 6)
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
        elif random_number == 5:
            question5()
        else:
            question6()


def polities():
    print(f"There are 3 Questions in this Polities Section")

    def question1():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Goodluck Ebele Jonathan Govern Lagos State?\n"
              f"[1] True \n[2] False\n"
              f"=============================")
        pol_q1 = two_options()

        global score
        if pol_q1 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] True\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question2():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Nigeria gained her independence what year?\n"
              f"[1] 1963 \n[2] 1960\n[3] 1950 \n[4] 1900\n"
              f"=============================")
        pol_q2 = four_options()

        global score
        if pol_q2 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] 1960\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question3():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What is the full meaning of LP?\n"
              f"[1] LAPO \n[2] Lagos Police\n[3] Labour Party \n[4] Lagos Party\n"
              f"=============================")
        pol_q3 = four_options()
        global score
        if pol_q3 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] Labour Party\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question4():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Who formed the first political party in Nigeria? \n"
              f"[1] Abacha \n[2] Obasanjo\n[3] Tinubu \n[4] Herbert Macaulay\n"
              f"=============================")
        pol_q4 = four_options()

        global score
        if pol_q4 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] Herbert Macaculay\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question5():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What was the name of the first political party in Nigeria? \n"
              f"[1] NNPC \n[2] APC \n[3] PDP \n[4] NNDP \n"
              f"=============================")
        pol_q5 = four_options()

        global score
        if pol_q5 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] NNDP\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1

    def question6():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What do the two horses represent on the Nigerian coat of arm? \n"
              f"[1] Peace \n[2] Strength\n[3] Dignity \n[4] So help me God\n"
              f"=============================")
        pol_q6 = four_options()

        global score
        if pol_q6 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] Dignity\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    rand_list = []
    for i in range(3):
        while True:
            random_number = randint(1, 6)
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
        elif random_number == 5:
            question5()
        else:
            question6()


def sport():
    print(f"There are 3 Questions in this Sport Section")

    def question1():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What sport is best known as the ‘king of sports’?\n"
              f"[1] Basketball \n[2] Golf\n[3] Soccer \n[4] Hockey\n"
              f"=============================")
        spo_q1 = four_options()

        global score
        if spo_q1 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] Soccer\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question2():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"The Olympics are held every how many years?\n"
              f"[1] 4 years \n[2] 2 years \n[3] 1 year \n[4] 3 years\n"
              f"=============================")
        spo_q2 = four_options()

        global score
        if spo_q2 == 1:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [1] 4 years\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question3():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What’s the national sport of Canada?\n"
              f"[1] America Soccer \n[2] Football\n[3] Lacrosse \n[4] Base Ball\n"
              f"=============================")
        spo_q3 = four_options()
        global score
        if spo_q3 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] Lacrosse\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question4():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What’s the diameter of a basketball hoop in inches?\n"
              f"[1] 23 inches \n[2] 14 inches \n[3] 10 inches \n[4] 18 inches\n"
              f"=============================")
        spo_q4 = four_options()

        global score
        if spo_q4 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] 18 inches\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question5():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Venus Williams has won more tennis grand slam titles than Serena Williams \n"
              f"[1] True \n[2] False \n"
              f"=============================")
        spo_q5 = two_options()

        global score
        if spo_q5 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] False\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question6():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"How many holes are played in an average round of golf? \n"
              f"[1] 18 \n[2] 19 \n[3] 20 \n[4] 21\n"
              f"=============================")
        spo_q6 = four_options()

        global score
        if spo_q6 == 1:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [1] 18\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    rand_list = []
    for i in range(3):
        while True:
            random_number = randint(1, 6)
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
        elif random_number == 5:
            question5()
        else:
            question6()


def beauty():
    print(f"There are 3 Questions in this Beauty Section")

    def question1():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What is the process of removing dead skin cells from the body called?\n"
              f"[1] remover \n[2] Exfoliation\n[3] Eclipse \n[4] sorcery \n"
              f"=============================")
        bea_q1 = four_options()

        global score
        if bea_q1 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] Exfoliation\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question2():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What is the clear gel extracted from aloe vera leaves used for medically?\n"
              f"[1] For clearer Eyes vision \n[2] Grow longer Hair \n[3] Cure level 1 cancer \n[4] Treating Burns\n"
              f"=============================")
        bea_q2 = four_options()

        global score
        if bea_q2 == 4:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [4] Treating Burns\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1

    def question3():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What is a hairstyle with two ponytails, one on each side of the head, called?\n"
              f"[1] Two ponies\n[2] Pigtails \n"
              f"=============================")
        bea_q3 = two_options()
        global score
        if bea_q3 == 2:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [2] Pigtails\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question4():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What body part is reshaped in plastic surgery known as 'rhinoplasty'?\n"
              f"[1] Nose \n[2] Ear \n[3] Stomach \n[4] Mouth\n"
              f"=============================")
        bea_q4 = four_options()

        global score
        if bea_q4 == 1:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [1] Nose\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question5():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"What beauty gadget is used to pluck stray eyebrow hairs?\n"
              f"[1] pluck \n[2] Eyelid \n[3] Tweezers \n[2] dryer \n"
              f"=============================")
        bea_q5 = four_options()

        global score
        if bea_q5 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] Tweezers \n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    def question6():
        global Q_numbers
        print(f"Question {Q_numbers}\n"
              f"=============================\n"
              f"Where did yoga originate? \n"
              f"[1] Spain \n[2] China \n[3] India \n[4] France\n"
              f"=============================")
        bea_q6 = four_options()

        global score
        if bea_q6 == 3:
            score += 5
            print(f"========================\n"
                  f"CORRECT\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        else:
            score -= 5
            print(f"========================\n"
                  f"WRONG\n"
                  f"The Answer is [3] India\n"
                  f"Your Current Score is {score}\n"
                  f"========================\n")
        Q_numbers += 1
        time.sleep(1)

    rand_list = []
    for i in range(3):
        while True:
            random_number = randint(1, 6)
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
        elif random_number == 5:
            question5()
        else:
            question6()


# Questions to ask when user pick
def question():
    if user_pick == 1:
        entertainment()
        # user_pick_list.append(user_pick)
    elif user_pick == 2:
        polities()
    elif user_pick == 3:
        sport()
    else:
        beauty()


user_pick_list = []
user_pick = userPickFunction()

if score == 0:
    print("Level 1! score 5 or more")
    while True:
        if user_pick not in user_pick_list:
            user_pick_list.append(user_pick)
            break
        else:
            print("Enter Another Option that you haven't played yet")
            userPickFunction()
            continue
    question()

if score >= 5:
    print(f"Congratulation! You are now in Level 2"
          f"\n[1] Entertainment"
          f"\n[2] Polities"
          f"\n[3] Sport"
          f"\n[4] Beauty")
    while True:
        userPickFunction()
        if user_pick not in user_pick_list:
            user_pick_list.append(user_pick)
            break
        else:
            print("Enter Another Option that you haven't played yet")
            continue
    question()
else:
    print("Game Over! Try Again")
    print("You need to have atleast 5 score to get to Level 2")
    quit()
if score >= 15:
    print(f"Congratulation! You are now in Level 3"
          f"\n[1] Entertainment"
          f"\n[2] Polities"
          f"\n[3] Sport"
          f"\n[4] Beauty")
    while True:
        userPickFunction()
        if user_pick not in user_pick_list:
            user_pick_list.append(user_pick)
            break
        else:
            print("Enter Another Option that you haven't played yet")
            continue
    question()
else:
    print("Game Over! Try Again")
    print("You need to have atleast 15 score to get to Level 3")
    quit()
if score >= 30:
    print(f"Congratulation! You are now in Level 4"
          f"\n[1] Entertainment"
          f"\n[2] Polities"
          f"\n[3] Sport"
          f"\n[4] Beauty")
    while True:
        userPickFunction()
        if user_pick not in user_pick_list:
            user_pick_list.append(user_pick)
            break
        else:
            print("Enter Another Option that you haven't played yet")
            continue
    question()
else:
    print("Game Over! Try Again")
    print("You need to have atleast 30 to get to Level 5")
    quit()
# if score >= 45:
#     print(f"Congratulation! You are now in Level 5"
#           f"\n[1] Entertainment"
#           f"\n[2] Polities"
#           f"\n[3] Sport"
#           f"\n[4] Beauty")
#     while True:
#         userPickFunction()
#         if user_pick not in user_pick_list:
#             user_pick_list.append(user_pick)
#             break
#         else:
#             print("Enter Another Option that you haven't played yet")
#             continue
#     question()
# else:
#     print("Game Over! Try Again")
#     print("You need to have 45 score to Win the Golden price")
#     quit()
if score >= 60:
    print("Congratulations! you won the ultimate price")
else:
    print(f"You lost the ultimate price\n"
          f"you got to the last stage but You can do better!")
