import random
rpsdict={
    'r':-1,
    'p':0,
    's':1
}
compdict={
    -1:'r',
    0:'p',
    1:'s'
}
while True:
    computer=random.randint(-1,1)
    print("Press r for rock")
    print("Press p for paper") 
    print("Press s for scissor")   
    yourdict=input("Enter your choice : ")
    print(f"You chose {yourdict} & computer chose {compdict[computer]}")
    if yourdict not in rpsdict:
        print("Choose from the above option :   ")
        continue
    you=rpsdict[yourdict]
    print()
    if(computer==you):
        print("Its a tie,Play again")
    else:
        if(computer==-1 and you==0) or (computer==0 and you==1) or (computer==1 and you==-1):
            print("You won")
        else:
            print("You lose")
    ch=int(input(" Enter 1 for play again or 0 for quitting:   "))
    if(ch==0):
        break
    