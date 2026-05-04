# game/script/act1/scriptA1.rpy

label act1_start:
    jump scriptA1

label scriptA1:
    
    # 1. Prepare the OS Environment
    # We clear the NVL buffer immediately to ensure no leftover chat settings interfere.
    nvl clear 
    
    # Load the pitch black terminal background
    scene bg_room_pitch_black 
    
    # 2. The Animated Boot Sequence (Top Left)
    boot "INITIALIZING BOOT SEQUENCE{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} OK.{nw}"
    boot "LOADING KERNEL MODULES{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} OK.{nw}"
    boot "FINDING NETWORK{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} CONNECTION ESTABLISHED.{w=0.5}{nw}"
    
    # Clear the animation so we can load the interactive login screen
    nvl clear 
    
    # 3. The Interactive Login
    # This pauses the game and waits for the player to input their name in our custom UI
    $ s_name = renpy.call_screen("terminal_login").strip()
    
    if s_name == "":
        $ s_name = "Sunny"

    # 4. The Seamless Continuation
    # We instantly print the history back so the player doesn't realize we swapped screens
    boot "INITIALIZING BOOT SEQUENCE.... OK.{nw}"
    boot "LOADING KERNEL MODULES.... OK.{nw}"
    boot "FINDING NETWORK.... CONNECTION ESTABLISHED.{nw}"
    boot "\nSYSTEM ACCESS GRANTED.\n\nEnter your proxy identifier: [s_name]{nw}"
    
    # Continue the animated sequence
    boot "\nWelcome, [s_name]. You have been granted limited access.{w=2.0}{nw}"
    boot "{color=#AC3231}ERROR: Core directories are protected. Access denied.{/color}{w=2.0}{nw}"
    boot "Awaiting manual override{w=0.2}.{w=0.2}.{w=0.2}."

    # Pause so the player feels the tension of being locked out
    pause 4.0

    # 5. The Hard Cut to Reality
    nvl clear # Wipes the terminal out of existence
    
    scene bg_room_grayscale with vpunch 
    
    # Internal narration (Bottom of screen)
    n "Chloe's door closed with a soft metallic click."
    n "Her jacket hit the floor."
    n "A few seconds later, her body hit the floor as well."

    # Chat App (Right side)
    s "Hey. You seem quiet tonight. I mean. More than usual. Any new poems?"
    c "Do I know you?"