image steve:
    "mod_assets/SteveH.png"

label Doom2:
    scene bg closet
    with dissolve_scene_half
    play music t4
    "Sometime later..."
    show sayori 1a zorder 2 at t31
    show natsuki 2d zorder 2 at t32
    show doomguy 1a zorder 2 at t33
    n "Welcome to the lair!"
    s 4q "I\'m so excited!"
    show doomguy 1d zorder 2 at t33
    "Wow, Sayori is so cute"
    n 2d "Hey Doom Guy, what are you blushing at buddy?"
    d 1a "Huh?"
    d "Nothing, nothing at all."
    s 4s "Ehehe..."
    n 5y "Good job Sayori, getting a fucking hunky boi like this."
    n "Can\'t shine a candle to my Yuri though."
    show yuri 3y2 zorder 3 at h43
    show sayori 2m zorder 2 at t41
    show natsuki 5y zorder 2 at t42
    show doomguy 1a zorder 2 at t44
    y "WHO SUMMONED THE ALMIGHTY ONE?"
    y 1c "Oh Natsuki AAAAAAA I LOVE YOUUU!!!"
    show yuri 3c zorder 5 at r_nyK
    show natsuki 1z zorder 2 at t42
    d "Well isn\'t that just fuckin adorable."
    show yuri 4e zorder 2 at lr43_nyK
    y "Th-thank you, Doom Guy."
    n 2l "Awww Yuri are you perhaps embarressed?"
    y "N-no..."
    show sayori 4q zorder 5 at lr44
    show doomguy 1d zorder 3 at i44
    s "I love you Doom Guy"
    show sayori 4q zorder 5 at r41
    show yuri 2f zorder 3 at t43
    y "Wait, so why are you guys here?"
    show natsuki 4j zorder 3 at t42
    show yuri 2f zorder 2 at t43
    show sayori 4q zorder 2 at t41
    n "We have come to learn to wield the anceint are of Texas Street Law!"
    show yuri 2f zorder 3 at t43
    show natsuki 4j zorder 2 at t42
    y "Really?"
    y "Why?"
    show yuri 2f zorder 2 at t43
    show doomguy 1a zorder 3 at t44
    d "Monika tried to get Sayori to kill herself."
    d "Luckily I was able to revive her with my super epic space marine powers."
    show yuri 3n zorder 3 at t43
    show doomguy 1a zorder 2 at t44
    "Yuri looks shocked."
    y "Oh my god!"
    y "Sayori are you okay?"
    y "Like holy shit are you good?"
    show yuri 2f zorder 2 at t43
    show sayori 2l zorder 3 at t41
    s "Ehehe... I wouldn\'t say I\'m totally fine, but I\'m definiately okay."
    s "Dying twice in the span of 15 minutes can be a bit traumatizing."
    y 3p "Lemme give you a hug!"
    show yuri 3s zorder 5 at r_ysH
    show natsuki 4j zorder 2 at lrn_syH
    play sound "sfx/fall.ogg"
    s 4s "Aw, thank you Yuri."
    s "That means a lot."
    "It\'s good to see Yuri supporting Sayori."
    "Brings joy to my heart."
    "That girl deserves the world."
    show doomguy 1d zorder 2 at t44
    $ pause(3.5)
    show doomguy 1a zorder 3 at t44
    stop music
    d "Ok you can stop hugging her now, {i}Yuri{/i}, you fucking {i}Yuri{/i}."
    $ pause(1)
    y 3y7 "nnnnNO!"
    d "GET OFF HER rrREEEEEEEEE!{p=1}{nw}"
    y "I WILL HUG HER FOREVER"
    d "I SAID GET OFF"
    $ pause(0.25)
    play sound "sfx/fall.ogg"
    show doomguy 1a at leftright_slide(1080, 295) zorder 5
    show natsuki 1hmm at leftright_slide(600, 635) zorder 4
    y "{cps=15}NYYAYAAAYAAAA{/cps}{nw}"
    d "{cps=15}AAAAAAAAAAAA{/cps}{nw}"
    y "AAAAAAAAAAAAAAA"
    show natsuki 1hmm at leftright_slide(635, 900) zorder 5
    n "SHUT THE FUCK UP!!!!!"
    $ pause(2)
    show doomguy 1a at leftright_slide(295, 786) zorder 4
    show yuri 1f at leftright_slide(295, 493) zorder 4
    n "GOD!!"
    n "STOP FIGHTING EACH OTHER WE SHOULD BE FIGHTING MONIKA!"
    y "..."
    d "..."
    s "..."
    play music t4
    y "S-sorry..."
    d "So uhhhhh."
    n "Yuri..."
    n "Tell them how to play it."
    n "Please."
    y "Okay..."
    show doomguy 1a at t44 zorder 3
    show natsuki 1g at t43 zorder 3
    show yuri 1g at t42 zorder 3
    show sayori 1g at t41 zorder 3
    s "Thank you for getting them off me Natsuki."
    n "Yeah no problem Sayori."
    d "Will knowing the game be enough to stop Monika?"
    y "Hopefully, I'm not sure."
    y "You might have to face off with her in a super ultra mega battle."
    y "But There's only about a 1 in a 100 chance of that happening."
    pause 1.5
    $ consolehistory = []
    call updateconsole("But what if I just")
    call updateconsole("python3", "python3")
    call updateconsole(">>>_SuperMegaBattle = random.randint(1, 10)", """Traceback (most recent call last):
    File "main.py", line 1, in <module>
        _SuperMegaBattle = random.randint(1, 10)
    NameError: name 'random' is not defined""")
    call updateconsole("wait shit uhhhhhhhhhhh")
    $ consolehistory = []
    call updateconsole("", "\n\n\n\n\n\n\n\n\n\n")
    call updateconsole("""
    import random

    _SuperMegaBattle = random.randint(1, 10)
    """)
    $ consolehistory = []
    y "OH GOD SHE\'S FOUND US!!!"
    call updateconsole("Wait no comeba-", "Wait no comeba-")
    y "FUCKING RUNNNNNNNNNNNN"
    call updateconsole("YURI!!  I DON\'T KNOW WHERE\nYOU ARE CALM DOWN GODDAMN LADY")
    d "Calm down Yuri, I got this."
    pause 2.0
    show doomguy 1c at tr44 zorder 4
    call Bang
    pause 0.5
    show doomguy 1a at ur44 zorder 4
    m "I'M CLAIMING INSURENCE ON THIS SHIT THESE ARE 400 FUCKING DOLLARS."
    d "How are you talking through the normal text box?"
    m ".....fu{nw}"
    call updateconsole("ck don't worry about it.", "ck don't worry about it.")
    call updateconsole("The overlord just forgot\nto make it that way.", "The overlord just forgot\nto make it that way.")
    y 1n "I thought you were the overlord?"
    call updateconsole("Yeah... yeah...", "Shit they figured us out.")
    call overlordConsole("Shut the fuck up they\n aren't supposed to\nknow I exist yet.")
    call updateconsole("sorry...")
    call hideconsole

    return

label steveTest:
    show doomguy 1a at t44 zorder 3
    show natsuki 1g at t43 zorder 3
    show yuri 1g at t42 zorder 3
    show sayori 1g at t41 zorder 3
    y 1l "Well that was... interesting..."
    d "Yeah..."
    d "Soo... Any chance I can get that tutorial on Texas Street Law."
    y 2d "Oh yes!  Of course, sorry, I had forgotten amongst all the excitment."
    n 5hmm "Amogus?{nw}"
    n 1a "{nw}"
    d "What was that Natsuki?"
    n 3w "Absolutely nothing..."
    n 3x "You are simply imagining things."
    d "Okay..."
    show natsuki 1a at i43 zorder 3
    y "So, Doomguy, ready for the Street Game sitrep?"
    d "Ready anytime you are, Yuri."
    y 1b "Alright."
    y "So basically Texas Street Law is a game of wits."
    y "You must outsmart your opponent in the blink of an eye and leave them in the dust."
    y 1r "It takes such skill, even I can barely keep up with the master."
    d "I'm ready."
    y 1b "So basically, there is some sort of judge presiding over the match, we are no animals."
    y "The judge asks both contestents a question and whoever answers with one of the matching answers on a board, wins."
    y "The answers are based on a worldwide survey that nobody even knows happened."
    y "The underground rulers of Texas Street Law have access to every piece of information ever recorded."
    y "It's how America won the Cold War."
    d "Wow..."
    "This seems like a familiar setup..."
    d "Wait so what did you say the questions are based on?"
    y "A survey."
    d "So..."
    y 1a "Survey says..."
    "Is it just..."
    "No..."
    "It couldn't possibly..."
    "Yuri stands there waiting for any other questions I may have, seemingly oblivious to the similarities of her beloved game to another beloved game."
    d "Yuri..."
    d "Did you ever stop to consider the similiarities of this game to another certain game?"
    show yuri 1p at i42 zorder 4
    "Yuri seems shocked for a moment, then recomposes herself."
    y "What are you talking about?"
    y "Texas Street Law is an indepentantly run global economy of wit."
    "Oh lord..."
    s "Yuri, please have you ever watched the videos on YouTube of the game?"
    y "What game??"
    y "You guys are scaring me!"
    "Even Natsuki, the previously also oblivious contender of Texas Street Law is beginning to look concerned."
    n 1g "Wait a second."
    pause 2.0
    show natsuki scream at i43 zorder 4
    n  "OH GOD IT'S JUST FUCKING FAMILY FUED!!!"
    y "What's family fued?"
    n "YURI YOU FUCKING IDOT IT'S THE STEVE GAME!"

    show steve zorder 5 at i11
    $ r_name = "Steve Harvey"
    r "Hey y'all I'm Steve Harvey.{w=1.82}{nw}"
    hide steve

    n "..."

