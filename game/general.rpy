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

## Custom transitions
label reset:
    call audio_fadeout
    scene bg black with dissolve 
    return




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