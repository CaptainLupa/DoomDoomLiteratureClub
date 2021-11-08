init 10 python:
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
        #"What is the most attractive vacation\ndestination?": ["Auschwitz", "", "", ""],
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
        "Doomguy": ["Dammit.", "I\'ll rip and tear that shitty little heard of yours right off.", "WOW THIS IS SO NOT SEX!", "I FUCKING LOVE SUSHI", "GOD WHY CAN\'T I GET ANY BAKED BEANS AROUND HERE!!", "Dammit, this makes me want to use Purell and its record breaking 99.9 percent germ death rate."],
        "Conky": ["GRUAAAAAAAAA!!!", "I\'M DONE!", "YOU ARE.... FFUFUFICKCKIFUCKUFIKCJFOISHJDF: KLSGPIOJN H{nw}", "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!", "FUCK YOU I DON\'T HAVE ANY ANGER ISSUES", "FUCKING PLACEHOLDERRRRRRRRRRRRRRRRRRRRRRR"]
    }

    pre_round_win = {#what they say after they won a round
        "Monika": ["Let\'s fucking go!", "God that was pathetic!", "You call yourself a Doom Marine?", "Trash... Heh.", "GOTTA FUCK EM ALL", "Wow... you suck."],
        "Doomguy": ["Haha You thought you could beat me?", "All acoording to plan.", "I hate trap music.", "Easier than an Imp.", "You\'re a dissapointment", "This won\'t do, you must work harder."],
        "Conky": ["GUAAAAAAAAA!!!!", "YOU THOUGHT YOU COULD WIN!!", "I'M SO FUCKING DONE WITH YOU!", "[[Guitar Solo]]", "Clown, get the trash can!", "Ahahhah, you fucking idiot!"]
    }

    openers = {#the first thing they say
        "Monika": ["I\'ll defeat you for the good of the club!", "You\'re going down!", "I will defeat you!"],
        "Conky": ["I\'m gonna beat your fuckin ass!", "You dare try to defeat me?", "Fuck off!"],
        "Doomguy": ["I\'ll slam you like an Imp!", "There\'s no defeating me!", "I will bash your skull in!"]
    }

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

label Texas_Game_Fix(practiceRound=True):
    stop music fadeout 2.0
    scene bg hellscape
    with dissolve_scene_full
    play music rt
    call screen dialog("Welcome, to Texas Street Law!", ok_action=Return())
    call screen dialog("I conceived this while High on Crack Cocaine.", ok_action=Return())
    call screen dialog("Don't expect anything coherent.", ok_action=Return())
    python:
        # opt = talkers[Opponent][0]
        # jt = talkers[Judge][0]
        if practiceRound:
            opt = c
            jt = y
            opImg = "conkycrinkler 1a"
        else:
            opt = m
            jt = c
            opImg = "menu_art_m_NOMOVE"

        renpy.show(opImg, at_list=[t41], zorder=3)
        renpy.show("doomguy 1a", at_list=[t44], zorder=3)

        jt("Alright guys flip a coin to start the game.")

        narrator("Heads or Tails?", interact=False)
        htChoice = renpy.display_menu([("Heads", True), ("Tails", False)], interact=True, screen="choice")

        pause(1.0)

        hOrt = random.randint(1, 10)
        renpy.show("coinflip", zorder=10)
        pause(2.0)

        if hOrt <= 5:
            flip_result = True
            renpy.show("heads", zorder=10)
            hider = "heads"
        else:
            flip_result = False
            renpy.show("tails", zorder=10)
            hider = "tails"

        if flip_result and htChoice:
            jt("Doomguy wins the coin flip!")
        else:
            jt(Opponent + " won!")

        renpy.hide(hider) #Hides result image, names are hard

    if practiceRound:
        jt "Alright Let's get down to business."
        jt "I will now explain the rules to you Doomguy."
        d "Alright."
        jt "Ok so first there will be a simple round system."
    else:
        jt "fart"

    return


