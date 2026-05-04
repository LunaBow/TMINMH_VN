# game/script/script.rpy

# Ren'Py automatically looks for a 'splashscreen' label before loading the Main Menu.
label splashscreen:
    scene bg_room_pitch_black
    pause 0.5
    
    # Show your studio logo or a content warning here
    show splash_logo with dissolve
    pause 2.0
    hide splash_logo with dissolve
    pause 0.5
    
    # Returning from here automatically boots up the Main Menu
    return

# 'start' is the default label triggered by the "New Game" button.
label start:

    
    $ s_name = "Sunny"
    $ trust_level = 0
    
    jump act1_start