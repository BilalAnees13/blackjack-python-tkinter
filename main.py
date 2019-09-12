import tkinter as tk
import random


def load_card_images(card_images):
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    face_cards = ['jack', 'queen', 'king', 'ace']
    extension = 'png'
    
    # for each suit fetch the image and save the image in the list
    # the list of cards is a LIST OF TUPLES
    # the 0th index of tuple will have card name
    # the 1th index of tuple will have card image
    for suit in suits:
        for card in range(2,11):
            name = 'cards\{}_of_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((card, image,))
            
        for card in face_cards:
            name = 'cards\{}_of_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    tk.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def deal_card_to_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_var.set(dealer_score)
    
    player_score = score_hand(player_hand)
    
    if dealer_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")
#def deal_card_to_player():
#    global player_score
#    global player_ace
#    global player_score_var
#    card_value = deal_card(player_card_frame)[0]
#    # because this method returns the popped element of list
#    # and the popped element of the list is a tuple
#    
#    if card_value == 1 and not player_ace:
#        player_ace = True
#        card_value = 11
#    player_score += card_value
##    if player is busted check is there is an ace and subtract score
#    if player_score > 21 and player_ace:
#        player_score -= 10
#        player_ace = False
#    player_score_var.set(player_score)
#    if player_score > 21:
#        result_text.set("Dealer wins!")


def deal_card_to_player():
#    global player_score
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_var.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")
    
    
def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score
    
  
def reset_game():
    global dealer_card_frame
    global player_card_frame
    global player_hand
    global dealer_hand
    
    player_hand.clear()
    dealer_hand.clear()
    random.shuffle(deck)
    
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    
    dealer_card_frame = tk.Frame(card_frame, relief=tk.SUNKEN, border=1,
                      background=main_window_bg_color)
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame = tk.Frame(card_frame, relief=tk.SUNKEN, border=1,
                          background=main_window_bg_color)
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    deal_card_to_player()
    #deal_card_to_dealer()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_var.set(score_hand(dealer_hand))
    deal_card_to_player()
    
    
    
main_window = tk.Tk()
main_window_title = "Blackjack"
main_window_height = 640
main_window_width = 480
main_window_bg_color = "green" # background color
main_window_fg_color = "white" # foreground color
main_window.configure(background=main_window_bg_color)
main_window.title(main_window_title)
main_window.geometry("%dx%d" %(main_window_height, main_window_width))

result_text = tk.StringVar()
result = tk.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(main_window, relief=tk.SUNKEN, border=1,
                      background=main_window_bg_color)
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

#dealer_score_var = tk.IntVar()
#dealer_score = tk.Label(card_frame, text)
dealer_score_var = tk.IntVar()
#dealer_score_var.set(0)
tk.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tk.Label(card_frame, textvariable=dealer_score_var, background='green', fg='white').grid(row=1, column=0)

dealer_card_frame = tk.Frame(card_frame, relief=tk.SUNKEN, border=1,
                      background=main_window_bg_color)
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

#player_score = 0
player_score_var = tk.IntVar()
#player_score_var.set(player_score)
player_ace = False
tk.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_var, background='green', fg='white').grid(row=3, column=0)

player_card_frame = tk.Frame(card_frame, relief=tk.SUNKEN, border=1,
                      background=main_window_bg_color)
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tk.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tk.Button(button_frame, text="Dealer", command=deal_card_to_dealer)
dealer_button.grid(row=0, column=0)
player_button = tk.Button(button_frame, text="Player", command=deal_card_to_player)
player_button.grid(row=0, column=1)
reset_button = tk.Button(button_frame, text="Reset", command=reset_game)
reset_button.grid(row=0, column=2)

cards = []
load_card_images(cards)
#print(cards)

deck = list(cards)
random.shuffle(deck)

player_hand = []
dealer_hand = []

deal_card_to_player()
#deal_card_to_dealer()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_var.set(score_hand(dealer_hand))
deal_card_to_player()
#print(dealer_card_frame.children)
#print(player_card_frame.children)

main_window.mainloop()
