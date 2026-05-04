# game/script/act1/scriptA1.rpy

label act1_start:
    jump scriptA1

label scriptA1:
    nvl clear 
    # Reset our custom history list to keep the terminal_login screen clean
    $ terminal_history = [] 
    
    play music "audio/music/test.mp3" volume 0.6
    play ambient "audio/ambient/hum.mp3" volume 0.2 
    play sound "audio/sfx/boot.mp3" volume 0.4
    scene bg_room_pitch_black 
    
    # 1. Terminal Boot (Building the history as we go)
    $ line = "INITIALIZING BOOT SEQUENCE.... OK."
    $ terminal_history.append(line)
    boot "[line]{nw}"
    
    $ line = "LOADING KERNEL MODULES.... OK."
    $ terminal_history.append(line)
    boot "[line]{nw}"
    
    $ line = "FINDING NETWORK.... CONNECTION ESTABLISHED."
    $ terminal_history.append(line)
    boot "[line]{w=0.5}{nw}"
    
    # --- TRANSITION TO INPUT ---
    # We do NOT use nvl clear here. 
    # terminal_login will now display the 3 lines we just appended to terminal_history.
    $ s_name = renpy.call_screen("terminal_login").strip()
    
    if s_name == "":
        $ s_name = "Sunny"

    # 2. Final Terminal Refresh
    # Now we clear and "slap" the final state onto the screen
    nvl clear 
    boot "INITIALIZING BOOT SEQUENCE.... OK.{nw}"
    boot "LOADING KERNEL MODULES.... OK.{nw}"
    boot "FINDING NETWORK.... CONNECTION ESTABLISHED.{nw}"
    boot "\nSYSTEM ACCESS GRANTED.\n\nEnter your proxy identifier: [s_name]{nw}"
    
    boot "\nWelcome, [s_name]. You have been granted limited access.{w=2.0}{nw}"
    boot "{color=#AC3231}ERROR: Core directories are protected. Access denied.{/color}{w=2.0}{nw}"
    boot "Awaiting manual override{w=0.2}.{w=0.2}.{w=0.2}.{nw}"

    pause 4.0

    # 3. The Hard Cut to Reality
    nvl clear 
    scene bg_room_grayscale with vpunch 
    
    n "Chloe's door closed with a soft metallic click."
    n "Her jacket hit the floor."
    n "A few seconds later, her body hit the floor as well."

    # 4. Loading the Desktop
    show screen os_desktop_interface
    $ unread_chats = 3
    
    n "When she finally sat in front of her computer, the monitor's glow almost felt like sunrise."
    
    # Narrative roadblock: Game waits until player clicks the Chat icon
    while not renpy.get_screen("os_nvl"):
        pause 0.1

    # 5. The Conversation
    s "Hey."
    s "You seem quiet tonight. I mean. More than usual."
    s "Any new poems?"
    
    c "Do I know you?"