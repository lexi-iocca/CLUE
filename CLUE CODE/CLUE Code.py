"""
FINAL PROJECT
CLUE: Murder at Mystery Mansion
CLUE Code.py
Demonstrates classes, lists, sound, easygui,
pygame, sprites, files and randomization
Lexi Iocca and Emily Gwin
Date: June 14, 2019
ICS4U - Computer Science
Mr. Mcclinchey
"""

from random import shuffle

# I - Import and initialize
import easygui
import pygame
import random
import time
from pygame.locals import *

pygame.init()  # allows sound to be added
pygame.mixer.init()
clock = pygame.time.Clock()

# import sounds
backtrack = pygame.mixer.Sound("backtrack.ogg")
scream = pygame.mixer.Sound("scream.ogg")
phone = pygame.mixer.Sound("phone.ogg")
candleSound = pygame.mixer.Sound("candleSound.ogg")
wrenchSound = pygame.mixer.Sound("wrenchSound.ogg")
gunSound = pygame.mixer.Sound("gunSound.ogg")
pipeSound = pygame.mixer.Sound("pipeSound.ogg")
knifeSound = pygame.mixer.Sound("knifeSound.ogg")
ropeSound = pygame.mixer.Sound("ropeSound.ogg")

#####################

# for button with picture
class Button(pygame.sprite.Sprite):
    def __init__(self, posx=320, posy=240, image="Ballroom.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.mouse = pygame.mouse.get_pos()

    def update(self):
        pass
        '''create an image based on the font and text'''
        """self.image = self.font.render(self.text, 1, (0,0,0), self.background)
        self.rect = self.image.get_rect()       #set the rectangle to be the size of the image.
        self.rect.center = self.center          #position the button
        self.mouse = pygame.mouse.get_pos()
        self.check_hover()            #check if mouse is hovering
        self.color()                            #change color of background of label"""

    def check_hover(self):
        '''adjust is_hover value based on mouse over button - to change hover color'''
        if self.rect.collidepoint(self.mouse):
            self.is_hover = True
        else:
            self.is_hover = False

    def color(self):
        '''change color when hovering'''
        if self.is_hover == True:
            self.background = (255, 0, 0)
        else:
            self.background = (212, 170, 255)

    def click(self):
        self.mouse = pygame.mouse.get_pos()
        '''return true or false based on mouse over the button '''
        # print (self.mouse())
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False


class ButtonWords(pygame.sprite.Sprite):
    def __init__(self, text="", posx=320, posy=240, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((color))
        self.font = pygame.font.SysFont("Courier", 25)
        self.text = text
        self.center = (posx, posy)
        self.background = (0, 0, 0)
        self.mouse = pygame.mouse.get_pos()

    def update(self):
        '''create an image based on the font and text'''
        self.image = self.font.render(self.text, 1, (0, 0, 0), self.background)
        self.rect = self.image.get_rect()  # set the rectangle to be the size of the image.
        self.rect.center = self.center  # position the button
        self.mouse = pygame.mouse.get_pos()
        self.check_hover()  # check if mouse is hovering
        self.color()  # change color of background of label

    def check_hover(self):
        '''adjust is_hover value based on mouse over button - to change hover color'''
        if self.rect.collidepoint(self.mouse):
            self.is_hover = True
        else:
            self.is_hover = False

    def color(self):
        '''change color when hovering'''
        if self.is_hover == True:
            self.background = (202, 247, 244)
        else:
            self.background = (255, 255, 255)

    def click(self):
        '''return true or false based on mouse over the button '''
        if self.rect.collidepoint(self.mouse):
            return True
        else:
            return False


class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Courier", 20)
        self.text = ""
        self.center = (500, 200)
        self.colour = (0, 0, 0)
        self.backcolour = (175, 255, 193)

    def update(self):
        self.image = self.font.render(self.text, 1, self.colour, self.backcolour)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class Label2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Courier", 20)
        self.text = ""
        self.center = (500, 200)
        self.colour = (0, 0, 0)
        self.backcolour = (255, 255, 255)

    def update(self):
        self.image = self.font.render(self.text, 1, self.colour, self.backcolour)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class scoreLabel(pygame.sprite.Sprite):

    def __init__(self, text1="", posx=0, posy=0):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Courier", 20)
        self.text = text1
        self.center = (posx, posy)
        self.colour = (0, 0, 0)
        self.backcolour = (247, 252, 250)

    def update(self):
        self.image = self.font.render(self.text, 1, self.colour, self.backcolour)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class CornerLogo(pygame.sprite.Sprite):  # detective lab
    def __init__(self, x=980, y=600, image="smallLogo.jpg"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class MagGlass(pygame.sprite.Sprite):  # for the mouse image
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mouse.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Xmark(pygame.sprite.Sprite):  # for the notepad xs
    def __init__(self, x=0, y=0, typeNum=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("x.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.type = typeNum

    def draw(self, screen):
        screen.blit(self.image, self.rect)


map = ["Ballroom",
       "Lounge",
       "Billiard Room",
       "Hall",
       "Kitchen",
       "Dining Room",
       "Conservatory",
       "Study",
       "Library"]

weapons = ["Lead Pipe",
           "Candlestick",
           "Revolver",
           "Rope",
           "Knife",
           "Wrench"]

victims = ["Roxy 'Big D' Warrenson",  # retired broadway starlet
           "Elton Whitehall",  # londons top criminal lawyer
           "'Bitsy' Elizabeth Debrevski Keyes",  # trust fund baby - thrice married
           "Millicent Friendly",  # spinster librarian - won lottery
           "Count Francois du Bennet",  # charming diplomat
           "Baron Deitrick bon Overlitzer"]  # shrewd businessman

suspects = ["Ms. Scarlett",
            "Mrs. White",
            "Mrs. Peacock",
            "Prof. Plum",
            "Mr. Green",
            "Colonel Mustard"]

evidence = ["Lead Pipe",  # includes everything except for the 3 envelope items
            "Candlestick",
            "Revolver",
            "Rope",  # weapons
            "Knife",
            "Wrench",

            "Ballroom",
            "Lounge",
            "Billiard Room",
            "Hall",
            "Kitchen",  # rooms
            "Dining Room",
            "Conservatory",
            "Study",
            "Library",

            "Ms. Scarlett",
            "Mrs. White",
            "Mrs. Peacock",
            "Prof. Plum",  # suspects
            "Mr. Green",
            "Colonel Mustard"]  # everything except the envelope

envelope = []  # victim, suspect, weapon, location
wrongGuess = []  # the things they guess incorrectly in each turn of the game (cleared after each turn)
crossedOff = []  # the clues they are given (things not in the envelope) - so they can get crossed off the notepad
guess = []  # the suspect, weapon and location guessed on each turn are added into this list for later (to check)
accusation = []  # for the final guess
correctGuess = []  # the things they get correct in the final accusation
guessNum = 0  # number of turns they get before accusation (can use less if they want)
labTries = 0  # number of turns they get to play the matching game
miniPlay = 0  # number of times the mini game has been played
turnCount = 0  # number of turns they take before making an accusation

ready = False  # once ready = True, it is time for the final accusation
pause = False  # used for if they are accessing certain things through the pause menu or not
play2 = False  # used for if they hit "play again"
leaderCheck = False
doneGame = False


def chooseLevel():
    backtrack.play(-1)

    global labTries
    global guessNum

    screen = pygame.display.set_mode((500, 300))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Choose your Level")
    title.font = pygame.font.SysFont("Courier", 30)
    title.center = (250, 90)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    subtitle = Label()
    subtitle.text = ("Welcome to CLUE: Murder at Mystery Mansion")
    subtitle.font = pygame.font.SysFont("Courier", 19)
    subtitle.center = (250, 29)
    subtitle.colour = (0, 0, 0)
    subtitle.backcolour = (221, 246, 255)

    easy = ButtonWords("Easy", 128, 150)
    medium = ButtonWords("Medium", 128, 195)
    hard = ButtonWords("Hard", 128, 240)

    explain = Label()
    explain.text = "20 turns + 3 mini game attempts"
    explain.font = pygame.font.SysFont("Courier", 15)
    explain.center = (320, 150)
    explain.colour = (0, 0, 0)
    explain.backcolour = (221, 246, 255)

    explain2 = Label()
    explain2.text = "15 turns + 2 mini game attempts"
    explain2.font = pygame.font.SysFont("Courier", 15)
    explain2.center = (320, 195)
    explain2.colour = (0, 0, 0)
    explain2.backcolour = (221, 246, 255)

    explain3 = Label()
    explain3.text = "10 turns + 1 mini game attempt"
    explain3.font = pygame.font.SysFont("Courier", 15)
    explain3.center = (320, 240)
    explain3.colour = (0, 0, 0)
    explain3.backcolour = (221, 246, 255)

    levelText = pygame.sprite.Group(title, easy, medium, hard, subtitle, explain, explain2, explain3)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy.click():  # this is where we set how many guesses and turns
                    guessNum = 20  # they get in the lab based on what level they choose
                    labTries = 3
                    mainMenu()

                elif medium.click():
                    guessNum = 15
                    labTries = 2
                    mainMenu()

                elif hard.click():
                    guessNum = 10
                    labTries = 1
                    mainMenu()

        levelText.clear(screen, background)
        levelText.update()
        levelText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def mainMenu():
    screen = pygame.display.set_mode((700, 480))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((220, 227, 239))
    screen.blit(background, (0, 0))

    logo = CornerLogo(350, 175, "Cluelogo.jpg")

    startBtn = ButtonWords("Start", 145, 385)
    instructBtn = ButtonWords("Instructions", 305, 385)
    leadBtn = ButtonWords("Leaderboard", 510, 385)

    mainText = pygame.sprite.Group(logo, startBtn, instructBtn, leadBtn)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startBtn.click() == True:
                    setup()
                elif instructBtn.click() == True:
                    instructions()
                elif leadBtn.click() == True:
                    leaderboard()

        mainText.clear(screen, background)
        mainText.update()
        mainText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def setup():
    global trueVic
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    # this is where we choose the 3 important facts that the player will have to figure out
    # the guilty suspect, the murder weapon and the room where the murder took place
    # they are randomized every game so you will never get the same outcome

    # random victim choice
    vicNum = random.randint(0, 5)
    trueVic = victims[vicNum]
    # print("the victim is:",trueVic)

    # random suspect choice
    suspectNum = random.randint(0, 5)
    trueSuspect = suspects[suspectNum]
    envelope.append(trueSuspect)
    evidence.remove(trueSuspect)  # the evidence list has everything in it EXCEPT for the guilty party

    # random weapon choice
    weaponNum = random.randint(0, 5)
    trueWeapon = weapons[weaponNum]
    envelope.append(trueWeapon)
    evidence.remove(trueWeapon)

    # random location choice
    shuffle(map)
    locationNum = random.randint(0, 8)
    trueLocation = map[locationNum]
    envelope.append(trueLocation)
    evidence.remove(trueLocation)

    print("Inside the envelope is:", envelope)  # the three things they need to figure out
    # print("Everything but envelope:", evidence)

    if not play2:  # if it is their first time playing, they get to hear the backstory
        introduction()

    elif play2:  # if they have played before, they can choose whether they want to hear the backstory again or not
        choice = easygui.buttonbox("Do you want to hear the backstory again?", "CLUE: Murder at Mystery Mansion",
                                   choices=('yes', 'no'))
        if choice == "yes":
            introduction()
        elif choice == "no":
            gameMap()


def instructions():
    global labTries, guessNum, pause

    guessNum = str(guessNum)
    labTries = str(labTries)

    screen = pygame.display.set_mode((1000, 820))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((225, 230, 239))
    screen.blit(background, (0, 0))

    notepad = pygame.image.load("notepad.png")

    title = Label2()
    line1 = Label2()
    line2 = Label2()
    line3 = Label2()
    line4 = Label2()
    line5 = Label2()
    line6 = Label2()
    line7 = Label2()
    line8 = Label2()
    line9 = Label2()
    line10 = Label2()
    line11 = Label2()
    line12 = Label2()
    line13 = Label2()
    line14 = Label2()
    line15 = Label2()
    line16 = Label2()
    line17 = Label2()
    line18 = Label2()

    continueGame = ButtonWords()

    title.text = "Instructions"
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (500, 100)
    title.backcolour = (202, 249, 249)

    line1.text = "The task is simple, really."
    line1.center = (200, 200)

    line2.text = ("You have " + guessNum + " turns to determine the correct, killer, weapon, and room. ")
    line2.center = (450, 250)

    line3.text = "The map on the screen is the floorplan to the house."
    line3.center = (343, 270)

    line4.text = "You, the detective, can enter any room and make a guess of what happened."
    line4.center = (460, 290)

    line5.text = "The guess will include a suspect, a weapon, and whatever room you are in."
    line5.center = (460, 310)

    line6.text = "As a group, the suspects will tell you one thing you have chosen incorrectly. "
    line6.center = (480, 330)

    line7.text = "Be careful, as the suspects might repeat themselves if you pick the same thing"
    line7.center = (480, 350)

    line8.text = "more than once!"
    line8.center = (100, 370)

    line9.text = "Once the suspects tell you the clue it will be crossed off in your notebook."
    line9.center = (480, 410)

    line10.text = "Check your notebook at any time by clicking the notebook button!"
    line10.center = (550, 460)

    line11.text = "When you think you've solved the case, click the 'Make Final Accusation' button."
    line11.center = (490, 550)

    line12.text = ("You can see how many turns you have left in the top right corner of the screen.")
    line12.center = (490, 590)

    line13.text = ("If you run out of turns, you will be forced to make your final guess!")
    line13.center = (450, 610)

    line14.text = ("If you need more turns, head to THE LAB to play the minigame!")
    line14.center = (460, 630)

    line15.text = ("You have " + labTries + " chance(s) to visit THE LAB to earn more turns.")
    line15.center = (470, 650)

    line17.text = "View the pause menu to see victim and suspect information"
    line17.center = (470, 700)

    line18.text = "or to view the instructions again"
    line18.center = (470, 720)

    line16.text = "Alright detective, are you ready to solve the case?"
    line16.center = (470, 755)
    line16.backcolour = (202, 249, 249)

    continueGame.text = "Continue"
    continueGame.center = (510, 790)

    labelGroup = pygame.sprite.Group(title, line1, line2, line3, line4, line5, line6, line7, line8,
                                     line9, line10, line11, line12, line13, line14, line15, line16,
                                     continueGame, line17, line18)

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause:
                    if continueGame.click():
                        pauseScreen()  # if they are viewing this from the pause menu, when they hit continue, they
                        # go back to the pause menu and can continue the game from there

                elif not pause:
                    if continueGame.click():
                        mainMenu()

        labelGroup.clear(screen, background)
        labelGroup.update()
        labelGroup.draw(screen)
        screen.blit(notepad, (20, 420))
        pygame.mouse.set_visible(True)
        pygame.display.flip()


def introduction():
    global trueVic

    global roxy, elton, bitsy, milli, count, baron

    # in the introduction of our game, you will hear the backstory corresponding to the victim that was randomly chosen

    roxy = "Roxy “Big D” Warrenson… Once America’s sweetheart, Roxy made it big through her work headlining multiple Broadway musicals. " \
           "Like any young starlet, Roxy’s younger years were full of scandalous romances and jet-set getaways. As she got older, the fame " \
           "and fortune got the better of young Roxy, and she started to dabble in drugs, alcohol, and of course, the slots. " \
           "Roxy had many enemies, like everyone does, but why would anyone want her dead? "

    elton = "Elton Whitehall … One of London’s brightest and most successful criminal lawyers, Whitehall was visiting on business when he was invited" \
            " to his old friend’s mansion for a get together. Recently, Whitehall has made a splash on newspaper headlines for" \
            " an alleged bribery accusation, which of course Whitehall has denied. Whitehall has made a fair few enemies through putting away Britain's" \
            " worst, but why would anyone want him dead?"

    bitsy = "Elizabeth Debrevski Keyes, better known as “Bitsy Keyes”... A dazzling young socialite, Bitsy’s daddy made it big in the oil industry," \
            " and ever since, Bitsy has been touring the world on her private jet with her many suitors. Three-times widowed at the ripe-age of" \
            " thirty-five, Bitsy’s husbands have a knack of simply disappearing. Many people believe that it is the work of her daddy and his hit men," \
            " but of course, Bitsy and her father deny any claims (Bitsy even releasing a book detailing her relationship with her father, entitled" \
            " Bitsy - My daddy, his money, and me). Bitsy has made herself quite a public target, but would anyone really want her dead? "

    milli = "Millicent Friendly… a seemingly innocent librarian who recently won big on the slots, earning herself a pretty little penny overnight." \
            " Millicent currently lives in a neighbouring mansion with her twenty five cats, and fleet of private jets and boats. They say people will" \
            " do anything for money, but was Millicent really murdered for it?"

    count = "Count Francois du Bennet … The charming French diplomat has graced international magazine covers for his work with underprivileged children" \
            " and the elderly, his scandalous love affairs, and his beach-ready physique. Bennet truly seems too good to be true - why would anyone want" \
            " him dead? "

    baron = "Baron Deitrick bon Overlitzer … Shrewd business man with a knack for stocks, Baron has brought in the big bucks by choosing good picks" \
            " for his wealthy and exclusive clientele. Sometimes it’s as if he knows where the stocks are going before it even happens. Baron has his" \
            " fair list of enemies, but why would anyone want his dead? "

    events = ["lunar eclipse", "meteor shower", "solar eclipse", "super moon", "blood moon", "hockey game",
              "fourth of July fireworks", "ball drop on New Year's Eve"]

    randomEvent = events[random.randint(0, 7)]

    randomSuspect = suspects[random.randint(0, 5)]

    easygui.msgbox(
        "Our story begins on a cold mid-winter night - you sit behind your desk absently scribbling on your notepad."
        " You are a world-class private detective, solving crime and tracking down killers in your town for the past"
        "twenty years. Recently, business has been slowing down and you find yourself waiting longer and longer "
        "between "
        " cases, hoping a new, juicy case will soon surface. You begin to doze off into a peaceful sleep …")

    easygui.msgbox("Meanwhile at the Mystery Mansion … ")

    # we have some randomization in the story so it isn't too repetitive if you play more than once
    # the suspect who is hosting the party and the event changes every time

    easygui.msgbox("It all started as a simple dinner party. " + randomSuspect + " invited"
                                                                                 "some of their closest friends over "
                                                                                 "to watch the " + randomEvent +
                   " at their family house, known around town as the strange and mystical Mystery Mansion. "
                   "Everything was going according to plan until the unthinkable occured!")

    scream.play()

    easygui.msgbox("MURDER!!!")

    easygui.msgbox("Here's the victim:")

    # they will get the background information of the unlucky victim that was chosen

    if trueVic == "Roxy 'Big D' Warrenson":
        easygui.msgbox(roxy, "ROXY 'BIG D' WARRENSON", image="roxy.gif")
    elif trueVic == "Elton Whitehall":
        easygui.msgbox(elton, "ELTON WHITEHALL", image="elton.gif")
    elif trueVic == "'Bitsy' Elizabeth Debrevski Keyes":
        easygui.msgbox(bitsy, "BITSY KEYES", image="bitsy.gif")
    elif trueVic == "Millicent Friendly":
        easygui.msgbox(milli, "MILLICENT FRIENDLY", image="milli.gif")
    elif trueVic == "Count Francois du Bennet":
        easygui.msgbox(count, "COUNT FRANCOIS", image="count.gif")
    elif trueVic == "Baron Deitrick bon Overlitzer":
        easygui.msgbox(baron, "BARON BON OVERLITZER", image="baron.gif")
    else:
        easygui.msgbox("something went wrong here :(")

    phone.play()
    easygui.msgbox("RIIIIINNNNNGGGGGGGGG")

    easygui.msgbox("You are awoken by the ringing of the telephone")

    easygui.msgbox("Although an unidentified innocent suspect had decided to call the police, all suspects have decided"
                   " to work together to cover for each other. Only you can find the truth!")

    easygui.msgbox("It's time to meet the suspects!")

    suspectPage()


def vicPage():
    # this page is for if they are viewing the victim information from the pause menu

    if trueVic == "Roxy 'Big D' Warrenson":
        easygui.msgbox(roxy, "ROXY 'BIG D' WARRENSON", image="roxy.gif")
    elif trueVic == "Elton Whitehall":
        easygui.msgbox(elton, "ELTON WHITEHALL", image="elton.gif")
    elif trueVic == "'Bitsy' Elizabeth Debrevski Keyes":
        easygui.msgbox(bitsy, "BITSY KEYES", image="bitsy.gif")
    elif trueVic == "Millicent Friendly":
        easygui.msgbox(milli, "MILLICENT FRIENDLY", image="milli.gif")
    elif trueVic == "Count Francois du Bennet":
        easygui.msgbox(count, "COUNT FRANCOIS", image="count.gif")
    elif trueVic == "Baron Deitrick bon Overlitzer":
        easygui.msgbox(baron, "BARON BON OVERLITZER", image="baron.gif")
    else:
        easygui.msgbox("something went wrong here :(")

    pauseScreen()


def suspectPage():
    global pause

    screen = pygame.display.set_mode((650, 725))
    pygame.display.set_caption("Meet the Suspects")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = "Meet the Suspects"
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (325, 40)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    sub = Label()
    sub.text = "click any card to view the backstory for that suspect"
    sub.font = pygame.font.SysFont("Courier", 12)
    sub.center = (325, 75)
    sub.colour = (0, 0, 0)
    sub.backcolour = (255, 255, 255)

    nextButton = ButtonWords("Continue", 325, 680)

    chooseScarlett = Button(120, 230, "MissScarlett.png")
    chooseWhite = Button(320, 230, "MrsWhite.png")
    choosePeacock = Button(515, 231, "MrsPeacock.png")
    choosePlum = Button(120, 520, "ProfPlum.png")
    chooseGreen = Button(320, 520, "MrGreen.png")
    chooseMustard = Button(515, 520, "ColonelMustard.png")

    suspectText = pygame.sprite.Group(title, sub, chooseScarlett, chooseWhite, choosePeacock,
                                      choosePlum, chooseGreen, chooseMustard, nextButton)

    scarlettText = "Ms. Scarlett is a vivacious and aspiring singer/songwriter with a passion for fame and fortune.  She" \
                   " is the daughter of Ms. Peacock, but the two have not been on speaking terms."

    whiteText = "Mrs. White is a long-time nurse who’s recently deceased husband was an award-winning brain surgeon."

    peacockText = "Notorious gold-digger, Mrs. Peacock is currently married to an extremely wealthy older foreign" \
                  " business man, to the dismay of her estranged daughter, Ms. Scarlett."

    plumText = "Intelligent and witty, Plum is currently a Harvard professor, celebrated for his work in the" \
               " fields of both chemistry and archaeology."

    greenText = "Mr. Green is a greedy, conniving mob boss who never misses a chance to make money."

    mustardText = "Colonel Mustard is a dignified, strong military man with a passion for hunting and valuable artwork."

    # print("Pause: ", pause)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if chooseScarlett.click() == True:
                    easygui.msgbox(scarlettText, "MS. SCARLETT")

                elif chooseWhite.click() == True:
                    easygui.msgbox(whiteText, "MRS. WHITE")

                elif choosePeacock.click() == True:
                    easygui.msgbox(peacockText, "MS. PEACOCK")

                elif choosePlum.click() == True:
                    easygui.msgbox(plumText, "PROF. PLUM")

                elif chooseGreen.click() == True:
                    easygui.msgbox(greenText, "MR. GREEN")

                elif chooseMustard.click() == True:
                    easygui.msgbox(mustardText, "COLONEL MUSTARD")

                elif nextButton.click() == True:
                    if pause == True:  # if they are accessing this from the pause menu - they go back to the pause menu when they hit continue
                        pauseScreen()
                    elif pause == False:  # if they are looking at this at the start of the game - they continue to the map once they hit continue
                        gameMap()

        suspectText.clear(screen, background)
        suspectText.update()
        suspectText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def leaderboard():
    global entry, score, askName, turnCount, scores
    global score1, score2, score3, score4, score5
    global name1, name2, name3, name4, name5, doneGame

    turnCount = str(turnCount)
    # print("#turns",turnCount)

    screen = pygame.display.set_mode((500, 450))
    pygame.display.set_caption("Leaderboard")

    background = pygame.Surface(screen.get_size())
    background.fill((211, 227, 232))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Leaderboard")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (250, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    contBtn = ButtonWords("Continue", 250, 410)
    contBtn.background = (225, 215, 226)

    #################################################
    allScores = []
    scoreFile = open("high_scores.txt", "r")  # makes file readable

    lines = scoreFile.readlines()
    for line in lines:  # splits everytime there's an enter
        words = line.split()
        for word in words:
            allScores.append(word)

    # print("all scores",allScores)

    name1 = allScores[0]
    score1 = allScores[1]

    name2 = allScores[2]
    score2 = allScores[3]

    name3 = allScores[4]
    score3 = allScores[5]

    name4 = allScores[6]
    score4 = allScores[7]

    name5 = allScores[8]
    score5 = allScores[9]

    #################################################

    name = Label()
    name.text = ("NAME")
    name.center = (125, 125)
    name.backcolour = (179, 234, 249)

    scoret = Label()
    scoret.text = ("SCORE")
    scoret.center = (375, 125)
    scoret.backcolour = (179, 234, 249)

    name1Label = scoreLabel(name1, 125, 175)
    name2Label = scoreLabel(name2, 125, 210)
    name3Label = scoreLabel(name3, 125, 245)
    name4Label = scoreLabel(name4, 125, 280)
    name5Label = scoreLabel(name5, 125, 315)

    score1Label = scoreLabel(score1, 375, 175)
    score2Label = scoreLabel(score2, 375, 210)
    score3Label = scoreLabel(score3, 375, 245)
    score4Label = scoreLabel(score4, 375, 280)
    score5Label = scoreLabel(score5, 375, 315)

    text = pygame.sprite.Group(title, contBtn, name, scoret, name1Label,
                               name2Label, name3Label, name4Label, name5Label, score1Label, score2Label,
                               score3Label, score4Label, score5Label)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if contBtn.click() == True:
                    if doneGame == True:
                        playAgain()
                    elif doneGame == False:
                        mainMenu()

        text.clear(screen, background)
        text.update()
        text.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def openNotepad():
    screen = pygame.display.set_mode((273, 673))
    pygame.display.set_caption("Notepad")

    back = pygame.Surface(screen.get_size())
    back = back.convert()
    back.fill((225, 225, 225))

    note = pygame.image.load("finalnotepad.png")
    note = note.convert()

    mouse = MagGlass()

    # if the player is finding out that one of these items was innocent then
    # it will be crossed off the notepad with one of these x's

    scarlettX = Xmark(210, 66, 1)
    whiteX = Xmark(210, 91, 2)  # suspect x's
    peacockX = Xmark(210, 116, 3)
    plumX = Xmark(210, 141, 4)
    greenX = Xmark(210, 166, 5)
    mustardX = Xmark(210, 191, 6)

    leadX = Xmark(210, 260)
    candleX = Xmark(210, 285)
    revolverX = Xmark(210, 313)
    ropeX = Xmark(210, 337)  # weapon x's
    knifeX = Xmark(210, 362)
    wrenchX = Xmark(210, 387)

    ballroomX = Xmark(210, 456)
    loungeX = Xmark(210, 481)
    billiardX = Xmark(210, 506)
    hallX = Xmark(210, 531)
    kitchenX = Xmark(210, 556)  # room x's
    diningX = Xmark(210, 583)
    conservatoryX = Xmark(210, 608)
    studyX = Xmark(210, 634)
    libraryX = Xmark(210, 658)

    xs = pygame.sprite.Group()  # group where x's for crossed off items go

    """when they get told that one of these things was not "guilty" it is added to a list called
    'crossedOff' and this is where we check to see what items are in the list.  If something needs
    to be crossed off then it is added to the sprite group that updates onto the screen when the player 
    clicks the notepad icon.  It is cleared if the player hits "play again" at the end of the game"""

    for item in crossedOff:
        if item == "Ms. Scarlett":
            xs.add(scarlettX)
        if item == "Mrs. White":
            xs.add(whiteX)
        if item == "Mrs. Peacock":
            xs.add(peacockX)
        if item == "Prof. Plum":
            xs.add(plumX)
        if item == "Mr. Green":
            xs.add(greenX)
        if item == "Colonel Mustard":
            xs.add(mustardX)

        if item == "Lead Pipe":
            xs.add(leadX)
        if item == "Candlestick":
            xs.add(candleX)
        if item == "Revolver":
            xs.add(revolverX)
        if item == "Rope":
            xs.add(ropeX)
        if item == "Knife":
            xs.add(knifeX)
        if item == "Wrench":
            xs.add(wrenchX)

        if item == "Ballroom":
            xs.add(ballroomX)
        if item == "Lounge":
            xs.add(loungeX)
        if item == "Billiard Room":
            xs.add(billiardX)
        if item == "Hall":
            xs.add(hallX)
        if item == "Kitchen":
            xs.add(kitchenX)
        if item == "Dining Room":
            xs.add(diningX)
        if item == "Conservatory":
            xs.add(conservatoryX)
        if item == "Study":
            xs.add(studyX)
        if item == "Library":
            xs.add(libraryX)

    mouseGroup = pygame.sprite.Group(mouse)

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameMap()
                keepGoing = False

        screen.blit(back, (0, 0))
        screen.blit(note, (0, 0))

        xs.clear(screen, back)
        mouseGroup.clear(screen, back)

        xs.update()
        mouseGroup.update()

        xs.draw(screen)
        mouseGroup.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def pauseScreen():
    """From the pause screen, the player is able to access the instructions, view the suspect
    and victim information, save and continue their game or go back to the map of the game"""

    global pause

    pause = True

    screen = pygame.display.set_mode((400, 330))
    pygame.display.set_caption("Pause Menu")

    background = pygame.Surface(screen.get_size())
    background.fill((220, 227, 239))
    screen.blit(background, (0, 0))

    gameBtn = ButtonWords("Back to the Game", 200, 50)
    instructBtn = ButtonWords("Instructions", 200, 100)
    saveBtn = ButtonWords("Save and Continue", 200, 150)

    suspectBtn = ButtonWords("Meet the Suspects", 200, 200)
    vicBtn = ButtonWords("Victim Info.", 200, 250)

    mainText = pygame.sprite.Group(gameBtn, instructBtn, saveBtn,
                                   suspectBtn, vicBtn)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameBtn.click() == True:
                    gameMap()
                elif instructBtn.click() == True:
                    instructions()
                elif saveBtn.click() == True:
                    pauseScreen()
                elif suspectBtn.click() == True:
                    suspectPage()
                elif vicBtn.click() == True:
                    vicPage()

        mainText.clear(screen, background)
        mainText.update()
        mainText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def gameMap():
    """This is the map of the game, they can start their guess from here, make a final accusation,
     access the pause menu and the mini game"""

    global guess
    global guessNum

    screen = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((239, 236, 206))
    screen.blit(background, (0, 0))

    guessNum = str(guessNum)  # this needs to be a string so it can be text
    guessesLeft = Label()
    guessesLeft.text = (guessNum)
    guessesLeft.font = pygame.font.SysFont("Courier", 40)
    guessesLeft.center = (1075, 112)
    guessesLeft.colour = (0, 0, 0)
    guessesLeft.backcolour = (255, 255, 255)

    # this makes the images of the rooms on the map into buttons
    ballroom = Button(350, 610, "Ballroom.png")
    lounge = Button(590, 95, "Lounge.png")
    billiard = Button(110, 455, "BilliardRoom.png")
    hall = Button(350, 115, "Hall.png")
    kitchen = Button(610, 580, "Kitchen.png")
    dining = Button(625, 335, "DiningRoom.png")
    conservatory = Button(110, 635, "Conservatory.png")
    study = Button(115, 70, "Study.png")
    library = Button(110, 250, "Library.png")
    lab = Button(355, 360, "Lab.png")
    notepad = Button(825, 80, "notepad.png")
    pause = Button(950, 75, "pause.png")
    turnsBtn = Button(1075, 75, "GuessesLeft.png")
    smallLogo = CornerLogo()
    mouse = MagGlass()
    accusation = Button(980, 400, "accusation.png")

    allRooms = pygame.sprite.Group(ballroom, lounge, billiard, hall, kitchen,
                                   dining, conservatory, study, library, lab, notepad, pause,
                                   accusation, turnsBtn, guessesLeft)

    otherSprite = pygame.sprite.Group(mouse, smallLogo)

    clock = pygame.time.Clock()
    keepGoing = True

    # once they choose which room to make their guess in - they continue to guess the suspect then weapon
    # the room they choose is added to the "guess" list which will later be used to give them a clue

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                guessNum = int(
                    guessNum)  # needs to be an integer so we can check its value (check if they have any tuns left)
                if guessNum == 0:  # if they don't have any turns left, they are forced to make their final guess of the game
                    easygui.msgbox("Sorry, you don't have any turns left. You may make your final accusation")
                    accusationPage()
                # print ( ballroom.click()) - true or false
                elif ballroom.click() == True:
                    guess.append("Ballroom")
                    easygui.msgbox("Your guess will take place in the ballroom", "Ballroom", "guess suspect",
                                   image="inBallroom.gif")
                    guessSuspect()

                elif lounge.click() == True:
                    guess.append("Lounge")
                    easygui.msgbox("Your guess will take place in the lounge", "Lounge", "guess suspect",
                                   image="inLounge.gif")
                    guessSuspect()

                elif billiard.click() == True:
                    guess.append("Billiard Room")
                    easygui.msgbox("Your guess will take place in the billiard room", "Billiard Room", "guess suspect",
                                   image="inBilliard.gif")
                    guessSuspect()

                elif hall.click() == True:
                    guess.append("Hall")
                    easygui.msgbox("Your guess will take place in the hall", "Hall", "guess suspect",
                                   image="inHall.gif")
                    guessSuspect()

                elif kitchen.click() == True:
                    guess.append("Kitchen")
                    easygui.msgbox("Your guess will take place in the kitchen", "Kitchen", "guess suspect",
                                   image="inKitchen.gif")
                    guessSuspect()

                elif dining.click() == True:
                    guess.append("Dining Room")
                    easygui.msgbox("Your guess will take place in the dining room", "Dining Room", "guess suspect",
                                   image="inDining.gif")
                    guessSuspect()

                elif conservatory.click() == True:
                    guess.append("Conservatory")
                    easygui.msgbox("Your guess will take place in the conservatory", "Conservatory", "guess suspect",
                                   image="inConservatory.gif")
                    guessSuspect()

                elif study.click() == True:
                    guess.append("Study")
                    easygui.msgbox("Your guess will take place in the study", "Study", "guess suspect",
                                   image="inStudy.gif")
                    guessSuspect()

                elif library.click() == True:
                    guess.append("Library")
                    easygui.msgbox("Your guess will take place in the library", "Library", "guess suspect",
                                   image="inLibrary.gif")
                    guessSuspect()

                elif lab.click() == True:
                    miniGame()

                elif notepad.click() == True:
                    openNotepad()

                elif pause.click() == True:
                    pauseScreen()

                elif accusation.click() == True:
                    accusationPage()

        allRooms.clear(screen, background)
        otherSprite.clear(screen, background)
        allRooms.update()
        otherSprite.update()
        allRooms.draw(screen)
        otherSprite.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def miniGame():
    global screen, clock, labTries, miniPlay, guessNum

    labTries = int(labTries)
    miniPlay = int(miniPlay)

    screen = pygame.display.set_mode((1000, 800))

    FPS = 30
    windoww = 1550
    windowh = 807
    square_size = 100
    square_gap = 20
    board_width = 4
    board_height = 4

    boxcolour = (255, 255, 255)

    clock = pygame.time.Clock()

    mouse_x = 0
    mouse_y = 0
    mouse_clicked = False
    first_selection = None
    # create allImages list
    allImages = ["magGlass.gif", "magGlass.gif", "notebook.gif", "notebook.gif", "prints.gif", "prints.gif", "tape.gif",
                 "tape.gif", "lie.gif", "lie.gif", "goggles.gif", "goggles.gif", "dna.gif", "dna.gif", "case.gif",
                 "case.gif"]
    # shuffles images to ensure game is random
    random.shuffle(allImages)

    # loads the images into the game
    image1 = pygame.image.load(allImages[0])
    image2 = pygame.image.load(allImages[1])
    image3 = pygame.image.load(allImages[2])
    image4 = pygame.image.load(allImages[3])
    image5 = pygame.image.load(allImages[4])
    image6 = pygame.image.load(allImages[5])
    image7 = pygame.image.load(allImages[6])
    image8 = pygame.image.load(allImages[7])
    image9 = pygame.image.load(allImages[8])
    image10 = pygame.image.load(allImages[9])
    image11 = pygame.image.load(allImages[10])
    image12 = pygame.image.load(allImages[11])
    image13 = pygame.image.load(allImages[12])
    image14 = pygame.image.load(allImages[13])
    image15 = pygame.image.load(allImages[14])
    image16 = pygame.image.load(allImages[15])

    screen = pygame.display.set_mode((windoww, windowh))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("inLab.gif")

    pick1 = None  # when you pick first picture, pick1 changes to the corresponding number
    pick2 = None  # when you pick second pic, pick2 changes to the corresponding number
    outofpick = False
    choose = 0
    compare1 = ""
    compare2 = ""
    counter = 0
    counterStart = False
    turns = 0

    b1check = True  # all images are hidden, all boxes are revealed
    b2check = True
    b3check = True
    b4check = True
    b5check = True
    b6check = True
    b7check = True
    b8check = True
    b9check = True
    b10check = True
    b11check = True
    b12check = True
    b13check = True
    b14check = True
    b15check = True
    b16check = True

    checks = [b1check, b2check, b3check, b4check, b5check, b6check, b7check, b8check, b9check, b10check, b11check,
              b12check, b13check, b14check, b15check, b16check]  # creates a list of checks (can compare them)

    # instructions
    myFont = pygame.font.SysFont("Courier", 28)
    myFont2 = pygame.font.SysFont("Courier", 14)
    welcomelab = myFont.render("WELCOME TO THE LAB!", 8, (0, 0, 0))
    instruct = myFont.render("Instructions:", 6, (0, 0, 0))
    instruct2 = myFont2.render("The lab has been ransacked!", 2, (0, 0, 0))
    instruct3 = myFont2.render("Tools and evidence are everywhere!", 2, (0, 0, 0))
    instruct4 = myFont2.render("Flip over the cards and", 2, (0, 0, 0))
    instruct5 = myFont2.render("match up all images to win!", 2, (0, 0, 0))

    instruct10 = myFont2.render("You will get extra guesses in", 2, (0, 0, 0))
    instruct11 = myFont2.render("the main game based on how good", 2, (0, 0, 0))
    instruct12 = myFont2.render("you do in this minigame", 2, (0, 0, 0))

    instruct6 = myFont2.render("Rewards:", 2, (0, 0, 0))
    instruct7 = myFont2.render("15 or less turns = 5 extra guesses", 2, (0, 0, 0))
    instruct8 = myFont2.render("16-22 turns = 3 extra guesses", 2, (0, 0, 0))
    instruct9 = myFont2.render("23 or more turns = 1 extra guess", 2, (0, 0, 0))

    pygame.draw.rect(background, (255, 255, 255), (550, 50, 400, 120))
    pygame.draw.rect(background, (255, 255, 255), (50, 265, 300, 410))

    # below is where we check to see if they still have attempts left on the minigame
    # (the number of mini game tries depends on what level they chose at the start of the game- they will get 1-3 tries)
    # if they have played the maximum number of times then they are sent back to the game

    if labTries == miniPlay:
        easygui.msgbox("Sorry, you have played the maximum number of times")
        gameMap()
    else:
        pass

    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_clicked = True

                if pick1 == None and pick2 == None:
                    # When the player picks the first box (x and y coordinates correspond to a box)

                    if 699 < mouse_x < 801 and 299 < mouse_y < 401:
                        checks[0] = False
                        pick1 = 0

                    if 824 < mouse_x < 926 and 299 < mouse_y < 401:
                        checks[1] = False
                        pick1 = 1

                    if 949 < mouse_x < 1051 and 299 < mouse_y < 401:
                        checks[2] = False
                        pick1 = 2

                    if 1074 < mouse_x < 1176 and 299 < mouse_y < 401:
                        checks[3] = False
                        pick1 = 3

                    if 699 < mouse_x < 801 and 424 < mouse_y < 526:
                        checks[4] = False
                        pick1 = 4

                    if 824 < mouse_x < 926 and 424 < mouse_y < 526:
                        checks[5] = False
                        pick1 = 5

                    if 949 < mouse_x < 1051 and 424 < mouse_y < 526:
                        checks[6] = False
                        pick1 = 6

                    if 1074 < mouse_x < 1176 and 424 < mouse_y < 526:
                        checks[7] = False
                        pick1 = 7

                    if 699 < mouse_x < 801 and 549 < mouse_y < 651:
                        checks[8] = False
                        pick1 = 8

                    if 824 < mouse_x < 926 and 549 < mouse_y < 651:
                        checks[9] = False
                        pick1 = 9

                    if 949 < mouse_x < 1051 and 549 < mouse_y < 651:
                        checks[10] = False
                        pick1 = 10

                    if 1074 < mouse_x < 1176 and 549 < mouse_y < 651:
                        checks[11] = False
                        pick1 = 11

                    if 699 < mouse_x < 801 and 674 < mouse_y < 776:
                        checks[12] = False
                        pick1 = 12

                    if 824 < mouse_x < 926 and 674 < mouse_y < 776:
                        checks[13] = False
                        pick1 = 13

                    if 949 < mouse_x < 1051 and 674 < mouse_y < 776:
                        checks[14] = False
                        pick1 = 14

                    if 1074 < mouse_x < 1176 and 674 < mouse_y < 776:
                        checks[15] = False
                        pick1 = 15

                elif pick1 >= 0 and pick2 == None:
                    # When the player picks the second box (x and y coordinates correspond to a box)
                    # when out of pick = True, images are compared

                    if 699 < mouse_x < 801 and 299 < mouse_y < 401:
                        checks[0] = False
                        pick2 = 0
                        outofpick = True

                    elif 824 < mouse_x < 926 and 299 < mouse_y < 401:
                        checks[1] = False
                        pick2 = 1
                        outofpick = True

                    elif 949 < mouse_x < 1051 and 299 < mouse_y < 401:
                        checks[2] = False
                        pick2 = 2
                        outofpick = True

                    if 1074 < mouse_x < 1176 and 299 < mouse_y < 401:
                        checks[3] = False
                        pick2 = 3
                        outofpick = True

                    if 699 < mouse_x < 801 and 424 < mouse_y < 526:
                        checks[4] = False
                        pick2 = 4
                        outofpick = True

                    if 824 < mouse_x < 926 and 424 < mouse_y < 526:
                        checks[5] = False
                        pick2 = 5
                        outofpick = True

                    if 949 < mouse_x < 1051 and 424 < mouse_y < 526:
                        checks[6] = False
                        pick2 = 6
                        outofpick = True

                    if 1074 < mouse_x < 1176 and 424 < mouse_y < 526:
                        checks[7] = False
                        pick2 = 7
                        outofpick = True

                    if 699 < mouse_x < 801 and 549 < mouse_y < 651:
                        checks[8] = False
                        pick2 = 8
                        outofpick = True

                    if 824 < mouse_x < 926 and 549 < mouse_y < 651:
                        checks[9] = False
                        pick2 = 9
                        outofpick = True

                    if 949 < mouse_x < 1051 and 549 < mouse_y < 651:
                        checks[10] = False
                        pick2 = 10
                        outofpick = True

                    if 1074 < mouse_x < 1176 and 549 < mouse_y < 651:
                        checks[11] = False
                        pick2 = 11
                        outofpick = True

                    if 699 < mouse_x < 801 and 674 < mouse_y < 776:
                        checks[12] = False
                        pick2 = 12
                        outofpick = True

                    if 824 < mouse_x < 926 and 674 < mouse_y < 776:
                        checks[13] = False
                        pick2 = 13
                        outofpick = True

                    if 949 < mouse_x < 1051 and 674 < mouse_y < 776:
                        checks[14] = False
                        pick2 = 14
                        outofpick = True

                    if 1074 < mouse_x < 1176 and 674 < mouse_y < 776:
                        checks[15] = False
                        pick2 = 15
                        outofpick = True
                # this code is when checking a mouse button pressed

            if outofpick == True:  # starts to compare images
                turns = turns + 1  # adds 1 to turns
                # print(checks)
                # print ("allImages pick 1 is ", allImages[pick1], "pick1 is ", pick1, "and the second allIMages[pick2] = ", allImages[pick2], pick2)
                if allImages[pick1] == allImages[pick2]:  # if a pair is found
                    # print("pair found")
                    checks[pick1] = False
                    checks[pick2] = False
                    outofpick = False
                    pick1 = None
                    pick2 = None

                else:  # if a pair is not found
                    # print ("resetting")
                    counter = 0
                    counterStart = True
                    outofpick = False

            # if player has found all matches
            if checks[0] == False and checks[1] == False and checks[2] == False and checks[3] == False and checks[
                4] == False and checks[5] == False and checks[6] == False and checks[7] == False and checks[
                8] == False and checks[9] == False and checks[10] == False and checks[11] == False and checks[
                12] == False and checks[13] == False and checks[14] == False and checks[15] == False:
                time.sleep(2)
                # print("turns:",turns)

                miniPlay = miniPlay + 1

                if turns < 16:
                    guessNum = guessNum + 5  # adds five turns
                    easygui.msgbox("You have earned 5 extra turns!")
                    gameMap()

                elif turns > 15 and turns < 23:
                    guessNum = guessNum + 3  # adds three turns
                    easygui.msgbox("You have earned 3 extra turns!")
                    gameMap()

                elif turns > 22:
                    guessNum = guessNum + 1
                    easygui.msgbox("You have earned 1 extra turn!")
                    gameMap()

                # print("New # turns: ")

            screen.blit(background, (0, 0))
            # draws either image or box
            if checks[0] == True:
                box1 = pygame.draw.rect(background, (255, 0, 0), (700, 300, 100, 100))
            if checks[0] == False:
                screen.blit(image1, (700, 300))

            if checks[1] == True:
                box2 = pygame.draw.rect(background, (255, 0, 0), (825, 300, 100, 100))
            if checks[1] == False:
                screen.blit(image2, (825, 300))

            if checks[2] == True:
                box3 = pygame.draw.rect(background, (255, 0, 0), (950, 300, 100, 100))
            if checks[2] == False:
                screen.blit(image3, (950, 300))

            if checks[3] == True:
                box4 = pygame.draw.rect(background, (255, 0, 0), (1075, 300, 100, 100))
            if checks[3] == False:
                screen.blit(image4, (1075, 300))

            if checks[4] == True:
                box5 = pygame.draw.rect(background, (255, 0, 0), (700, 425, 100, 100))
            if checks[4] == False:
                screen.blit(image5, (700, 425))

            if checks[5] == True:
                box6 = pygame.draw.rect(background, (255, 0, 0), (825, 425, 100, 100))
            if checks[5] == False:
                screen.blit(image6, (825, 425))

            if checks[6] == True:
                box7 = pygame.draw.rect(background, (255, 0, 0), (950, 425, 100, 100))
            if checks[6] == False:
                screen.blit(image7, (950, 425))

            if checks[7] == True:
                box8 = pygame.draw.rect(background, (255, 0, 0), (1075, 425, 100, 100))
            if checks[7] == False:
                screen.blit(image8, (1075, 425))

            if checks[8] == True:
                box9 = pygame.draw.rect(background, (255, 0, 0), (700, 550, 100, 100))
            if checks[8] == False:
                screen.blit(image9, (700, 550))

            if checks[9] == True:
                box10 = pygame.draw.rect(background, (255, 0, 0), (825, 550, 100, 100))
            if checks[9] == False:
                screen.blit(image10, (825, 550))

            if checks[10] == True:
                box11 = pygame.draw.rect(background, (255, 0, 0), (950, 550, 100, 100))
            if checks[10] == False:
                screen.blit(image11, (950, 550))

            if checks[11] == True:
                box12 = pygame.draw.rect(background, (255, 0, 0), (1075, 550, 100, 100))
            if checks[11] == False:
                screen.blit(image12, (1075, 550))

            if checks[12] == True:
                box13 = pygame.draw.rect(background, (255, 0, 0), (700, 675, 100, 100))
            if checks[12] == False:
                screen.blit(image13, (700, 675))

            if checks[13] == True:
                box14 = pygame.draw.rect(background, (255, 0, 0), (825, 675, 100, 100))
            if checks[13] == False:
                screen.blit(image14, (825, 675))

            if checks[14] == True:
                box15 = pygame.draw.rect(background, (255, 0, 0), (950, 675, 100, 100))
            if checks[14] == False:
                screen.blit(image15, (950, 675))

            if checks[15] == True:
                box16 = pygame.draw.rect(background, (255, 0, 0), (1075, 675, 100, 100))
            if checks[15] == False:
                screen.blit(image16, (1075, 675))

        #  x, y = get_pos(mouse_x, mouse_y)

        counter = counter + 1
        if counter > 30 and counterStart == True:  # delay

            checks[pick1] = True
            checks[pick2] = True
            pick1 = None
            pick2 = None
            # This is the counter reset code

            counterStart = False
            counter = 0

        screen.blit(welcomelab, (600, 100))
        screen.blit(instruct, (65, 275))
        screen.blit(instruct2, (65, 320))
        screen.blit(instruct3, (65, 350))
        screen.blit(instruct4, (65, 380))
        screen.blit(instruct5, (65, 410))
        screen.blit(instruct10, (65, 440))
        screen.blit(instruct11, (65, 470))
        screen.blit(instruct12, (65, 500))
        screen.blit(instruct6, (65, 530))
        screen.blit(instruct7, (65, 560))
        screen.blit(instruct8, (65, 590))
        screen.blit(instruct9, (65, 620))

        pygame.display.flip()


def guessSuspect():
    global guess
    global ready

    screen = pygame.display.set_mode((650, 700))
    pygame.display.set_caption("Guess the Suspect")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Guess the Suspect")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (325, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    # turns the images into buttons
    chooseScarlett = Button(120, 230, "MissScarlett.png")
    chooseWhite = Button(320, 230, "MrsWhite.png")
    choosePeacock = Button(515, 231, "MrsPeacock.png")
    choosePlum = Button(120, 520, "ProfPlum.png")
    chooseGreen = Button(320, 520, "MrGreen.png")
    chooseMustard = Button(515, 520, "ColonelMustard.png")

    suspectText = pygame.sprite.Group(title, chooseScarlett, chooseWhite, choosePeacock,
                                      choosePlum, chooseGreen, chooseMustard)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if ready == False:  # if ready is false that means this is a normal turn(NOT the final accusation)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if chooseScarlett.click() == True:  # the suspect they choose is also added to the "guess" list for later
                        guess.append("Ms. Scarlett")  # so we can give them a clue
                        guessWeapon()
                    elif chooseWhite.click() == True:
                        guess.append("Mrs. White")
                        guessWeapon()  # they continue to guess the weapon
                    elif choosePeacock.click() == True:
                        guess.append("Mrs. Peacock")
                        guessWeapon()
                    elif choosePlum.click() == True:
                        guess.append("Prof. Plum")
                        guessWeapon()
                    elif chooseGreen.click() == True:
                        guess.append("Mr. Green")
                        guessWeapon()
                    elif chooseMustard.click() == True:
                        guess.append("Colonel Mustard")
                        guessWeapon()

            if ready == True:  # if ready is true then this guess is for the final accusation
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if chooseScarlett.click() == True:
                        accusation.append("Ms. Scarlett")  # suspect added to "accusation" list to see
                        guessWeapon()  # if they got the correct killer
                    elif chooseWhite.click() == True:
                        accusation.append("Mrs. White")
                        guessWeapon()
                    elif choosePeacock.click() == True:
                        accusation.append("Mrs. Peacock")
                        guessWeapon()
                    elif choosePlum.click() == True:
                        accusation.append("Prof. Plum")
                        guessWeapon()
                    elif chooseGreen.click() == True:
                        accusation.append("Mr. Green")
                        guessWeapon()
                    elif chooseMustard.click() == True:
                        accusation.append("Colonel Mustard")
                        guessWeapon()

                        # print(accusation) #this is the final guess of the game

        suspectText.clear(screen, background)
        suspectText.update()
        suspectText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def guessWeapon():
    global guess
    global ready

    screen = pygame.display.set_mode((635, 700))
    pygame.display.set_caption("Guess the Weapon")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Guess the Weapon")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (325, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    # turns the images into buttons
    chooseCandle = Button(120, 230, "candlestick.gif")
    chooseWrench = Button(320, 230, "wrench.png")
    chooseRevolver = Button(515, 230, "revolver.gif")
    choosePipe = Button(120, 520, "leadpipe.gif")
    chooseRope = Button(320, 520, "rope.gif")
    chooseKnife = Button(515, 520, "knife.gif")

    weaponText = pygame.sprite.Group(title, chooseCandle, chooseWrench, chooseRevolver,
                                     chooseRope, choosePipe, chooseKnife)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if ready == False:  # if ready is false, this is a normal turn (NOT the final accusation)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if chooseCandle.click() == True:
                        candleSound.play()  # sound effect for each weapon
                        guess.append("Candlestick")
                        totalGuess()
                    elif chooseWrench.click() == True:
                        wrenchSound.play()  # weapon guess is final thing that is added to "guess list"
                        guess.append("Wrench")
                        totalGuess()
                    elif chooseRevolver.click() == True:
                        gunSound.play()
                        guess.append("Revolver")
                        totalGuess()
                    elif choosePipe.click() == True:
                        pipeSound.play()
                        guess.append("Lead Pipe")
                        totalGuess()
                    elif chooseRope.click() == True:
                        ropeSound.play()
                        guess.append("Rope")
                        totalGuess()
                    elif chooseKnife.click() == True:
                        knifeSound.play()
                        guess.append("Knife")
                        totalGuess()

            if ready == True:  # if ready is true this guess if for the final accusation
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if chooseCandle.click() == True:
                        candleSound.play()
                        accusation.append("Candlestick")
                        guessRoom()
                    elif chooseWrench.click() == True:
                        wrenchSound.play()
                        accusation.append(
                            "Wrench")  # the weapon is added to "accusation" list so we can check to see if
                        guessRoom()  # they got the correct murder weapon
                    elif chooseRevolver.click() == True:
                        gunSound.play()
                        accusation.append("Revolver")
                        guessRoom()
                    elif choosePipe.click() == True:
                        pipeSound.play()
                        accusation.append("Lead Pipe")
                        guessRoom()
                    elif chooseRope.click() == True:
                        ropeSound.play()
                        accusation.append("Rope")
                        guessRoom()
                    elif chooseKnife.click() == True:
                        knifeSound.play()
                        accusation.append("Knife")
                        guessRoom()

        weaponText.clear(screen, background)
        weaponText.update()
        weaponText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def guessRoom():
    """This page is for when the player is making their final accusation.  Usually, they would guess the room from the map
    but instead, they choose it from this list with the names of the rooms"""

    global ready

    screen = pygame.display.set_mode((500, 510))
    pygame.display.set_caption("Guess the Location")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Guess the Location")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (250, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    # makes the text into buttons
    ballBtn = ButtonWords("Ballroom", 250, 125)
    loungeBtn = ButtonWords("Lounge", 250, 165)
    billBtn = ButtonWords("Billiard Room", 250, 205)
    hallBtn = ButtonWords("Hall", 250, 245)
    kitchBtn = ButtonWords("Kitchen", 250, 285)
    dinBtn = ButtonWords("Dining Room", 250, 325)
    consBtn = ButtonWords("Conservatory", 250, 365)
    studyBtn = ButtonWords("Study", 250, 405)
    libBtn = ButtonWords("Library", 250, 445)

    roomText = pygame.sprite.Group(title, ballBtn, loungeBtn, billBtn, hallBtn, kitchBtn,
                                   dinBtn, consBtn, studyBtn, libBtn)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ballBtn.click() == True:
                    accusation.append(
                        "Ballroom")  # room is added to the "accusation" list so we can check to see if they got the correct
                    finalCheck()  # room where the murder happend
                elif loungeBtn.click() == True:
                    accusation.append("Lounge")
                    finalCheck()  # they continue to see if they have won the game or not
                elif billBtn.click() == True:
                    accusation.append("Billiard Room")
                    finalCheck()
                elif hallBtn.click() == True:
                    accusation.append("Hall")
                    finalCheck()
                elif kitchBtn.click() == True:
                    accusation.append("Kitchen")
                    finalCheck()
                elif dinBtn.click() == True:
                    accusation.append("Dining Room")
                    finalCheck()
                elif consBtn.click() == True:
                    accusation.append("Conservatory")
                    finalCheck()
                elif studyBtn.click() == True:
                    accusation.append("Study")
                    finalCheck()
                elif libBtn.click() == True:
                    accusation.append("Library")
                    finalCheck()

        roomText.clear(screen, background)
        roomText.update()
        roomText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def totalGuess():
    """This screen is where the player is taken after they make their guess of the suspect, weapon and room.
    We give them a clue so they can narrow down who the guilty party is."""

    global guess, crossOff, crossedOff, guessNum, turnCount

    # these are alibis of what an innocent suspect could have been doing during the murder (means they couldn't have been
    # the murderer if they were too busy doing one of these things)

    innocentSuspect = ["quite tired after dinner and went to take a little nap",
                       "looking for a bathroom",
                       "fixing their makeup in the mirrors",
                       "feeling a little peckish so went down to grab something to eat",
                       "reading a novel on the sofa",
                       "admiring the beautiful artwork",
                       "deep in thought",
                       "reading a magazine",
                       "having a drink after dinner",
                       "shuffling a deck of cards",
                       "listening to music",
                       "watching a film"]

    ######################################################

    # these are where the weapons could have been doing during the murder (reasons why they couldn't have been the murder weapon)

    innWrench = ["someone left it outside in the rain after repairing the outdoor plumbing",
                 "someone couldn’t find a hammer so they used a wrench to strike a nail… It was not ideal, but it worked",
                 "it was left under the sink because there was a rather aggravating leaky faucet"]

    innCandle = ["lights went out in one of the hallways so we were using the candlestick to light the way",
                 "we were telling ghost stories after dinner. We used a candle under our chins to add to the ambiance",
                 "it was left on the dinner table… Someone would not sacrifice the beautiful decorations for murder"]

    innPipe = ["we refuse to touch the lead pipe! We heard it was extremely toxic…",
               "you really think we would touch that toxic piece of metal?! Think again, dear detective",
               "the table was slightly off balance so we were using the pipe under one of the legs to balance it out"]

    innRevolver = ["it is a very expensive revolver. Someone left it locked in the safe!",
                   "someone was shining it earlier in the garage and left it in there",
                   "someone went hunting earlier in the day and used up all of the amo..."]

    innRope = ["someone was practicing some rope jewelry and used up all of the rope",
               "the rope was safely stowed in someone’s camping survival kit out in the shed",
               "someone had tied the family rottweiler to a tree outside with the last of the rope"]

    innKnife = ["the knife was in the sink as it had been used to prepare dinner that night",
                "the knife had just been used to open up a package and was left untouched near the door",
                "someone used the knife to cut their hair upstairs and forgot about it in the hustle and bustle"]

    ##################################################

    # these are excuses of why the murder couldn't have taken place in one of these rooms

    innBallroom = ["nobody was in the mood for dancing", "nobody felt like listening to music"]

    innLounge = ["nobody felt like relaxing", "nobody could find a good magazine in there"]

    innBill = ["nobody is really that keen on pool", "we had already played a game of pool before dinner"]

    innHall = ["it wastoo bright and out in the open to kill anyone in there",
               "there were too many windows to kill anyone secretly in there"]

    innKitchen = ["someone had burned some toast and the smell was too strong to go in",
                  "there was too many surfaces to clean if anyone killed someone in there"]

    innDining = ["the food had not been cleared up yet and nobody wanted to see that",
                 "dome people were still finishing dinner in the dining room"]

    innConserv = ["too many windows! Anyone would be able to see the murder if they walked by",
                  "someone was tending to the plants in the conservatory"]

    innStudy = ["nobody was in the right mindset to study", "someone was reading a book in the study"]

    innLibrary = ["too many expensive books to risk a murder in there!",
                  "the owner had locked the library after someone had spilt wine on a priceless novel"]

    #####################################################

    screen = pygame.display.set_mode((1000, 550))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    mapBtn = ButtonWords("Back to Map", 500, 510)

    title = Label()
    title.text = ("The suspects are thinking...")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (500, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    suspectGuess = guess[1]
    weaponGuess = guess[2]
    roomSet = guess[0]

    subtitle = Label()
    subtitle.text = ("Your guess was:")
    subtitle.center = (500, 125)
    subtitle.colour = (0, 0, 0)
    subtitle.backcolour = (202, 249, 249)

    guess1 = Label()
    guess1.text = (suspectGuess)
    guess1.center = (500, 175)
    guess1.colour = (0, 0, 0)
    guess1.backcolour = (255, 255, 255)

    guess2 = Label()
    guess2.text = (weaponGuess)
    guess2.center = (500, 225)
    guess2.colour = (0, 0, 0)
    guess2.backcolour = (255, 255, 255)

    guess3 = Label()
    guess3.text = (roomSet)
    guess3.center = (500, 275)
    guess3.colour = (0, 0, 0)
    guess3.backcolour = (255, 255, 255)

    yourClue = Label()
    yourClue.text = ("Your Clue:")
    yourClue.center = (500, 350)
    yourClue.colour = (255, 255, 255)
    yourClue.backcolour = (0, 0, 0)

    ################################################

    # here is where we compare the items they just guessed to the people/items/rooms that are innocent
    # so we can tell them a clue of something that was not involved in the murder

    # if all 3 things they guessed are in evidence, it means everything they guessed is innocent
    if guess[0] in evidence and guess[1] in evidence and guess[2] in evidence:
        wrongGuess.append(guess[0])
        wrongGuess.append(guess[1])  # the things they guess wrong are added to another list called "wrongGuess"
        wrongGuess.append(guess[2])

    # these are for if they guessed 2 of 3 things incorrectly
    elif guess[0] in evidence and guess[1] in evidence:
        wrongGuess.append(guess[1])
        wrongGuess.append(guess[0])

    elif guess[0] in evidence and guess[2] in evidence:
        wrongGuess.append(guess[0])
        wrongGuess.append(guess[2])

    elif guess[1] in evidence and guess[2] in evidence:
        wrongGuess.append(guess[1])
        wrongGuess.append(guess[2])

    # these statements are for if they only guessed one thing wrong
    elif guess[0] in evidence:
        wrongGuess.append(guess[0])

    elif guess[1] in evidence:
        wrongGuess.append(guess[1])

    elif guess[2] in evidence:
        wrongGuess.append(guess[2])

    # print("guess:", guess)
    # print("wrong guess:",wrongGuess)

    numWrong = len(wrongGuess)
    # number of things they guess that are in evidence - so are not the correct "guilty party" of the game
    # print("length of wrong guess:", numWrong)

    clue = Label()
    clue.center = (500, 400)
    clue.colour = (0, 0, 0)
    clue.backcolour = (255, 255, 255)
    clue.font = pygame.font.SysFont("Courier", 14)

    excuse = Label()
    excuse.center = (500, 435)
    excuse.colour = (0, 0, 0)
    excuse.backcolour = (255, 255, 255)
    excuse.font = pygame.font.SysFont("Courier", 14)

    # "crossOff" is the most recent thing that they are told is innocent
    # "crossedOff" is the list of EVERYTHING that they have been told is innocent so far

    if numWrong == 0:  # if they guessed 0 things wrong - this means they've figured it out - the 3 things in the envelope
        clue.text = ("The suspects seem nervous. They have no new information for you......")
        excuse.text = ("what could that mean?")

    elif numWrong == 1:  # if they guessed one thing wrong then they are told that that one thing is innocent
        crossOff = wrongGuess[0]
        crossedOff.append(crossOff)  # added to "crossed off" so it will show up with an "x" in the notepad

    elif numWrong == 2:  # if they guessed 2 things wrong, one is randomly chosen and they are told that thing is innocent
        crossOff = wrongGuess[random.randint(0, 1)]
        crossedOff.append(crossOff)

    elif numWrong == 3:  # if they guess all 3 things wrong, one is chosen at random and they are told it is innocent
        crossOff = (wrongGuess[random.randint(0, 2)])
        crossedOff.append(crossOff)

    if numWrong > 0:  # so they got at least 1 thing in their guess incorrect

        # if the thing being crossed off is a suspect, then one of the suspect alibis from above will be chosen randomly
        if crossOff in suspects:
            clue.text = ("You have been told that " + crossOff + " is innocent")
            excuse.text = ("since they were " + innocentSuspect[random.randint(0, 11)])

        # if the thing being crossed off is a weapon then we check which weapon it is and use one of those excuses
        # of why that specific weapon was not the murder weapon
        elif crossOff in weapons:
            clue.text = ("The suspects say " + crossOff + " was not the murder weapon")
            if crossOff == "Lead Pipe":
                excuse.text = ("because " + innPipe[random.randint(0, 2)])
            elif crossOff == "Candlestick":
                excuse.text = ("because " + innCandle[random.randint(0, 2)])
            elif crossOff == "Revolver":
                excuse.text = ("because " + innRevolver[random.randint(0, 2)])
            elif crossOff == "Rope":
                excuse.text = ("because " + innRope[random.randint(0, 2)])
            elif crossOff == "Knife":
                excuse.text = ("because " + innKnife[random.randint(0, 2)])
            elif crossOff == "Wrench":
                excuse.text = ("because " + innWrench[random.randint(0, 2)])

        # if it is a room being crossed off this turn then we check which room it is and randomly choose one of
        # the reasons of why the murder did not take place in that specific room

        elif crossOff in map:
            clue.text = ("The murder did not take place in the " + crossOff)
            if crossOff == "Ballroom":
                excuse.text = ("because " + innBallroom[random.randint(0, 1)])
            elif crossOff == "Lounge":
                excuse.text = ("because " + innLounge[random.randint(0, 1)])
            elif crossOff == "Billiard Room":
                excuse.text = ("because " + innBill[random.randint(0, 1)])
            elif crossOff == "Hall":
                excuse.text = ("because " + innHall[random.randint(0, 1)])
            elif crossOff == "Kitchen":
                excuse.text = ("because " + innKitchen[random.randint(0, 1)])
            elif crossOff == "Dining Room":
                excuse.text = ("because " + innDining[random.randint(0, 1)])
            elif crossOff == "Conservatory":
                excuse.text = ("because " + innConserv[random.randint(0, 1)])
            elif crossOff == "Study":
                excuse.text = ("because " + innStudy[random.randint(0, 1)])
            elif crossOff == "Library":
                excuse.text = ("because " + innLibrary[random.randint(0, 1)])

        # print("Crossed off this round:", crossOff)
    # print("Everything crossed off:", crossedOff)

    # clear the guess list for the next turn
    guess.clear()
    wrongGuess.clear()

    # print("cleared guess", guess)

    guessText = pygame.sprite.Group(title, guess1, guess2, guess3, subtitle, clue, yourClue, excuse, mapBtn)

    # print("# turns", guessNum)
    guessNum = int(guessNum)
    guessNum = guessNum - 1  # this is the end of their turn and we subtract one from their turn count
    # print("# turns", guessNum)

    turnCount = int(turnCount)
    turnCount = turnCount + 1  # this is the counter for the total number of turns they take during the entire game

    ##################################################

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapBtn.click() == True:  # after they are told their clue, they go back to the game to make another guess
                    gameMap()

        guessText.clear(screen, background)
        guessText.update()
        guessText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def accusationPage():
    """"when the player decides/is forced to make the final accusation, we se the variable "ready" as true
    so we can use the pages we previously made to guess the suspect and the weapon - if ready is false, the
    things they guess are added to the "guess" list, if ready is true, the things they guess are added to
    the "accusation" list """

    global ready
    global guessNum

    ready = True

    # if they press the final accusation button before they run out of the allowed number of turns, we ask to make sure they are ready
    # if they say yes then they continue, if they say no, they are sent back to the game to make more guesses

    if guessNum != 0:
        readyGuess = easygui.buttonbox("Are you sure you want to make your final guess?", "ACCUSATION",
                                       choices=('yes', 'no'))

        if (readyGuess == "yes"):
            easygui.msgbox(
                "Ok, guess the suspect you think committed the crime, the murder weapon you think was used, and"
                " the location where you think the murder took place.")
            guessSuspect()

        elif (readyGuess == "no"):
            ready = False
            gameMap()

        else:
            print("Something went wrong")

    elif guessNum == 0:
        guessSuspect()


def finalCheck():
    """"This page is where the player finds out if they won the game or not and they are told
    who the actual guilty party was - we also reset all the variables incase they choose to play again"""

    global ready, turnCount, pause, miniPlay
    global guessNum, correctGuess, labTries

    if trueVic == "Roxy 'Big D' Warrenson" or trueVic == "'Bitsy' Elizabeth Debrevski Keyes" or trueVic == "Millicent Friendly":
        vicBlanks = ["she", "she'd", "her", "her"]
    else:  # 0      1        2     3
        vicBlanks = ["he", "he'd", "his", "him"]

    if envelope[0] == "Ms. Scarlett" or envelope[0] == "Mrs. White" or envelope[0] == "Mrs. Peacock":
        suspectBlanks = ["she", "she'd", "her", "her"]

    else:
        suspectBlanks = ["he", "he'd", "his", "him"]

    if trueVic == "Roxy 'Big D' Warrenson":
        nicName = "Roxy"
    elif trueVic == "'Bitsy' Elizabeth Debrevski Keyes":
        nicName = "Bitsy"
    elif trueVic == "Millicent Friendly":
        nicName = "Millicent"
    elif trueVic == "Elton Whitehall":
        nicName = "Elton"
    elif trueVic == "Count Francois du Bennet":
        nicName = "Count Francois"
    elif trueVic == "Baron Deitrick bon Overlitzer":
        nicName = "Baron"

    motives = [(trueVic + " saw " + envelope[0] + " trying to steal money from the safe in the basement, and when " +
                vicBlanks[0] + " realized " + vicBlanks[1] + " been caught, " + envelope[0] + " killed " + vicBlanks[
                    3]),
               (envelope[0] + " was being blackmailed by " + trueVic + " over some risky photos " + vicBlanks[
                   1] + " had taken, and killed " + nicName + " to avoid the embarrassment."),
               (envelope[
                    0] + " got extremely intoxicated and killed " + trueVic + " by accident and dragged the body out to avoid being caught."),
               (envelope[0] + " killed " + trueVic + " in order to buy " + vicBlanks[2] + " home and estate for cheap"),
               (envelope[0] + " killed " + trueVic + " because it was revealed that " + suspectBlanks[
                   2] + " partner was cheating on the killer with " + vicBlanks[3]),
               (envelope[
                    0] + " and " + trueVic + " had started an illegal drug trade together; " + trueVic + " was killed in order for " +
                envelope[0] + " to take control of the drug ring."),
               (envelope[0] + " was terminally ill and wanted to kill someone else before the sickness killed " +
                suspectBlanks[3] + ". (victim was chosen at random " + envelope[0] + " had nothing to lose)"),
               (envelope[
                    0] + " was secretly a member of a satanic cult and killed" + trueVic + " in order to ascend to the next level (" + trueVic + " was deemed a sinner due to" +
                vicBlanks[2] + " prior misconducts"),
               (envelope[
                    0] + " and " + trueVic + " were both members of rival mafia families and the killer killed " + nicName + " to avenge the death of their relative."),
               (envelope[
                    0] + " was having a bad day when " + trueVic + " decided to make a smart comment about the killer’s hair - " +
                envelope[0] + " was so upset that " + suspectBlanks[0] + " killed " + vicBlanks[3])]

    screen = pygame.display.set_mode((650, 600))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    winOrlose = Label()
    winOrlose.font = pygame.font.SysFont("Courier", 20)
    winOrlose.backcolour = (249, 54, 54)
    winOrlose.colour = (0, 0, 0)
    winOrlose.center = (325, 360)

    next = ButtonWords("Continue", 325, 500)

    motive = ButtonWords("Find out the motive by clicking here", 325, 450)

    if accusation[0] == envelope[0]:
        correctGuess.append(accusation[0])

    if accusation[1] == envelope[1]:
        correctGuess.append(accusation[1])

    if accusation[2] == envelope[2]:
        correctGuess.append(accusation[2])

    if len(correctGuess) == 3:
        winOrlose.text = ("Good Job! You guessed all 3 things correctly!!")
        # print("number of turns:",turnCount)

    elif len(correctGuess) == 2:
        winOrlose.text = ("You guessed 2 of the 3 things correctly")

    elif len(correctGuess) == 1:
        winOrlose.text = ("Sorry, you only guessed 1 of the 3 things correctly")

    elif len(correctGuess) == 0:
        winOrlose.text = ("Sorry, you didn't guess anything correctly")

    title = Label()
    title.text = ("Final Accusation")
    title.font = pygame.font.SysFont("Courier", 35)
    title.center = (325, 50)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    subtitle = Label()
    subtitle.text = ("Your Guess:")
    subtitle.center = (175, 125)
    subtitle.backcolour = (202, 249, 249)

    guess1 = Label()
    guess1.text = (accusation[0])
    guess1.center = (175, 175)
    guess1.backcolour = (255, 255, 255)

    guess2 = Label()
    guess2.text = (accusation[1])
    guess2.center = (175, 225)
    guess2.backcolour = (255, 255, 255)

    guess3 = Label()
    guess3.text = (accusation[2])
    guess3.center = (175, 275)
    guess3.backcolour = (255, 255, 255)

    ######################################################

    # this is for the text of the 3 things that were guilty

    subtitle2 = Label()
    subtitle2.text = ("The Guilty Party:")
    subtitle2.center = (425, 125)
    subtitle2.backcolour = (202, 249, 249)

    eText = Label()
    eText.text = (envelope[0])
    eText.center = (425, 175)
    eText.backcolour = (255, 255, 255)

    eText1 = Label()
    eText1.text = (envelope[1])
    eText1.center = (425, 225)
    eText1.backcolour = (255, 255, 255)

    eText2 = Label()
    eText2.text = (envelope[2])
    eText2.center = (425, 275)
    eText2.backcolour = (255, 255, 255)

    finalStatement = (
            trueVic + " was brutally murdered by " + envelope[0] + " with a " + envelope[1] + " in the " + envelope[
        2] +
            "\n\nHere's Why: " + motives[random.randint(0, 9)])

    # print(finalStatement)

    accusationText = pygame.sprite.Group(title, guess1, guess2, guess3, subtitle, motive,
                                         subtitle2, eText, eText1, eText2, winOrlose, next)

    ##################################################

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if motive.click() == True:
                    easygui.msgbox(finalStatement)
                elif next.click() == True:
                    evidence.append(envelope[
                                        0])  # adds the three things in the envelope back into the evidence so it is full again when the game starts
                    evidence.append(envelope[1])
                    evidence.append(envelope[2])
                    # print(evidence)
                    envelope.clear()  # clears the envelope so that if they play again new things are chosen
                    wrongGuess.clear()  # things guessed wrong are cleared
                    crossedOff.clear()  # notepad gets cleared
                    guess.clear()  # guess during turn is cleared
                    accusation.clear()  # final accusation cleared
                    # correctGuess.clear()
                    ready = False  # not ready for the final accusation
                    pause = False  # pause is false since they haven't entered pause yet when game begins
                    guessNum = 0  # number of guesses they have resets - they choose level again
                    labTries = 0  # number of lab tries back to zero - reset when they choose level
                    miniPlay = 0  # number of times they played minigame resets to zero
                    # turnCount = 0
                    askLeaderboard()

        accusationText.clear(screen, background)
        accusationText.update()
        accusationText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


def askLeaderboard():
    global askName, turnCount, entry, scores, score1, score2, score3, score4, score5
    global name1, name2, name3, name4, name5, leaderCheck, allScores, doneGame

    # if they won the game, they can be added to the leaderboard
    if len(correctGuess) == 3:
        choice = easygui.buttonbox("Would you like to be added to the leaderboard?", "CLUE: Murder at Mystery Mansion",
                                   choices=('yes', 'no'))
        if choice == "yes":

            allScores = []
            scoreFile = open("high_scores.txt", "r")  # makes file readable

            lines = scoreFile.readlines()
            for line in lines:  # splits everytime there's an enter
                words = line.split()
                for word in words:
                    allScores.append(word)

            # print("all scores",allScores)

            name1 = allScores[0]
            score1 = allScores[1]

            name2 = allScores[2]
            score2 = allScores[3]

            name3 = allScores[4]
            score3 = allScores[5]

            name4 = allScores[6]
            score4 = allScores[7]

            name5 = allScores[8]
            score5 = allScores[9]

            score1 = int(score1)
            score2 = int(score2)
            score3 = int(score3)
            score4 = int(score4)
            score5 = int(score5)

            scores = [(name1, score1), (name2, score2), (name3, score3), (name4, score4), (name5, score5)]

            askName = easygui.enterbox("Please enter your name: ", "CLUE: Murder at Mystery Mansion", image="hello.gif")
            turnCount = int(turnCount)
            newScore = (askName, turnCount)
            # print(newScore)
            scores.append(newScore)

            # print(score1)

            # print("all scores:", scores)

            # sorts list by the second item in the tuple (the score not the name)
            sortedList = sorted(scores, key=lambda tup: tup[1])

            # print("sorted scores", sortedList)

            set1 = sortedList[0]
            set2 = sortedList[1]
            set3 = sortedList[2]
            set4 = sortedList[3]
            set5 = sortedList[4]

            name1 = set1[0]
            score1 = set1[1]

            name2 = set2[0]
            score2 = set2[1]

            name3 = set3[0]
            score3 = set3[1]

            name4 = set4[0]
            score4 = set4[1]

            name5 = set5[0]
            score5 = set5[1]

            score1 = str(score1)
            score2 = str(score2)
            score3 = str(score3)
            score4 = str(score4)
            score5 = str(score5)

            scoreFile = open("high_scores.txt", "w")  # deletes everything in the file
            scoreFile.close()

            scoreFile = open("high_scores.txt", "a")  # makes file appendable

            # rewrites the file with only the top 5 names/scores
            scoreFile.write(name1)
            scoreFile.write("\n")
            scoreFile.write(score1)
            scoreFile.write("\n")
            scoreFile.write(name2)
            scoreFile.write("\n")
            scoreFile.write(score2)
            scoreFile.write("\n")
            scoreFile.write(name3)
            scoreFile.write("\n")
            scoreFile.write(score3)
            scoreFile.write("\n")
            scoreFile.write(name4)
            scoreFile.write("\n")
            scoreFile.write(score4)
            scoreFile.write("\n")
            scoreFile.write(name5)
            scoreFile.write("\n")
            scoreFile.write(score5)

            scoreFile = open("high_scores.txt", "r")
            # print(scoreFile.read())

            doneGame = True
            correctGuess.clear()
            leaderboard()

        elif choice == "no":
            correctGuess.clear()
            playAgain()

    else:  # they did not win the game
        correctGuess.clear()
        playAgain()


def playAgain():
    global turnCount, play2, doneGame

    screen = pygame.display.set_mode((600, 430))
    pygame.display.set_caption("CLUE: Murder at Mystery Mansion")

    background = pygame.Surface(screen.get_size())
    background.fill((227, 231, 237))
    screen.blit(background, (0, 0))

    title = Label()
    title.text = ("Would you like to play again?")
    title.font = pygame.font.SysFont("Courier", 25)
    title.center = (300, 60)
    title.colour = (255, 255, 255)
    title.backcolour = (0, 0, 0)

    yes = ButtonWords("Yes", 200, 125)
    no = ButtonWords("No", 400, 125)

    logo2 = Button(300, 300, "smallLogo.jpg")

    againText = pygame.sprite.Group(title, yes, no, logo2)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes.click() == True:
                    doneGame = False
                    turnCount = 0  # if they want to play again they go back to choose a level again
                    play2 = True
                    chooseLevel()
                elif no.click() == True:
                    print("Have a nice day")  # if they don't want to lay again they exit
                    exit()

        againText.clear(screen, background)
        againText.update()
        againText.draw(screen)

        pygame.mouse.set_visible(True)
        pygame.display.flip()


chooseLevel()
