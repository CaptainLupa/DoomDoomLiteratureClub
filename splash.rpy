init python:
    menu_trans_time = 1
    splash_message_default = "This is the default splash_message_default"
    splash_messages = [
    "Why do you look like a cheese stick?",
    "How old are you?",
    "How many shrimps do you have to eat, before you make your skin turn pink?  Eat too much and you\'ll get sick, shrimp are pretty rich.",
    "I ama Mad Shientisto, eh so cuuuul...  sonovabich!",
    "Big ol tiddies",
    "Tig ol Biddies",
    "FUCK",
    "show natsuki 4y zorder 3 at h11\n\"MANGA IS FUCKING LITERATURE!!!!\"",
    "Make sure to delete the game directory",
    "Natsuki is the best fuck you.",
    "Holy shit I love pink haired tsunderes",
    "Zero Two can shove her cock in my ass oh YEAH.",
    "My pubes are pink...",
    "Should I be concerned that it\'s only 30 minutes to mars?",
    "I love futa porn, and also tentacle stuff.\nNice and pulsating..."
    ]

    hs_splash_messages = [
    "Why do you look like a cheese stick?",
    "How old are you",
    "Big ol tiddies",
    "Tig ol biddies",
    "FUCK",
    "show natsuki 4y zorder 3 at h11\n\"MANGA IS FUCKING LITERATURE!!!!!\"",
    "Make sure to delete the game directory.",
    "Natsuki is the best fuck you.",
    "Holy shit do I love pink haired tsunderes",
    "My pubes are pink...",
    "How many shrimps do you have to eat,\nbefore you make your skin turn pink?\nEat too much and you\'ll get sick\nshrimp are pretty rich.",
    "I ama Mad Shientisto, eh so cuuuuul!\nsonovabich."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image splash_skyrim = ParameterizedText(style="splash_skyrim", xalign=0.83, yalign=0.90)

image splash_halo = ParameterizedText(style="splash_halo", xalign=0.88, yalign=0.45)

image splash_sw = ParameterizedText(style="splash_sw", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image skyrim_load:
    truecenter
    "mod_assets/Skyrimloading.png"
    xalign 0.5
    yalign 0.5
    zoom 0.67

image sw_load:
    truecenter
    "mod_assets/starfield.png"
    xalign 0.5
    yalign 0.5
    zoom 0.45

image sw_logo:
    truecenter
    "mod_assets/sw.png"
    xalign 0.5
    yalign 0.5

image halo_load:
    truecenter
    "mod_assets/Haloload.png"
    xalign 0.5
    yalign 0.5
    zoom 0.75

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_d:
    subpixel True
    "mod_assets/menu_art_D.png"
    xcenter 685
    ycenter 460
    zoom 0.8
    menu_art_move(0.78, 750, 0.68)

image menu_art_CC:
    subpixel True
    "mod_assets/menu_art_CC.png"
    xcenter 975
    ycenter 220
    zoom 0.70
    menu_art_move(0.78, 800, 0.60)

image menu_art_L:
    subpixel True
    "mod_assets/luigi.png"
    xcenter 1100
    ycenter 50
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_m_NOMOVE:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 0.75

image menu_art_y_NOMOVE:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 1000
    ycenter 640
    zoom 0.75

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "mod_assets/logo.png"
    subpixel True
    xcenter 240
    ycenter 125
    zoom 0.65
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform sw_move:
    subpixel True
    yoffset 400
    pause 0.50
    linear 6.25 yoffset -600

transform sw_logo_move:
    subpixel True
    truecenter
    zoom 1.00
    easein 6 zoom 0.00

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:

    python:
        persistent.playthrough = 0
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    $ restore_relevant_characters()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.First_run_DOOM:
        $ restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "This is a mod for Doki Doki Literature Club and is not affiliated with Team Salvato."
        "This is designed to be played after finishing the base game."
        "You can download the original game at http://ddlc.moe"
        "Also make sure you have sound on!"
        $ persistent.First_run_DOOM = True
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: renpy.file("../characters/sayori.chr")
            except: s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        $ pause(1.0)
        show end with dissolve_cg
        $ pause(3.0)
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Now everyone can be happy.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ Succ = renpy.random.randint(1, 100)
    $ is_skyrim = False
    $ is_halo = False
    $ is_sw = False
    if Succ >= 10 and Succ <= 15:
        $ config.main_menu_music = audio.halo
        $ is_halo = True
    elif Succ >= 16 and Succ <= 21:
        $ config.main_menu_music = audio.Skyrim
        $ is_skyrim = True
    elif Succ >= 22 and Succ <= 27:
        $ config.main_menu_music = audio.sw
        $ is_sw = True
    else:
        $ config.main_menu_music = audio.rt
    if not is_sw:
        $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if is_halo or is_skyrim or is_sw:
        $ splash_message = renpy.random.choice(hs_splash_messages)
    else:
        $ splash_message = renpy.random.choice(splash_messages)
    if is_skyrim:
        show black with Dissolve(2, alpha=True)
        $ pause(2)
        show skyrim_load with Dissolve(2, alpha=True)
        show splash_skyrim "[splash_message]" with Dissolve(0.5, alpha=True)
        $ pause(5)
        hide splash_skyrim with Dissolve(0.25, alpha=True)
        hide skyrim_load with Dissolve(1, alpha=True)
        hide black with Dissolve(1, alpha=True)
    elif is_halo:
        show black with Dissolve(2, alpha=True)
        $ pause(2.25)
        show halo_load with Dissolve(5, alpha=True)
        show splash_halo "[splash_message]" with Dissolve(5.90, alpha=True)
        $ pause(3)
        hide splash_halo with Dissolve(0.25, alpha=True)
        hide halo_load with Dissolve(1, alpha=True)
        hide black with Dissolve(1, alpha=True)
    elif is_sw:
        show black with Dissolve(0.25, alpha=True)
        $ pause(0.5)
        show sw_load with Dissolve(1.5, alpha=True)
        $ renpy.music.play(config.main_menu_music)
        $ pause(0.45)
        show sw_logo at sw_logo_move
        $ pause(6)
        show splash_sw "[splash_message]" at sw_move
        $ pause(6)
        hide splash_sw with Dissolve(0.25, alpha=True)
        hide sw_logo
        hide sw_load with Dissolve(0.75, alpha=True)
        hide black with Dissolve(1, alpha=True)
    else:
        show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "You're so funny."
        else:
            m "You're so funny, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.rt
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
