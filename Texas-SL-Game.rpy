#Goes until health is depleted
#whoever wins the coin flip goes first
#Opponent has opportunity to defelct half the damage of the attck that the other selected
#Embrace the jank, don't worry too much about it being perfect its call fucking texas street law dude

init -1 python:
    import random

    QAs = {#questions for the main round loop
        "Who is the author of the\nMonogatari books?": ["Nisioisin", "JK Rowling", "Gandalf", "Brandon Sanderson"],
        "In the manga Komi-san Can\'t \nCommunicate, who is the \'MC\'?": ["Tadano", "Najimi", "Naofumi", "Big sex man"],
        "How many good episodes of SAO are there?": ["0", "5", "2", "Good?  Sao?"],
        "Who is the second JoJo?": ["Joseph Joestar", "Giorno Giovanna", "Jolyne Joestar", "jacksepticeye"],
        "Who is the best girl from monogatari?": ["Kanbaru", "Senjougahara", "Karen", "Yotsugi"],
        "What is the most popular Manga\nof all time?": ["One Piece", "JoJo's Bizarre Adventure", "Death Note", "The Rising of the \nSpear Hero"],
        "Who is the best dead\npresident of the US?": ["Abraham Lincoln", "JFK", "Zachory Taylor", "James A. Garfield"],
        "What is the best form of literature?": ["Manga", "Books", "Yuri art", "Monika\'s large thighs"],
        "Choose the best...": ["Tights", "Thigh Highs", "Knee socks", "No socks(mmm toes)"],
        "What is the best architype of girl?": ["Tomboy", "Tsundere", "Kuudere", "Yandere"],
        "What is a girls best friend?": ["Her best friend", "Hitachi Magic Wand", "BDSM", "Femdom Yuri"],
        "Who is the sexiest\nPresidential Candidate?": ["Sernie Banders", "Tonald Drump", "Boe Jiden", "Cillary Hinton"],
        "What is the most attractive vacation\ndestination?": ["Auschwitz", "", "", ""],
        "Who is the greatest Tsundere\nof all time?": ["Asuka", "Hitagi", "Taiga", "Rin"]
    }

    lightning_QA_4 = {#lightning questions with 4 answers
        "Which Persona game is the best?": ["Persona 3", "Persona 5", "Persona 5 Dancing in Starlight", "P4G"],#First item in array will always be the correct answer
        "How many dicks can Elsa\nfit in her ass?": ["Perhaps 7", "8?", "9?", "Dear god 10?"],
        "Who is the best doki?": ["Natsuki", "Monika", "Yuri", "Sayori"],
        "What, is the air-speed velocity\nof an unlaiden swollow?": ["African or European?", "69Kph", "What?", "Red no blu-AAAUAUGHHGHGAHGAHGA"],
        "Who\'s the king of the beach now?": ["Big Wheel", "Small Wheel", "Large Rotating Device", "Sex"],
        "What is Jotaro\'s stand?": ["Star Platinum", "Heirophant Green", "The Tower", "Looking cool Joker!"],
        "Who's looking cool?": ["Joker", "Lady Ann", "Feet", "Cum"]
    }

    lightning_QA_2 = {#lightning questions with 2 answers
        "True or false,\nYou are gay?": ["True", "False"],
        "But can he really dance?": ["Yes", "No"],
        "Just": ["Monika", "Thicc ass lolis"],
        "Natsuki is god.": ["True", "False"],
        "Bernie Sanders Fucks.": ["True", "False"],
        "Tomboys are the greatest\ninvention of all time.": ["Yes", "No"],
        "Tsundere's are adorable": ["True", "False"],
        "Rei from EVA is a\nKuudere": ["True", "False"],
        "Manga is literature.": ["True", "False"]
    }

    pre_round_lose = {#what opponents and the player say after they lost a round
        "Monika": ["Ugh!", "So close!", "I had that!", "...Don\'t look at me, trash.", "God... this is bullshit.", "Grrr, I\'m gonna fuck you to death later."],
        "Yuri": ["...", "G-Good job Doomguy...", "I won\'t let you get it that easily this time!", "Oh no... what will Natsuki think?", "This is bad.", "Haaah, this isn\'t good!"],
        "Doomguy": ["Dammit.", "I\'ll rip and tear that shitty little heard of yours right off.", "WOW THIS IS SO NOT SEX!", "I FUCKING LOVE SUSHI", "GOD WHY CAN\'T I GET ANY BAKED BEANS AROUND HERE!!", "Dammit, this makes me want to use Purell and its record breaking 99.9 percent germ death rate."],
        "Conky": ["GRUAAAAAAAAA!!!", "I\'M DONE!", "YOU ARE.... FFUFUFICKCKIFUCKUFIKCJFOISHJDF: KLSGPIOJN H{nw}", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!", "FUCK YOU I DON\'T HAVE ANY ANGER ISSUES", "FUCKING PLACEHOLDERRRRRRRRRRRRRRRRRRRRRRR"]
    }

    pre_round_win = {#what they say after they won a round
        "Monika": ["Let\'s fucking go!", "God that was pathetic!", "You call yourself a Doom Marine?", "Trash... Heh.", "GOTTA FUCK EM ALL", "Wow... you suck."],
        "Yuri": ["Natsuki are you proud of me?", "Oh yeah take that!  I mean uh, hehe, I\'m sure you\'ll do better next time.", "HHH I\'LL STAB YOU", "Good try, but you just can\'t beat me.(SMUG)", "Hmm, maybe I\'ll read a book after this borefest", "Natsuki would be dissapointed in you."],
        "Doomguy": ["Haha You thought you could beat me?", "All acoording to plan.", "I hate trap music.", "Easier than an Imp.", "You\'re a dissapointment", "This won\'t do, you must work harder."],
        "Conky": ["GUAAAAAAAAA!!!!", "YOU THOUGHT YOU COULD WIN!!", "I'M SO FUCKING DONE WITH YOU!", "[[Guitar Solo]]", "Clown, get the trash can!", "Ahahhah, you fucking idiot!"]
    }

    openers = {#the first thing they say
        "Monika": ["I\'ll defeat you for the good of the club!", "You\'re going down!", "I will defeat you!"],
        "Yuri": ["I\'m only doing this for Natsuki!", "Ehh, good luck, I guess.", "I\'ll do it if Natsuki wills it!"],
        "Conky": ["I\'m gonna beat your fuckin ass!", "You dare try to defeat me?", "Fuck off!"],
        "Doomguy": ["I\'ll slam you like an Imp!", "There\'s no defeating me!", "I will bash your skull in!"]
    }

    full_questions = []#arrays
    I_answers = []#create answers list
    L_questions2 = []
    L_questions4 = []
    Doomguy_loss = []
    Monika_loss = []
    Yuri_loss = []
    Conky_loss = []
    Doomguy_win = []
    Monika_win = []
    Yuri_win = []
    Conky_win = []
    Monika_openers = []
    Yuri_openers = []
    Conky_openers = []
    Doomguy_default_o = []
    Doomguy_s_openers = [
        "This club\'s no good anymore!",
        "Good luck?  That\'s what I should be saying!",
        "NO YOU FUCK OFF!"
    ]
    Doomguy_otl = [
        "Wow you\'re dumb.",
        "That made me wanna blow my brains out.",
        "God that was painful."
    ]
    attacks = [
        "Aikido Kick",
        "Taekwondo Chop",
        "The Fucking Gun",
        "Sex Attack"
    ]

    for i in QAs:
        full_questions.append(i)

    for i in lightning_QA_2:
        L_questions2.append(i)

    for i in lightning_QA_4:
        L_questions4.append(i)

    for i in range(6):
        Doomguy_loss.append(pre_round_lose["Doomguy"][i])
        Monika_loss.append(pre_round_lose["Monika"][i])
        Yuri_loss.append(pre_round_lose["Yuri"][i])
        Conky_loss.append(pre_round_lose["Conky"][i])

    for i in range(6):
        Doomguy_win.append(pre_round_win["Doomguy"][i])
        Monika_win.append(pre_round_win["Monika"][i])
        Yuri_win.append(pre_round_win["Yuri"][i])
        Conky_win.append(pre_round_win["Conky"][i])

    for i in range(3):
        Monika_openers.append(openers["Monika"][i])
        Yuri_openers.append(openers["Yuri"][i])
        Conky_openers.append(openers["Conky"][i])
        Doomguy_default_o.append(openers["Doomguy"][i])

    JumpL = ''
    Judge = ""
    Opponent = ""
    Boss = ""
    Sus = ""
    Jad = ""
    which_answer = 0
    round = 1#round number
    round_s = str(round)
    opH = 100#opponent health
    selfH = 100#player health
    opH_s = ""
    selfH_s = ""
    Heads = False #heads or tails
    Tails = False
    ystart = 250
    L24 = ""
    L2 = False
    L4 = False
    time = 5
    timer_range = 0
    timer_jump = ""
    dmg = 0#Damgae int
    dmg_s = ""#Damage as a string
    wrong_answers = []
    gets_Right = 0
    C_answer_shown = False
    first_H_show = True
    winner = ""
    tights = False#a specific question was asked
    current_q = ""

    last_round_win = False#won the last round
    lightning_win = False
    player_turn = False
    op_lightning_win = False
    op_total_loss = False

    M_Boss = False

    def who_win():
        return winner



label reset_texas_vars:
    python:
        JumpL = ''
        Judge = ""
        Opponent = ""
        Boss = ""
        Sus = ""
        Jad = ""
        which_answer = 0
        round = 1#round number
        round_s = str(round)
        opH = 100#opponent health
        selfH = 100#player health
        opH_s = ""
        selfH_s = ""
        Heads = False #heads or tails
        Tails = False
        ystart = 250
        L24 = ""
        L2 = False
        L4 = False
        time = 5
        timer_range = 0
        timer_jump = ""
        dmg = ""#Damgae int
        dmg_s = str(dmg)
        wrong_answers = []
        gets_Right = 0
        C_answer_shown = False
        first_H_show = True
        winner = ""
        tights = False#a specific question was asked
        current_q = ""
        last_round_win = False#won the last round
        lightning_win = False
        player_turn = False
        op_lightning_win = False
        op_total_loss = False
        M_Boss = False

    return


image opH_d = ParameterizedText(style="texasgame_text", xalign=0.10, yalign=0.10)

image selfH_d = ParameterizedText(style="texasgame_text", xalign=0.86, yalign=0.10)

image coinflip:
    truecenter
    "mod_assets/heads.png"
    pause 0.25
    "mod_assets/tailes.png"
    pause 0.25
    repeat 50

image heads:
    truecenter
    "mod_assets/heads.png"

image tails:
    truecenter
    "mod_assets/tailes.png"


label Texas_Game(Judge="", Opponent="", JumpL='', M_Boss=None):
    stop music fadeout 2.0
    scene bg hellscape
    with dissolve_scene_full
    play music rt
    call screen dialog("It\'s time to dddddddddduel!!!!", ok_action=Return())
    call screen dialog("Today you are facing " + Opponent + "\nunder the supervision of judge " + Judge + ".", ok_action=Return())
    python:
        if Opponent == "Monika":#sets opponent speaking var
            Sus = m
        elif Opponent == "Yuri":
            Sus = y
        elif Opponent == "Conky Crinkler":
            Sus = c

        if Judge == "Conky Crinkler":#sets judge speaking var, idk why i chose Jad but I did
            Jad = c
        elif Judge == "Yuri":
            Jad = y
        elif Judge == "Monika":
            Jad = m

        if Opponent == "Monika":#show opponent and player art
            renpy.show("menu_art_m_NOMOVE", at_list=[t41], zorder=3)
        elif Opponent == "Yuri":
            renpy.show("menu_art_y_NOMOVE", at_list=[t41], zorder=3)
        elif Opponent == "Conky Crinkler":
            renpy.show("conkycrinkler 1a", at_list=[t41], zorder=3)
        renpy.show("doomguy 1a", at_list=[t44], zorder=3)

        renpy.say(Jad, "FLIP THE COIN, AND OFF TO THE RESCUE!")

        narrator("Heads or tails?", interact=False)
        UHT = renpy.display_menu([("Heads", "Heads"), ("Tails", "Tails")], interact=True, screen="choice")#lets the player select heads or tails

        pause(1.0)

        H_or_T = random.randint(1, 10)
        renpy.show("coinflip", zorder=10)#show coin flip "animation"
        pause(2)
        renpy.hide("coinflip")
        if H_or_T <= 5:
            Heads = True
            renpy.show("heads", zorder=10)
        elif H_or_T >= 6:
            Tails = True
            renpy.show("tails", zorder=10)

        if UHT == "Heads" and Heads == True:#set who goes first
            renpy.say(Jad, "Doomguy won!!")
            player_turn = True
        elif UHT == "Heads" and not Heads:
            renpy.say(Jad, Opponent + " won!!")
            player_turn = False
        elif UHT == "Tails" and Tails:
            renpy.say(Jad, "Doomguy won!!")
            player_turn = True
        elif UHT == "Tails" and not Tails:
            renpy.say(Jad, Opponent + " won!!")
            player_turn = False

        if Heads:
            renpy.hide("heads")
        else:
            renpy.hide("tails")

    jump Rounds
    return#not sure if i need this but im scared to change it



label Rounds:
    python:
        if selfH > 0 and opH > 0:#if opponent or player still have health keep going
            ui.text("ROUND " + round_s + "!", style="texasgame_large_text", xpos=500, ypos=360)
            pause(3)
            ui.text("FIGHT!", style="texasgame_large_text", xpos=530, ypos=360)
            pause(3)
            d_resp = random.choice(Doomguy_loss)
            d_win = random.choice(Doomguy_win)
            d_otl = random.choice(Doomguy_otl)
            if Opponent == "Monika":#set responses to winning/losing
                response = random.choice(Monika_loss)
                winnd = random.choice(Monika_win)
                opener = random.choice(Monika_openers)
                d_opener = random.choice(Doomguy_default_o)
                if opener == Monika_openers[0]:
                    d_opener = Doomguy_s_openers[0]
            elif Opponent == "Yuri":
                response = random.choice(Yuri_loss)
                winnd = random.choice(Yuri_win)
                opener = random.choice(Yuri_openers)
                d_opener = random.choice(Doomguy_default_o)
                if opener == Yuri_openers[1]:
                    d_opener = Doomguy_s_openers[1]
            elif Opponent == "Conky Crinkler":
                response = random.choice(Conky_loss)
                winnd = random.choice(Conky_win)
                opener = random.choice(Conky_openers)
                d_opener = random.choice(Doomguy_default_o)
                if opener == Conky_openers[2]:
                    d_opener = Doomguy_s_openers[2]

            #What the opponent and player characters say at the beginning of the game.
            if round == 1:#say opening line at start of game
                renpy.say(Sus, opener)
                renpy.say(d, d_opener)
            elif last_round_win and not op_lightning_win and Opponent == "Monika":#player won the last round totally
                renpy.hide("menu_art_m_NOMOVE")
                renpy.show("menu_art_m_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif last_round_win and not op_lightning_win and Opponent == "Yuri":
                renpy.hide("menu_art_y_NOMOVE")
                renpy.show("menu_art_y_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif last_round_win and not op_lightning_win and Opponent == "Conky Crinkler":
                renpy.hide("conkycrinkler 1a")
                renpy.show("conkycrinkler 1a", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif not last_round_win and op_lightning_win and Opponent == "Monika":#opponent won the lightning round
                renpy.hide("menu_art_m_NOMOVE")
                renpy.show("menu_art_m_NOMOVE", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
            elif not last_round_win and op_lightning_win and Opponent == "Yuri":
                renpy.hide("menu_art_y_NOMOVE")
                renpy.show("menu_art_y_NOMOVE", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
            elif not last_round_win and op_lightning_win and Opponent == "Conky Crinkler":
                renpy.hide("conkycrinkler 1a")
                renpy.show("conkycrinkler 1a", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
            elif not last_round_win and lightning_win and Opponent == "Monika":#Player won the lightning round
                renpy.hide("menu_art_m_NOMOVE")
                renpy.show("menu_art_m_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif not last_round_win and lightning_win and Opponent == "Yuri":
                renpy.hide("menu_art_y_NOMOVE")
                renpy.show("meny_art_y_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif not last_round_win and lightning_win and Opponent == "Conky Crinkler":
                renpy.hide("conkycrinkler 1a")
                renpy.show("conkycrinkler 1a", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_win)
            elif not last_round_win and not lightning_win and op_total_loss and Opponent == "Monika":#opponent lost last round totally
                renpy.hide("menu_art_m_NOMOVE")
                renpy.show("menu_art_m_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_otl)
            elif not last_round_win and not lightning_win and op_total_loss and Opponent == "Yuri":
                renpy.hide("menu_art_y_NOMOVE")
                renpy.show("menu_art_y_NOMOVE", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_otl)
            elif not last_round_win and not lightning_win and op_total_loss and Opponent == "Cony Crinkler":
                renpy.hide("conkycrinkler 1a")
                renpy.show("conkycrinkler 1a", at_list=[aO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[hP], zorder=3)
                renpy.say(Sus, response)
                renpy.say(d, d_otl)
            elif not last_round_win and not lightning_win and not op_total_loss and Opponent == "Monika":#Player lost
                renpy.hide("menu_art_m_NOMOVE")
                renpy.show("menu_art_m_NOMOVE", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
            elif not last_round_win and not lightning_win and not op_total_loss and Opponent == "Yuri":
                renpy.hide("menu_art_y_NOMOVE")
                renpy.show("menu_art_y_NOMOVE", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
            elif not last_round_win and not lightning_win and not op_total_loss and Opponent == "Conky Crinkler":
                renpy.hide("conkycrinkler 1a")
                renpy.show("conkycrinkler 1a", at_list=[hO], zorder=3)
                renpy.hide("doomguy 1a")
                renpy.show("doomguy 1a", at_list=[aP], zorder=3)
                renpy.say(Sus, winnd)
                renpy.say(d, d_resp)
        elif selfH <= 0 or opH <= 0:#determin who is the winner
            renpy.jump('Wank')

    $ opH_s = str(opH)
    $ selfH_s = str(selfH)

    if first_H_show == True:#dissolve in health
        show opH_d "[opH_s]" with Dissolve(0.50, alpha=True)
        show selfH_d "[selfH_s]" with Dissolve(0.50, alpha=True)
        $ first_H_show = False
    else:#just show health
        hide opH_d
        hide selfH_d
        show opH_d "[opH_s]"
        show selfH_d "[selfH_s]"

    jump Op_N


label Op_N:#Main game loop
    if player_turn:
        python:
            current_q = random.choice(full_questions)#set current question
            answer = QAs[current_q][0]#set answer
            I_answers = []
            I_answers.append(QAs[current_q][1])#add incorrect answers to array
            I_answers.append(QAs[current_q][2])
            I_answers.append(QAs[current_q][3])
            which_answer = random.randint(0, 1)
            C_answer_shown = False
            renpy.say(Jad, "Alright, let's go.")
            if round == 1:
                renpy.say(Jad, "Doomguy! You're up first!")
            else:
                renpy.say(Jad, "Doomguy!  You're up!")

            ui.text(current_q, style="texasgame_text", xpos=420, ypos=105)#display current question

            for j in range(2):#Two vertical stacks of answers
                if j == 0: x = 430
                else: x = 670
                ui.vbox()#vbox for stacking
                for i in range(2):
                    if i == which_answer and C_answer_shown == False:#shows the answer at a random location
                        option = answer
                        C_answer_shown = True
                    else:
                        option = random.choice(I_answers)
                        I_answers.remove(option)
                    ui.textbutton(option, clicked=ui.returns(option), xpos=x, ypos=i * 56 + ystart)
                ui.close()

            t = ui.interact()#click
            if t == answer:#player got answer correct
                renpy.say(d, answer + "!")
                if current_q == "Choose the best...":
                    renpy.say(Jad, "That\'s right!")
                    renpy.say(Jad, "Tights are the best!")
                    renpy.say(Jad, "PLUS POINTS!!(+10HP)")
                    selfH+=10
                    selfH_s = str(selfH)
                else:
                    renpy.say(Jad, "Correct!")

                renpy.say(Jad, "Please choose attack!")

                ui.text("Attacks!", style="texasgame_text", xpos=550, ypos=150)

                for j in range(2):
                    if j == 0: x = 430
                    else: x = 670
                    ui.vbox()
                    for i in range(2):
                        option = random.choice(attacks)
                        attacks.remove(option)
                        ui.textbutton(option, clicked=ui.returns(option), xpos=x, ypos=i * 56 + ystart)#show attack selections
                    ui.close()

                attacks = [
                    "Aikido Kick",
                    "Taekwondo Chop",
                    "The Fucking Gun",
                    "Sex Attack"
                ]

                atk = ui.interact()
                if atk == "Aikido Kick":#sets attacks and damage
                    renpy.say(d, "I select Aikido Kick!")
                    dmg = 16
                    dmg_s = str(dmg)
                elif atk == "Taekwondo Chop":
                    renpy.say(d, "I select Taekwondo Chop!")
                    dmg = 16
                    dmg_s = str(dmg)
                elif atk == "The Fucking Gun":
                    renpy.say(d, "I chooose the fucking gun!")
                    dmg = 30
                    dmg_s = str(dmg)
                elif atk == "Sex Attack":
                    renpy.say(d, "I shall suck your cock!")
                    dmg = 40
                    dmg_s = str(dmg)

                renpy.say(Jad, "Alrighty!  " + Opponent + ", you have a chance to turn this around!")


        if t == answer:#calls the lightning label
            hide selfH_d
            show selfH_d "[selfH_s]"
            $ ui.text("PLUS POINTS", style="texasgame_text", xpos=590, ypos=360)
            $ pause(1.5)
            call Op_Lightning

            if op_lightning_win:#if opponent wins lightning round, player will take half the damage of his/her selected attack
                python:
                    dmg/=2#div damage
                    dmg_s = str(dmg)#set damage string
                    renpy.say(Jad, "Congrats " + Opponent +", you won the lightning round, half the damage that would\'ve been dealt to you will be given to Doomguy.")
                    ui.text("Doomguy takes \n" + dmg_s + " damage!!", style="texasgame_large_text", xpos=475, ypos=360)
                    pause(3)
                    selfH-=dmg#subtract from health
                    selfH_s = str(selfH)#set string
                    dmg = 0#reset damage
                    dmg_s = ""
                    player_turn = False#Player lost, so they do not go next round
                    last_round_win = False
                    I_answers = []#reset answers
                    answer = ""#reset answer
                    round+=1#advance round number
                    round_s = str(round)#set string
                hide selfH_d
                show selfH_d "[selfH_s]"#show health
                jump Rounds#go back to round loop
            elif not op_lightning_win:#opponent lost lightning, so they take full damage of attack
                python:
                    dmg_s = str(dmg)
                    renpy.say(Jad, "OOOOhhhhh ohoho noooo, " + Opponent + " that was badddd.")
                    renpy.say(Jad, "You\'re getting full damage.")
                    ui.text(Opponent + " takes \n" + dmg_s + " damage!!", style="texasgame_large_text", xpos=495, ypos=360)
                    pause(3)
                    opH-=dmg#subtract damage from health
                    opH_s = str(opH)
                    dmg = 0#reset damage
                    dmg_s = ""
                    player_turn = True#player turn next round
                    last_round_win = True
                    I_answers = []#reset answers
                    answer = ""
                    round+=1#advance round
                    round_s = str(round)
                hide opH_d
                show opH_d "[opH_s]"#show health
                jump Rounds#back to round loop
        elif t != answer:#player got question wrong
            python:
                if current_q == "Choose the best...":
                    tights = True
                    renpy.say(Jad, "Oho, nonononono, TIGHTS ARE THE BETS YOU FOOL, NOT " + t + "!!")
                    renpy.say(Jad, "Minus points!")
                    ui.text("MINUS POINTS!", style="texasgame_text", xpos=640, ypos=360)
                    selfH-=10
                    selfH_s = str(selfH)
                    renpy.say(Jad, Opponent + ", anything to say?")
                else:
                    renpy.say(Jad, "OHO!!!  I\'m so sorry Doomguy, but that is not correct.")
                    renpy.say(Jad, Opponent + ", do you have anything to say to him?")

                say_something = random.randint(1, 20)

                if say_something >= 15:
                    renpy.say(Sus, "Yare yare...")
                    renpy.say(Sus, "What a degenerate.")
                else:
                    renpy.say(Sus, "...")
                    renpy.say(Jad, "Alright then!  Moving on the next round!")

                player_turn = False
                last_round_win = False
                op_total_loss = False
                I_answers = []
                answer = ""
                round+=1
                round_s = str(round)
                current_q = ""

            if tights:
                $ tights = False
                hide selfH_d
                show selfH_d "[selfH_s]"

            jump Rounds#no damage is done, advanes to next round and opponent goes
    elif not player_turn:#opponents turn
        python:
            current_q = random.choice(full_questions)#current question is set from the questions list defined at beginning of python block
            answer = QAs[current_q][0]#the answer to current_q
            I_answers = []
            C_answer_shown = False
            which_answer = random.randint(0, 1)
            I_answers.append(QAs[current_q][1])
            I_answers.append(QAs[current_q][2])
            I_answers.append(QAs[current_q][3])
            renpy.say(Jad, Opponent + ", this question is for you!")
            renpy.say(Jad, current_q)

            for j in range(2):#Two vertical stacks of answers
                if j == 0: x = 430
                else: x = 670
                ui.vbox()#vbox for stacking
                for i in range(2):
                    if i == which_answer and not C_answer_shown:#shows the answer at a random location
                        option = answer
                        C_answer_shown = True
                    else:
                        option = random.choice(I_answers)
                        I_answers.remove(option)
                    ui.text(option, xpos=x, ypos=i * 56 + ystart)
                ui.close()

            gets_Right = ""
            gets_Right = random.randint(1, 100)#below 25 = correct, above = incorrect, 75% chance of incorrect, for player advantage

            I_answers = []
            I_answers.append(QAs[current_q][1])
            I_answers.append(QAs[current_q][2])
            I_answers.append(QAs[current_q][3])

        if gets_Right <= 25:#opponent got question correct
            python:
                renpy.say(Sus, answer + "!")
                renpy.say(Jad, "Correct!")
                renpy.say(Jad, "Please choose which attack you would like to perform.")

                atk = random.randint(1, 4)#randomly select attack

                ui.text("Attacks!", style="texasgame_text", xpos=550, ypos=80)

                for j in range(2):
                    if j == 0: x = 430
                    else: x = 670
                    ui.vbox()
                    for i in range(2):
                        option = random.choice(attacks)
                        attacks.remove(option)
                        ui.text(option, xpos=x, ypos=i * 56 + ystart)#show attack selections
                    ui.close()

                attacks = [
                    "Aikido Kick",
                    "Taekwondo Chop",
                    "The Fucking Gun",
                    "Sex Attack"
                ]

                if atk == 1:
                    renpy.say(Sus, "I select Aikido Kick!")
                    dmg = 16
                    dmg_s = str(dmg)
                elif atk == 2:
                    renpy.say(Sus, "I select Taekwondo Chop!")
                    dmg = 16
                    dmg_s = str(dmg)
                elif atk == 3:
                    renpy.say(Sus, "I chooose the fucking gun!")
                    dmg = 30
                    dmg_s = str(dmg)
                elif atk == 4:
                    renpy.say(Sus, "I shall suck your cock!")
                    dmg = 40
                    dmg_s = str(dmg)

                renpy.say(Jad, "Alright, Doomguy, you have a chance to retaliate, please choose the correct answer to this question")

                I_answers = []
                answer = ""
                current_q = ""

            call Lightning#player lightning round is called

            if lightning_win == True:#player won the lightning round
                python:
                    dmg/=2#div the damage
                    dmg_s = str(dmg)#set the string
                    renpy.say(Jad, "Congrats Doomguy, you won the lightning round, " + Opponent + " will recieve half of the damage that they would\'ve given you!")
                    ui.text(Opponent + " takes \n" + dmg_s + " damage!", style="texasgame_large_text", xpos=475, ypos=360)
                    pause(3)
                    opH-=dmg#subtract from health
                    opH_s = str(opH)#set health string
                    dmg = 0#resset damage
                    dmg_s = ""
                    player_turn = True
                    I_answers = []
                    answer = ""
                    round+=1#advance round
                    round_s = str(round)
                hide opH_d
                show opH_d "[opH_s]"#show opponent health
                jump Rounds#back to round loop
            elif lightning_win == False:#Player lost lightning round
                python:
                    renpy.say(Jad, "Doomguy, you have failed the lightning round, you will take full damage.")
                    ui.text("Doomguy takes \n" + dmg_s + " damage!", style="texasgame_large_text", xpos=475, ypos=360)
                    pause(3)
                    selfH-=dmg#subtract health
                    selfH_s = str(selfH)
                    dmg = 0#reset damage and string
                    dmg_s = ""
                    player_turn = False#player does not go next round
                    I_answers = []#reset array
                    answer = ""
                    round+=1#advance round counter
                    round_s = str(round)
                hide selfH_d
                show selfH_d "[selfH_s]"#show updated health
                jump Rounds#go back to round loop
        elif gets_Right >= 26:#opponent got it wrong
            python:
                WA = random.choice(I_answers)
                renpy.say(Sus, WA + "!")
                renpy.say(Jad, "Nope!")
                renpy.say(Jad, "Sadly, that is incorrect, moving on to the next round!")
                I_answers = []
                player_turn = True#player goes next round
                last_round_win = False#player did not win but the op lost so last_round_win is set to false
                op_total_loss = True#a total loss on the opponents part
                answer = ""
                round+=1#advance round counter
                round_s = str(round)

            jump Rounds


label Op_Lightning:#opponent lightning round
    python:
        L24 = random.randint(1, 10)#L24 is used to determin if a 4 answer or a 2 answer question will be used
        L2 = False
        L4 = False
        current_q = ""

        if L24 <= 5:
            current_q = random.choice(L_questions2)
            answer = lightning_QA_2[current_q][0]#set answer and wrong answer
            Wr_A = lightning_QA_2[current_q][1]
            L2 = True
            L_gets_Right = random.randint(1, 100)#determins if op gets it right
        elif L24 >= 6:
            current_q = random.choice(L_questions4)
            answer = lightning_QA_4[current_q][0]#set answer and wrong answers
            wr1 = lightning_QA_4[current_q][1]
            wr2 = lightning_QA_4[current_q][2]
            wr3 = lightning_QA_4[current_q][3]
            L4 = True
            L_gets_Right = random.randint(1, 100)#determins if op gets it right

        pause(0.75)

        ui.text(current_q, style="texasgame_text", xpos=500, ypos=250)#display question

        time = 5#timer for 5 seconds
        timer_range = 5#range for the bar, I think its for a linear command, idk i just copied it from the renpy wiki
        timer_jump = 'Too_slow'#where the timer would go if it finsihed
        where_correct2 = random.randint(1, 2)
        where_correct4 = random.randint(1, 4)

        #add displayed answers
        if where_correct2 == 1 and L2:
            ui.text(answer, xpos=480, ypos=306)
            ui.text(Wr_A, xpos=480, ypos=362)
        elif where_correct2 == 2 and L2:
            ui.text(Wr_A, xpos=480, ypos=306)
            ui.text(answer, xpos=480, ypos=362)
        elif where_correct4 == 1 and L4:
            ui.text(answer, xpos=480, ypos=306)
            ui.text(wr1, xpos=480, ypos=362)
            ui.text(wr2, xpos=720, ypos=306)
            ui.text(wr3, xpos=720, ypos=362)
        elif where_correct4 == 2 and L4:
            ui.text(wr1, xpos=480, ypos=306)
            ui.text(answer, xpos=480, ypos=362)
            ui.text(wr2, xpos=720, ypos=306)
            ui.text(wr3, xpos=720, ypos=362)
        elif where_correct4 == 3 and L4:
            ui.text(wr1, xpos=480, ypos=306)
            ui.text(wr2, xpos=480, ypos=362)
            ui.text(answer, xpos=720, ypos=306)
            ui.text(wr3, xpos=720, ypos=362)
        elif where_correct4 == 4 and L4:
            ui.text(wr3, xpos=480, ypos=306)
            ui.text(wr1, xpos=480, ypos=362)
            ui.text(wr2, xpos=720, ypos=306)
            ui.text(answer, xpos=720, ypos=362)

    show screen countdown#show timer bar

    $ p_int = random.randint(1, 4)

    $ pause(p_int)

    if L_gets_Right <= 25:
        hide screen countdown
        python:
            renpy.say(Sus, answer + "!!")
            op_lightning_win = True
            last_round_win = False
            player_turn = False
            L24 = 0
    elif L_gets_Right >= 26:
        hide screen countdown
        python:
            op_lightning_win = False

            if L2:
                answer = lightning_QA_2[current_q][1]
            elif L4:
                answer = lightning_QA_4[current_q][random.randint(1, 3)]

            renpy.say(Sus, answer + "!!")
            last_round_win = True
            player_turn = True
            L24 = 0

    python:#reset lightning vars
        L2 = False
        L4 = False
        wr1 = ""
        wr2 = ""
        wr4 = ""
        answer = ""
        Wr_A = ""
        L_gets_Right = ""
        current_q = ""

    return#back to Op_N



label Lightning:
    python:
        L24 = random.randint(1, 10)
        current_q = ""

        if L24 <= 5:#2 option questions
            current_q = random.choice(L_questions2)
            answer = lightning_QA_2[current_q][0]
            F_answer1 = lightning_QA_2[current_q][1]
            L2 = True
        elif L24 >= 6:#4 option questions
            current_q = random.choice(L_questions4)
            answer = lightning_QA_4[current_q][0]
            F_answer1 = lightning_QA_4[current_q][1]
            F_answer2 = lightning_QA_4[current_q][2]
            F_answer3 = lightning_QA_4[current_q][3]
            L4 = True

        renpy.say(Jad, "LIGHTNING ROUND!!")

        ui.text(current_q, style="texasgame_text", xpos=500, ypos=80)

        time = 5
        timer_range = 5
        timer_jump = 'Too_slow'
        where_correct4 = random.randint(1, 4)
        where_correct2 = random.randint(1, 2)
        L24 = ""

    #End of python block
    show screen countdown
    #if player does not make a choice within five seconds, program jumps to label 'Too_slow'
    if L4 == True and L2 == False:
        if where_correct4 == 1:
            menu:
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct!")
                    $ lightning_win = True
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "Now that just ain\'t right!")
                    $ lightning_win = False
                "[F_answer2]":
                    hide screen countdown
                    $ renpy.say(Jad, "Now that just ain\'t right!")
                    $ lightning_win = False
                "[F_answer3]":
                    hide screen countdown
                    $ renpy.say(Jad, "Now that just ain\'t right!")
                    $ lightning_win = False
        elif where_correct4 == 2:
            menu:
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "NEIN")
                    $ lightning_win = False
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct!")
                    $ lightning_win = True
                "[F_answer2]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope")
                    $ lightning_win = False
                "[F_answer3]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope")
                    $ lightning_win = False
        elif where_correct4 == 3:
            menu:
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[F_answer2]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct")
                    $ lightning_win = True
                "[F_answer3]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
        elif where_correct4 == 4:
            menu:
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[F_answer2]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[F_answer3]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct!")
                    $ lightning_win = True
    elif L2 == True and L4 == False:
        if where_correct2 == 1:
            menu:
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct!")
                    $ lightning_win = True
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
        elif where_correct2 == 2:
            menu:
                "[F_answer1]":
                    hide screen countdown
                    $ renpy.say(Jad, "Nope!")
                    $ lightning_win = False
                "[answer]":
                    hide screen countdown
                    $ renpy.say(Jad, "Correct!")
                    $ lightning_win = True
    python:
        if lightning_win:
            last_round_win = True
            lightning_win = True
        elif not lightning_win:
            last_round_win = False
            lightning_win = False
        L2 = False
        L4 = False
        where_correct2 = ""
        where_correct2 == ""
        answer = ""
        F_answer1 = ""
        F_answer2 = ""
        F_answer3 = ""
        current_q = ""

    return


label Too_slow:#for when the player fails to answer lightning questions fast enough.
    python:
        renpy.say(Jad, "TOOO SLOOWWWWWW!!!")
        renpy.say(Jad, "Doomguy, you recieve full damage!")
        ui.text("Doomguy takes \n" + dmg_s + " damage!", style="texasgame_text", xpos=475, ypos=360)
        pause(3)
        selfH-=dmg
        selfH_s = str(selfH)
        dmg = 0
        dmg_s = ""
        I_answers = []
        answer = ""
        player_turn = False
        last_round_win = False
        round+=1
        round_s = str(round)
    hide selfH_d
    show selfH_d "[selfH_s]"
    jump Rounds


label Wank:
    hide opH_d
    hide selfH_d
    stop music
    if selfH <= 0:
        Jad "STTOOOOOP!"
        Jad "The game has ended, Doomguy has been edged down to 0 health!"
        Jad "[Opponent] has won!"
        if M_Boss:
            m "Serves you right, glitch."
            d "I\'ll show you next time!"
            m "Oh really?"
            m "Well this terminal Says otherwise!"
            call updateconsole("sudo del_all()", "Are you sure?(y/n)")
            call updateconsole("y", "Deleting...")
            call updateconsolehistory("Done...")
            hide menu_art_m_NOMOVE
            hide doomguy
            scene black with dissolve_scene_full
            $ pause(2)
            menu:
                "Retry?"

                "Yes":
                    call updateconsole("Haha, I\'d like to see you try again!")
                    $ pause(1.5)
                    call hideconsole
                    call reset_texas_vars
                    jump M_fight
                "No":
                    menu:
                        "Are you sure?"

                        "Yes":
                            show sayori 5a at t11 zorder 3
                            s "Ok, I hope you come back!"
                            $ pause(1)
                            $ renpy.quit(relaunch=False, status=0, save=True)
                        "No":
                            show sayori 4q at t11 zorder 3
                            s "Whew, I though I was gonna have to punch you dummy!"
                            jump M_fight
        else:
            if Opponent == "Yuri":
                y "S-sorry, but I\'ve had a lot more practice than you at this..."
                y "You\'ll do better next time, I know it!"
                d "Thanks Yuri."
                d "I\'ll do my best."
                $ pause(1.2)
                hide menu_art_y_NOMOVE
                hide doomguy
                scene black with dissolve_scene_full
                $ pause(1)
                menu:
                    "Retry?"

                    "Yes":
                        call reset_texas_vars
                        call Texas_Game("Conky Crinkler", "Yuri", 'Gloom', False)
                    "No":
                        menu:
                            "You sure?"

                            "Yes":
                                show sayori 1c at t11 zorder 3
                                s "Ok, I know you\'ll get em next time!"
                                s "I love you no matter what!"
                                $ pause(1)
                                call reset_texas_vars
                                hide sayori
                                $ renpy.quit(relaunch=False, status=0, save=True)
                            "No":
                                show sayori 4s at t11 zorder 3
                                s "I knew you\'d pull through!!"
                                $ pause(2)
                                call reset_texas_vars
                                hide sayori
                                call Texas_Game("Conky Crinkler", "Yuri", 'Gloom', False)
            else:
                c "You fucking retard, I though we were through this whole losing thing."
                c "You\'re nothing but dirt!"
                hide doomguy
                hide conkycrinkler
                scene black with dissolve_scene_full
                $ pause(1.5)
                menu:
                    "Retry?"

                    "Yes":
                        call reset_texas_vars
                        call Texas_Game("Yuri", "Conky Crinkler", 'Gloom', False)
                    "No":
                        menu:
                            "You sure?"

                            "Yes":
                                show sayori 1c at t11 zorder 3
                                s "That\'s ok!"
                                s "I Still love you!"
                                $ pause(2)
                                call reset_texas_vars
                                hide sayori
                                $ renpy.quit(relaunch=False, status=0, save=True)
                            "No":
                                show sayori 4s at t11 zorder 3
                                s "That\'s right, Go get em!"
                                $ pause(1)
                                call reset_texas_vars
                                hide sayori
                                call Texas_Game("Yuri", "Conky Crinkler", 'Gloom', False)
    elif opH <= 0:
        Jad "STOOOOP!!!"
        Jad "Doomguy is the winner!"
        Jad "[Opponent] has been edged down to 0 health!"
        d "Alright!"
        jump JumpL



transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.
