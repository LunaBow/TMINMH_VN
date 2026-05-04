# game/core/os/apps/app_terminal.rpy

# This list will hold our "Safe" strings for the boot sequence
default terminal_history = []

screen term_nvl(dialogue, items=None):
    zorder 50 
    frame:
        style "term_window"
        vbox:
            spacing 10 
            for d in dialogue:
                # Standard NVL objects work here
                text d.what id d.what_id style "term_text"

screen terminal_login(): 
    zorder 60
    
    frame:
        style "term_window"
        vbox:
            spacing 10
            
            # 1. Render our custom history strings safely
            for line in terminal_history:
                text line style "term_text"

            # 2. Add the live interactive part
            null height 10
            text "SYSTEM ACCESS GRANTED." style "term_text"
            text "" style "term_text" 
            
            hbox:
                spacing 0
                text "Enter your proxy identifier: " style "term_text"
                input id "input" style "term_text" length 15 color "#FFFFFF"

style term_window:
    xpos 50 
    ypos 50 
    background None 
    padding (0, 0, 0, 0)

style term_text:
    color "#08D3A4" # Empathy Green
    size 24             
    bold True
    outlines [(1, "#000000", 1, 1)]
    layout "tex"