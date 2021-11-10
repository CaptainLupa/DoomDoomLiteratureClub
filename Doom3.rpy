label Doom3:
    play music t9
    scene bg sayori_bedroom
    with dissolve_scene_full

    "After that whole ordeal in the club room, we decided to go back to Sayori's room."
    "We watched a few movies, talked about literally anything else."
    "Aything to get Natsuki and Yuri's minds off what happened."

    show sayori 1g at t41 zorder 3
    show yuri 1i at t42 zorder 3
    show natsuki 1n at t43 zorder 3
    show doomguy 1a at t44 zorder 3

    "We're watching some TV in sayori's bedroom at the moment."
    "Takeshi's Castle is playing at a decent volume."

    n "..."
    y "..."
    s "..."
    d "..."
    "..."
    "We're all situated around Sayori's bed, sitting, standing."
    "Even though we're watching TV, it's awkward."

    menu:
        "What should I do?"
        
        "Talk to Yuri":
            call YuriComf
        "Talk to Sayori":
            call SayoriComf
        "Talk to Natsuki":
            call NatsukiComf
        "Talk to everyone":
            call AllComf
    
    "Back from comfort arc"
    return

# Comfort arcs
label YuriComf:
    "I scoot a little closer to Yuri."
    hide sayori
    hide natsuki
    show doomguy 1a at t22 zorder 3
    show yuri 1i at t21 zorder 3
    "I speak to her in a slightly hushed voice."
    return

label SayoriComf:
    return

label NatsukiComf:
    return

label AllComf:
    return