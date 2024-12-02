import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)   

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You Lose"
    elif u_score == 0:
        return "You Win"
    elif u_score > 21:
        return "You Lose"
    elif c_score > 21:
        return "You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"


user_cards=[]
computer_cards=[]
is_game_over = False
computer_score = -1
user_score = -1

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())




while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your Cards: {user_cards} and Your Score: {user_score}")
    print(f"Computer Cards {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_input = input("Press Yes to Continue and No to Discontinue \n")
        if user_input == "Yes":
            user_cards.append(deal_card())
        else:
            is_game_over = True    
        
while computer_score != 0 and computer_score < 17:
     computer_cards.append(deal_card())
     computer_score = calculate_score(computer_cards)
     
print(compare(user_score , computer_score))     