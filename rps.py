print(".......Rock........")
print(".......Paper........")
print(".......Scissor.......")

player1 = input("Player 1 : ")
player2 = input("Player 2 : ")

round = int(input("How many rounds you wanna play? "))
print("Ohhk then! Let's Start")

def decide(n1,n2):
    if((n1=="Rock" or "rock")and(n2=="Paper" or "paper")):
        print(f"Shoot! Congrats {player2}! You win")
    elif((n2=="Rock" or "rock")and(n1=="Paper" or "paper")):
        print(f"Shoot! Congrats {player1}! You win")
    elif((n2=="Paper" or "paper")and(n1=="Scissor" or "scissor")):
        print(f"Shoot! Congrats {player1}! You win")
    elif((n2=="Scissor" or "scissor")and(n1=="Paper" or "paper")):
        print(f"Shoot! Congrats {player2}! You win")
    elif((n2=="Scissor" or "scissor")and(n1=="Rock" or "rock")):
        print(f"Shoot! Congrats {player1}! You win")
    elif((n1=="Scissor" or "scissor")and(n2=="Rock" or "rock")):
        print(f"Shoot! Congrats {player2}! You win")
    elif(n1==n2):
        print(f"You both entered the same")

for n in range(1,round+1):
    n1 = input(f"{player1}, it's your turn : ")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    n2 = input(f"{player2}, it's your turn now : ")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    print("****NO CHEATING****\n\n\n\n")
    decide(n1,n2)