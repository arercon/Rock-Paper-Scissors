import random

def com_choice(options):
    return options[random.randint(0,len(options)-1)]

def name_score():
    global score
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    ratings = open("rating.txt", "r")
    for line in ratings.readlines():
        test= line.rstrip("\n").split()
        if test[0] == name:
            score = int(test[1])
            break
        else:
            score = 0
    ratings.close()

def choose_mode():
    mode = input()
    if mode:
        mode = mode.split(",")
    else:
        mode = ["rock","paper","scissors"]
    return mode

def whobeatswho(choice):     #returns list with first half stronger
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    g = 'gun'
    l = 'lightning'
    d = 'devil'
    dr = 'dragon'
    w = 'water'
    a = 'air'
    sp = 'sponge'
    wo = 'wolf'
    t = 'tree'
    h = 'human'
    sn = 'snake'
    f = 'fire'


    if choice == r:
        return [g,l,d,dr,w,a,p,sp,wo,t,h,sn,s,f]
    elif choice == g:
        return [l,d,dr,w,a,p,sp,wo,t,h,sn,s,f,r]
    elif choice == l:
        return [d,dr,w,a,p,sp,wo,t,h,sn,s,f,r,g]
    elif choice == d:
        return [dr,w,a,p,sp,wo,t,h,sn,s,f,r,g,l]
    elif choice == dr:
        return [w,a,p,sp,wo,t,h,sn,s,f,r,g,l,d]
    elif choice == w:
        return [a,p,sp,wo,t,h,sn,s,f,r,g,l,d,dr]
    elif choice == a:
        return [w,p,sp,wo,t,h,sn,s,f,r,g,l,d,dr]
    elif choice == p:
        return [w,sp,wo,t,h,sn,s,f,r,g,l,d,dr,a]
    elif choice == sp:
        return [wo,t,h,sn,s,f,r,g,l,d,dr,w,a,p]
    elif choice == wo:
        return [t,h,sn,s,f,r,g,l,d,dr,w,a,p,sp]
    elif choice == t:
        return [h,sn,s,f,r,g,l,d,dr,w,a,p,sp,wo]
    elif choice == h:
        return [sn,s,f,r,g,l,d,dr,w,a,p,sp,wo,t]
    elif choice == sn:
        return [s,f,r,g,l,d,dr,w,a,p,sp,wo,t,h]
    elif choice == s:
        return [f,r,g,l,d,dr,w,a,p,sp,wo,t,h,sn]
    elif choice == f:
        return [r,g,l,d,dr,w,a,p,sp,wo,t,h,sn,s]

def rock_paper_scissors(options):
    c_choice = com_choice(options)
    u_choice = input().lower()
    if u_choice == '!exit':
        print("Bye!")
        return 0
    elif u_choice == '!rating':
        print(f"Your rating: {score}")
    elif u_choice == c_choice: # draw
        print_state('d', c_choice)
    elif u_choice in options:
        if c_choice in whobeatswho(u_choice)[7:]:
            print_state('w', c_choice)
        elif c_choice in whobeatswho(u_choice)[:7]:
            print_state('l', c_choice)
    else:
        print("Invalid input")

def print_state(state, choice):
    global score
    if state == 'd':
        print(f"There is a draw ({choice})")
        score += 50
    elif state == 'w':
        print(f"Well done. The computer chose {choice} and failed.")
        score += 100
    elif state == 'l':
        print(f"Sorry, but the computer chose {choice}")


play = 1 # Game is running
name_score()
options = choose_mode()
print("Okay, let's start")
while play != 0:
    play = rock_paper_scissors(options)
