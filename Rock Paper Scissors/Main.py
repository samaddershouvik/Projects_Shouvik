import random

u,c=0,0
op=['r','p','s']

while True:
    ui=input("Enter Rock(r), Paper(p), Scissors(s), or Quit(q): ").lower()
    if ui=='q':
        break
    if ui not in op:
        continue
    comp=op[random.randint(0,2)]
    if ui=='r' and comp=='s':
        print("Comp= ",comp,"\nYou won!")
        u+=1
    elif ui=='p' and comp=='r':
        print("Comp= ",comp,"\nYou won!")
        u+=1
    elif ui=='s' and comp=='p':
        print("Comp= ",comp,"\nYou won!")
        u+=1
    elif comp==ui:
        print("Comp= ",comp,"\nGo again!!")
    else:
        print("Comp= ",comp,"\nYou Lost!")
        c+=1  
if(c==u):
    print("Draw")
elif(c<u):
    print("User Won")
else:
    print("Computer won")