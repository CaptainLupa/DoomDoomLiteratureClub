image console_bg:
    "#333"
    topleft
    alpha 0.75 size (480,180)

image overlordConsole_bg:
    "#333"
    topright
    alpha 0.75 size (480,180)

image bang:
    "mod_assets/bang.png"
    topleft
    alpha 1 size (480, 180)

style console_text:
    font "gui/font/F25_Bank_Printer.ttf"
    color "#fff"
    size 18
    outlines []


style console_text_console is console_text:
    slow_cps 30

default consolehistory = []
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

default overlord_consoleHistory = []
image overlord_console_caret = Text(">", style="console_text", anchor=(0,0), xpos=800, ypos=10)
image overlord_console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=830, ypos=50)
image overlord_console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=830, ypos=10)

label updateconsole(text="", history=""):
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    show console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

label overlordConsole(text="", history=""):
    show overlordConsole_bg zorder 100
    show overlord_console_caret zorder 100
    show overlord_console_text "_" as ctext zorder 100
    show overlord_console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show overlord_console_text "_" as ctext zorder 100
    call updateOverlordConsoleHistory(history)
    $ pause(0.5)
    return

label Bang:
    play sound bang
    show bang zorder 101
    $ pause(0.5)

label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return

label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole (drawtext=currenttext)
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    $ pause(0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

    label drawconsole(drawtext=""):

        show console_text "[drawtext]_" as ctext zorder 100

        return

label updateconsolehistory(text=""):
    if text:
        python:
            consolehistory.insert(0, text)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history "[consolehistorydisplay]" as chistory zorder 100
    return

label clearConsoleHistory:
    python:
        consolehistory = []
        consolehistorydisplay = '\n'.join(map(str, consolehistory))
    show console_history "[consolehistorydisplay]" as chistory zorder 100
    return

label updateOverlordConsoleHistory(text=""):
    if text:
        python:
            overlord_consoleHistory.insert(0, text)
            if len(overlord_consoleHistory) > 5:
                del overlord_consoleHistory[5:]
            consolehistorydisplay = '\n'.join(map(str, overlord_consoleHistory))
        show overlord_consoleHistory "[consolehistorydisplay]" as chistory zorder 100
    return

label hideconsole:
    hide console_bg
    hide console_caret

    hide ctext
    hide chistory

    hide overlordConsole_bg
    hide overlord_console_caret

    hide bang
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
