#nim.py
#Richard Parker
#CSCI 77800 Fall 2022
#collaborators: none
#consulted: none




stones = 12
stones_taken = 0
machine_turn =3

while stones > 0:
 
 stones_taken = input("How many stones do you want? ")
 stones_taken = int(stones_taken)
 
 if stones_taken < 1 or stones_taken > 3:
    stones_taken = input("Pick between 1 and 3: ")
 
 stones = stones - int(stones_taken)

 if stones == 0:
  print("Player wins")
  quit()

 print(str(stones) + " stones remaining")

 if stones >= 3:
  import random
  machine_turn = random.randint(1,3)
 elif stones == 2:
   machine_turn = 2
 else:
   machine_turn = 1

 print("The computer picks " + str(machine_turn) + " stones")

 stones = stones - machine_turn

 if stones == 0:
   print("Computer wins")
   quit()

 print(str(stones)+ " stones remaining")