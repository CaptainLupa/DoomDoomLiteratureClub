init -1 python:
    cursorPos = 0#main battle menu cursor position

image PFight:
    truecenter
    "mod_assets/PFight.png"

image Cursor:
    truecenter
    "mod_assets/Cursor.png"

#image pAtkBg: big box for persona attacks

#image pCursor: persona attack select cursor

#image pAtkText1 = ParameterizedText( add persona font )

#image pAtkText2 = ParameterizedText( add persona font )

#image pAtkText3 = ParameterizedText( add persona font )

#image pAtkText4 = ParameterizedText( Sex )

transform turnIn(x=400, z=0.80, y=1.03):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 0.00 subpixel True
    linear 0.30 alpha 1.00

transform turnSlide(x=400, x2=500, z=0.80, y=1.03):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x2

transform cUp(x, y, x2, y2):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom 0.30 alpha 1.00 subpixel True
    easein .15 xcenter x2 ypos y2

transform Bump(x, y, x2, y2):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom 0.30 alpha 1.00 subpixel True
    easein .15 xcenter x2 ypos y2
    pause 0.05
    easein .15 xcenter x ypos y

transform CursorDefault:#equivilent to 0 in cursorPos
    xcenter 460 yoffset 0 yanchor 1.0 ypos 0.80 zoom 0.30 alpha 0.00 subpixel True
    linear 0.15 alpha 1.00

screen move():
    key "K_w" action [Jump("moveCursorUp")]
    key "K_s" action [Jump("moveCursorDown")]
    key "K_k" action [Jump("kHit")]

label TurnBased:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg class_day with dissolve_scene_half
    play music persona
    show menu_art_m_NOMOVE at turnIn(990, 0.65) zorder 3
    show doomguy 1a at turnIn(335) zorder 4
    show PFight at turnIn(440, 1.15) zorder 5
    show Cursor at CursorDefault zorder 6
    call screen move

    return

label moveCursorUp:#moves the big ass cursor up
    if cursorPos != 0:
        if cursorPos == 1:#Cursor is at 1, move to 0
            show Cursor at cUp(400, 0.88, 460, 0.80) zorder 6
            $ cursorPos = 0
        elif cursorPos == 2:#Cursor at 2, move to 1
            show Cursor at cUp(515, 0.91, 400, 0.88) zorder 6
            $ cursorPos = 1
        elif cursorPos == 3:#Cursor at 3, move to 2
            show Cursor at cUp(445, 0.97, 515, 0.91) zorder 6
            $ cursorPos = 2
    else:#Cursor at 0 so it can't go up anymore
        show Cursor at Bump(460, 0.80, 462, 0.79) zorder 6
        $ cursorPos = 0

    $ pause(0.10)
    call screen move#recalls the screen for loop
    return


label moveCursorDown:
    if cursorPos != 3:
        if cursorPos == 2:#cursor at 2, move to 3
            show Cursor at cUp(515, 0.91, 445, 0.97) zorder 6
            $ cursorPos = 3
        elif cursorPos == 1:#cursor at 1, move to 2
            show Cursor at cUp(400, 0.88, 515, 0.91) zorder 6
            $ cursorPos = 2
        elif cursorPos == 0:#cursor at 0, move to 1
            show Cursor at cUp(460, 0.80, 400, 0.88) zorder 6
            $ cursorPos = 1
    else:#cursor at 3, so it cant go down
        show Cursor at Bump(445, 0.97, 446, 0.99) zorder 6
        $ cursorPos = 3

    $ pause(0.10)
    call screen move
    return

label kHit:
    if cursorPos == 0:
        jump pAttacks
    elif cursorPos == 1:
        jump items
    elif cursorPos == 2:
        jump guard
    elif cursorPos == 3:
        jump mAttack
    return

label pAttacks:
    "persona Attacks"

    call screen move

label guard:
    "Guard"

    call screen move

label items:
    "Items"

    call screen move

label mAttack:
    "Melee attacks"

    call screen move
