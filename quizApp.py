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

if user_pick3