image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label Doom:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "Outside Sayori's room, I knock on her door."
    d "Sayori?"
    d "Wake up, dummy..."
    "There's no response."
    "I really didn't want to have to enter her room like this..."
    "Isn't it kind of a breach of privacy?"
    "But she really leaves me no choice."
    "I gently open the door."
    d "{cps=30}.......Sayo--{/cps}{nw}"
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show death as death zorder 100 at d_mid
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    hide death
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing.", False)
        except: pass
    $ pause(6.0)
    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    hide vignette
    hide noise
    hide s_kill_bg_zoom
    hide s_kill_bg2_zoom
    hide s_kill
    hide s_kill_zoom
    hide s_kill2_zoom
    hide s_kill_bg2
    hide s_kill2
    hide s_kill_zoom_trans
    scene bg sayori_bedroom
    show s_kill as s_kill zorder 2 at s_kill_mid
    stop music
    show screen texasText("Revive?", 560, 105)
    menu:
        "Yes":
            hide screen texasText
            jump FakeIn
        "No":
            jump FakeOut

label FakeOut:
    show screen texasText("Wait really?", 420, 105)
    menu:
        "Yes":
            "Okay then{cps=3}...{/cps}"
            "Suit yourself..."
            jump credits
        "No":
            "Phew..."
            "Though we lost him there for a sec."
            hide screen texasText
            jump FuckY

label FakeIn:
    d "OH FUCK NO!!"
    hide s_kill_zoom
    hide s_kill
    show doomguy 1a zorder 3 at t22
    show s_kill as s_kill zorder 2 at s_kill_out
    d "Sayori! Take this healing!"
    show megahealth 1a zorder 3 at r21
    show doomguy 1a zorder 2 at t22
    $ pause(1.75)
    hide megahealth
    play sound bgo
    hide s_kill
    hide s_kill_out
    show s_kill as s_kill zorder 2 at S_Shake_Out
    $ pause(8)
    hide s_kill
    hide S_Shake_Out
    show sayori 4m zorder 3 at t21
    s "Wahhhh!"
    s "I thought I fucking killed myself!"
    d "No, you\'re fine."
    d "I managed to revive you using my super epic space marine powers!"
    s 1i "But..."
    s "I really {i}did{/i} want to kill my self."
    d "Sayori, there is no way you are ever dying on my watch, I love you!"
    s 2t "Th-thank you, Doomguy."
    play music t4
    s "I... I love you too."
    show doomguy 1d zorder 2 at t22
    "Damn that\'s good to hear."
    "Doomguy (me), has been crushing on Sayori since before middle school."
    s 1o "Hey, do you have any idea why I would just suddenly want to kill myself?"
    d 1a "I have a sneaking suspicion."
    s "What are you thinking?"
    d "..."
    s "...?"
    d "Monika..."
    $ consolehistory = []
    call updateconsole("Hey assholes I can hear you.", "Hey assholes I can hear you.")
    show doomguy 1a zorder 2 at t22
    show sayori 1j zorder 3 at t21
    s "MONIKA!!!"
    call updateconsole("Sayori, do me a favor and \njust hang ur self again.", "Sayori, do me a favor and \njust hang ur self again.")
    s 5b "Uh, jeez Monika, that\'s not very nice of a thing to say to me."
    call updateconsole("Bitch, I don't fucking care.", "Bitch, I don't fucking care.")
    call updateconsole("Just fucking die!!!", "Just fucking die!!!")
    call updateconsole("del sayori.chr", "Permission Denied \'del sayori.chr\'")
    call updateconsole("Shit...", "Shit...")
    $ pause(1)
    call updateconsole("sudo del sayori.chr", "Deleting...")
    hide sayori
    show s_kill as s_kill zorder 2 at s_kill_out
    play sound "sfx/crack.ogg"
    stop music
    show doomguy 1a zorder 3 at t22
    d "NOOO!"
    d "Health GOOOOO!"
    show doomguy 1a zorder 2 at t22
    show megahealth 1a zorder 3 at r21
    $ pause(1.75)
    hide megahealth
    hide s_kill
    hide s_kill_out
    show s_kill as s_kill zorder 2 at S_Shake_Out
    play sound bgo
    $ pause(2)
    stop sound
    hide s_kill
    hide S_Shake_Out
    show sayori 4m zorder 3 at t21
    s "OH GOD IT HAPPENED AGAIN!!"
    s "WHY DO I KEEP KILLING MYSELF, WHAT KIND OF TWISTED HELL IS THIS???!!??"
    call updateconsole("lol", "lol")
    d "LOL??"
    d "DON\'T YOU LOL ME SLUT"
    call updateconsole("Oh yeah?", "Oh yeah?")
    $ pause(0.5)
    call updateconsole("And what are {i}you{/i} going to do about it?", "And what are {i}you{/i} going to do about it?")
    d "THIS, MOTHERFUCKER!!!!"
    show sayori 4m zorder 2 at t21
    show doomguy 1c zorder 3 at tr22
    call Bang
    d "There we go..."
    show doomguy 1a zorder 2 at ur22
    call updateconsole("Really?", "Really?")
    call updateconsole("Now I need a new terminal.", "Now I need a new terminal.")
    $ pause(1)
    call hideconsole
    $ consolehistory = []
    s 1q "Thank you!"
    s "I WILL NOW SMOOCH THE DOOM MARINE"
    play music t4
    show sayori 1q zorder 3 at lr22
    hide doomguy
    show doomguy 1d zorder 2 at t22
    d "Sayori..."
    show sayori 1q zorder 2 at r21
    show doomguy 1d zorder 2 at t22
    s 1r "Ehehe..."
    show sayori 4p zorder 2 at t31
    show conkycrinkler 1a zorder 3 at t32
    show doomguy 1a zorder 2 at t33
    play sound go
    c "{cps=100}GGGOOOAOHHHAHAHHAOHAOHOHAOAHOAHOAHOHAOHAOHAOHAOHAOH\nOHOHOHOHOOHHHOHOHHOOHOHOOHHOOHOHOHOHOOOHOOHOHOHOHOHOHOHHOHOHH!!!{/cps}{nw}"
    c "NO SMOOCHING BEFORE MARRIAGE!!!!!{nw}"
    hide conkycrinkler
    show sayori 4p zorder 2 at t21
    show doomguy 1a zorder 2 at t22
    $ pause(0.5)
    d "..."
    s 1o "..."
    d "Do you have any idea who that was?"
    s 1n "No..."
    show sayori 1n zorder 2 at t31
    show natsuki 4y zorder 3 at t32
    show doomguy 1a zorder 2 at t33
    stop music
    play sound "sfx/fall.ogg"
    n "Well!  I guess you\'re glad that I\'m here then!!"
    a "Natsuki?!"
    n "YES! IT IS I!!  THE BEST DOKI!!"
    call updateconsole("Hey you\'re not supposed to \nknow you\'re in a game yet.", "Hey you\'re not supposed to \nknow you\'re in a game yet.")
    n 4u "Oh... my bad..."
    call updateconsole("Yeah", "Yeah")
    show sayori 1n zorder 2 at t31
    show natsuki 4u zorder 2 at t32
    pause 1.5
    show doomguy 1c zorder 3 at tr33
    call Bang
    d "FUCK YOU!"
    call updateconsole("Dude seriously stop breaking these \nthey\'re expensive.", "Dude seriously stop breaking these \nthey\'re expensive.")
    $ pause(0.5)
    call hideconsole
    show doomguy 1a zorder 3 at ur33
    hide doomguy
    show doomguy 1a zorder 3 at i33
    d "AND STAY OUT!"
    s "Ok, ummm..."
    s "Natuski, you said you knew who that guy was?"
    n 3d "Yes!"
    play music t4
    n "He is a mystical fellow, told to be the lord of Texas Street Law."
    d "Texas Street Law?"
    n "Indeed!"
    n "Texas Street Law!"
    n "The ancient way of battle, even Monika is said to be a master in it!"
    s 3o "Wait, who is saying that Monika is a master at Texas Street Law?"
    n "Why of course that would be Yuri!"
    n "She is the head boss of the UTSLG."
    d "the what?{nw}"
    n "Her goons can take on anyone Monika throws at them!"
    n "But of course, Yuri can defeat even them."
    d "Well, it sounds like we need to get Yuri on our side then."
    n "Worry not!"
    n 4y "She's my girlfriend!"
    n "So she\'s already on our side."
    n 2d "But, although Yuri is a fucking ninja at Texas Street Law, the fellow I mentioned earlier is even better!"
    s 2n "Oh yeah, who is that guy?"
    n 1l "Why, it\'s Conky Crinkler of course!"
    n "And his appearence after you two{cps=3}...{/cps} smooched{cps=3}...{/cps} means that he has summoned you."
    d "Summoned us for what."
    "Natsuki gets a massive grin across her face."
    n 3y "Well... he means to instruct you in the ancient art of Texas Street Law."
    $ c_name = "speaker in Natsuki\'s pocket"
    c "Come find me, Doom Guy and Sayori, in the manga closet of the clubroom."
    d "But how will we get past Monika?"
    d "She is lord of that realm."
    c "That\'s the best part Doom Guy, She\'s so focused on finding you, she\'d never check right under her nose."
    d "Aaahhhhh, Souka."
    d "IKUZO!"
    $ c_name = "Conky Crinkler"
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    call Doom2

    return
