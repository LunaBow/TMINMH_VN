
# --- Splashscreen ---
label splashscreen:
    scene bg_room_pitch_black
    pause 0.5
    
    show splash_logo with dissolve
    play sound "audio/sfx/splash.mp3" volume 0.8 
    pause 2.0
    hide splash_logo with dissolve
    pause 0.5
    return

# --- Main Entry Point ---
label start:
    # Initialize Core Stats
    $ trust_level = 0
    $ influence_level = 0
    $ perm_pc_files = False # Progression starts with limited permissions
    $ current_pov = "webcam" # Standard Act I POV

    menu boot_selection:
        "DEMO MODE":
            $ demo_mode = True
            "Loading streamlined vertical slice..."
            jump act1_start

        "DEBUG MODE":
            $ debug_mode = True
            jump debug_menu

        "NORMAL MODE":
            $ demo_mode = False
            $ debug_mode = False
            "Initializing system..."
            jump intro_sequence # The animated intro where Sunny wakes up

# --- 3. Debug Navigation ---
label debug_menu:
    menu:
        "DEBUG :: JUMP TO ACT"
        "Act I: Signal (Start)":
            jump act1_start
        "Act II: Attachment (Desktop Access)":
            $ perm_pc_files = True
            jump act2_start
        "Act III: Access (Phone POV)":
            $ current_pov = "phone"
            jump act3_start
        "Test OS Desktop":
            show screen os_desktop_interface
            "OS Screen active. Interact with icons or Taskbar."
            jump debug_menu

# --- 4. Narrative Intro ---
label intro_sequence:


    jump act1_start


label ending:
    "Thank you for playing!"
    return  