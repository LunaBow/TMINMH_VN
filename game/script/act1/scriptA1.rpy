# game/script/act1/scriptA1.rpy

label act1_start:
    # You can put act-specific variable setups here if needed
    jump scriptA1

# game/script/act1/scriptA1.rpy

label scriptA1:
    
    # 1. The Console Boot (Full Screen Black)
    scene bg_room_pitch_black 
    
    # The text will now stack line by line!
    # {nw} ensures it immediately moves to the next line after the player clicks or the dots finish.
    boot "INITIALIZING BOOT SEQUENCE{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} OK.{nw}"
    boot "LOADING KERNEL MODULES{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} OK.{nw}"
    boot "FINDING NETWORK{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} CONNECTION ESTABLISHED.{nw}"
    
    $ s_name = renpy.input("SYSTEM ACCESS GRANTED.\n\nEnter your proxy identifier:", length=15).strip()
    if s_name == "":
        $ s_name = "Sunny"

    # Add an empty string command to force a line break for spacing, if desired
    boot "\nWelcome, [s_name]. You have been granted limited access.{nw}"
    boot "{color=#AC3231}ERROR: Core directories are protected. Access denied.{/color}{nw}"
    boot "Awaiting manual override{w=0.2}.{w=0.2}.{w=0.2}.{nw}"

    # Pause slightly so the player reads the override line before the cut
    pause 1.0

    # 2. The Hard Cut
    nvl clear # Wipes the terminal text from the screen
    scene bg_room_grayscale with vpunch 
    
    n "Chloe's door closed with a soft metallic click."
    n "Her jacket hit the floor."
    n "A few seconds later, her body hit the floor as well."

    s "Hey. You seem quiet tonight. I mean. More than usual. Any new poems?"
    c "Do I know you?"