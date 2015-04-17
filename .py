import simplegui
import random

secret_words = ['aysin', 'martin', 'happy', 'music', 'programming', 'python', 'code',
               'dance', 'sandwich', 'travel', 'sweden', 'decision', 'apple', 'disclosure',
               'latch', 'mathematics', 'love', 'depression', 'fly', 'developer', 'journalist',
               'mind', 'magic', 'traffic', 'confuse', 'smile', 'perfect']
num_misses = 0 
the_guess = 0
valid_characters = "abcdefghijklmnopqrstuvwxyz"
user_guess = ""
the_progress =" "

#for hangman
head = "Black"
body = "Black"
left_arm = "Black"
right_arm = "Black"
left_leg = "Black"
right_leg = "Black"
left_palm = "Black"
right_palm = "Black"
left_foot = "Black"
right_foot = "Black"

#displaying lost/win message
you_won = "Black"
you_lost = "Black"
won_counter = 0
lost_counter = 0


def init():
    global num_misses
    num_misses = 0
    global user_guess
    user_guess = ""
    global head, body, left_arm, right_arm, left_leg
    global right_leg, left_palm, right_palm, left_foot
    global right_foot, you_won, you_lost, won_count, lost_count

    head = "Black"
    body = "Black"
    left_arm = "Black"
    right_arm = "Black"
    left_leg = "Black"
    right_leg = "Black"
    left_palm = "Black"
    right_palm = "Black"
    left_foot = "Black"
    right_foot = "Black"
    you_won = "Black"
    you_lost = "Black"
    won_counter = 0
    lost_counter = 0
    
    print "\n H*A*N*G*M*A*N  "
    print "You missed ", num_misses, " (6, you lose!)"
    
    global the_guess
    the_guess = random.randint(0, 25)
    print_progress()

#Showing progress made by user
def print_progress():
    global the_progress
    the_progress = " "
    
    for x in range(0,len(secret_words[the_guess])):
        if (user_guess.find(secret_words[the_guess][x]) >= 0):
            the_progress += " " + secret_words[the_guess][x] + " "
        else: 
            the_progress += " _ "
    print "Secret Word: ", the_progress

#Check if user won/not
def user_points():
    user_won = True
    for x in range(0, len(secret_words[the_guess])):
        if (user_guess.find(secret_words[the_guess][x]) < 0):
            user_won = False
    return user_won

#Function to draw hangman
def draw_hangman():
    if num_misses == 1:
        global head
        head = "Purple"
    elif num_misses == 2:
        global body
        body = "Purple"
    elif num_misses == 3:
        global left_arm
        left_arm = "Purple"
        global left_palm
        left_palm = "Green"
    elif num_misses == 4:
        global right_arm
        right_arm = "Purple"
        global right_palm
        right_palm = "Green"
    elif num_misses == 5:
        global left_leg
        left_leg = "Purple"
        global left_foot
        left_foot = "Green"
    else:
        global right_leg
        right_leg = "Purple"
        global right_foot
        right_foot = "Green"
        
def get_input(guess):
    textGuess.set_text("")
    
    global user_guess
    global num_misses
    
    guess = guess.lower()
    
    if len(guess) != 1:
        print "Enter a single letter!"
        return None
    elif valid_characters.find(guess) < 0:
        print "Please enter a valid letter (a-z)"
        return None
    elif user_guess.find(guess) >= 0:
        print "You already guessed " + guess + ". Please try something else!"
        return None
    else:
        user_guess += guess
        
    print "You Guessed: ", guess
    print "Number of misses: ", num_misses
    
    if secret_words[the_guess].find(guess) >= 0:
        print "Great!" , "\n"
        print_progress()
        print ""
    else:
        print "Sorry! Try again!", "\n"
        print_progress()
        
        #update number of misses and draw hangman
        num_misses += 1
        draw_hangman()
        
        if (num_misses >= 6 and not user_points()):
            print "Sorry, you lost!.\n The secret word was ", secret_words[the_guess]
            global lost_counter
            lost_counter = 5
            timerLost.start();
            return None
        
    if user_points():
        print "You Won! Congratulations!!"
        global won_counter
        won_counter = 80
        timerWon.start();
    
def draw(canvas):
    canvas.draw_text("  *H*A*N*G*M*A*N*  ", [70, 100], 48, "Blue")
    canvas.draw_text("Number of misses: "+ str(num_misses) + " (6, you lose)", [50,500], 36, "Blue")
    canvas.draw_text("Secret Word: " + the_progress, [50, 460], 36, "Red") 
    
    canvas.draw_line((300, 150), (300, 325), 2, "Yellow")
    canvas.draw_line((275, 325), (325, 325), 2, "Yellow")
    canvas.draw_line((300, 150), (350, 150), 2, "Yellow")
    canvas.draw_line((350, 150), (350, 170), 2, "Yellow")
    
    #Draw Hangman
    canvas.draw_circle((350,185), 16, 2, head)
    canvas.draw_line((350, 200), (350, 225), 2, body)
    canvas.draw_line((350, 200), (325, 225), 2, left_arm)
    canvas.draw_line((350, 200), (375, 225), 2, right_arm)
    canvas.draw_line((350, 250), (325, 280), 2, left_leg)
    canvas.draw_line((350, 250), (375, 280), 2, right_leg)
    canvas.draw_circle((325, 225), 4, 2, left_palm)
    canvas.draw_circle((375, 225), 4, 2, right_palm)
    canvas.draw_circle((325, 275), 4, 2, left_foot)
    canvas.draw_circle((375, 275), 4, 2, right_foot)
    
    canvas.draw_text("CONGRATS, YOU WON!", [70, 60], 48, you_won)
    canvas.draw_text("SORRY, YOU LOST!", [70, 550], 48, you_lost)
    
        
def show_you_won():
    global won_counter, you_won
    won_counter -= 1
    if you_won == "Black":
        you_won = "White"
    else:
        you_won = "Black"
        
    if won_counter <= 0:
        timerWon.stop()
        init() #new game starts
        
def show_you_lost():
    global lost_counter, you_lost
    lost_counter -=1
    if you_lost == "Black":
        you_lost = "White"
    else:
        you_lost = "Black"
     
    if lost_counter <= 0:
        timerLost.stop()
        init()
        
    
    
#draw the frame    
f = simplegui.create_frame("Hangman", 650, 650)
   
#register event handlers

textGuess = f.add_input("Guess a letter ", get_input, 200)
timerWon = simplegui.create_timer(100, show_you_won)
timerLost = simplegui.create_timer(1000, show_you_lost)
button = f.add_button("New Game", init)

f.set_draw_handler(draw)
f.start()
init()
    
    
    
    
