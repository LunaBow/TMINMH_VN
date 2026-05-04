init python:
    # Audio Channels
    renpy.music.register_channel("ambient", "ambient", loop=True, stop_on_mute=True)

## Color Palette Definitions
define onyx = "#0d0e13"    
define mint = "#08d3a4" 
define blood_red = "#ac3231"
define midnight = "#2e1131"
define dusk = "#454e7e"         
define black = "#0d0e13"
define white = "#d6d3d3"

## Screen Macros
label reset:
    call audio_fadeout
    scene bg black with dissolve 
    return

## Custom Transitions
define flash_blood = Fade(0.1, 0.0, 0.5, color=blood_red) 

define flash_mint = Fade(0.1, 0.0, 0.5, color=mint)

define fade_onyx = Fade(2.0, 1.0, 2.0, color=onyx) 

define hard_cut = Fade(0.0, 0.0, 0.0, color=onyx)

transform engine_panic:
    parallel:
        choice:
            xoffset 10 yoffset -10
        choice:
            xoffset -15 yoffset 5
        choice:
            xoffset 5 yoffset 15
        choice:
            xoffset -5 yoffset -5
        pause 0.05
        repeat
    parallel:
        choice:
            alpha 1.0
        choice:
            alpha 0.4
        choice:
            alpha 0.8
        choice:
            alpha 0.2
        pause 0.08
        repeat

# --- CAMERA & SURVEILLANCE EFFECTS ---

# Simulates the subtle, unsteady breathing of the Phone Camera POV in Act III+
transform camera_drift:
    ease 3.0 xoffset 5 yoffset 3
    ease 4.0 xoffset -4 yoffset -5
    ease 3.5 xoffset 2 yoffset 4
    ease 4.0 xoffset 0 yoffset 0
    repeat

# A slow, creeping zoom for when Sunny watches Chloe sleep or paint
transform surveillance_zoom:
    ease 15.0 zoom 1.15 xalign 0.5 yalign 0.5

# --- SYSTEM & UI EFFECTS ---

# Perfect for the blinking red recording dot on your Main Menu or Camera Overlay
transform ui_pulse:
    ease 0.8 alpha 0.2
    ease 0.8 alpha 1.0
    repeat

# --- HORROR & CORRUPTION EFFECTS ---

# A sharp, horizontal visual tear. Use this during the Convergence or when Luna interferes.
transform glitch_tear:
    parallel:
        choice:
            xoffset 15
        choice:
            xoffset -15
        choice:
            xoffset 0
        pause 0.05
        repeat
    parallel:
        choice:
            alpha 1.0
        choice:
            alpha 0.5
        pause 0.05
        repeat


## Audio Macros
label audio_fadeout:
    stop music fadeout 1.0
    stop sound fadeout 1.0
    stop ambient fadeout 1.0
    return

label audio_stop:
    stop music fadeout 0.0
    stop sound fadeout 0.0
    stop ambient fadeout 0.0
    return