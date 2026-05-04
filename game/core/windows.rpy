# game/core/windows.rpy


# The invisible box that holds the terminal text
style terminal_window:
    xalign 0.0 # Anchors to the left
    yalign 0.0 # Anchors to the top
    xoffset 50 # Pushes it 50 pixels away from the left edge of your monitor
    yoffset 50 # Pushes it 50 pixels down from the top edge
    background None # Completely transparent

style terminal_text:
    color "#08D3A4"     # Empathy Green
    size 24             
    bold True
    # font "fonts/JetBrainsMonoNL-Regular.ttf" # Uncomment when you drop the font in
    outlines [(1, "#000000", 1, 1)]
    layout "tex"
    xalign 0.0 # Left-aligns the text itself

style terminal_prompt:
    color "#08D3A4"
    size 22
    bold True
    textalign 0.5
    xalign 0.5
    # font "fonts/JetBrainsMonoNL-Regular.ttf"

style terminal_input:
    color "#FFFFFF"
    size 28
    xalign 0.5
    # font "fonts/JetBrainsMonoNL-Regular.ttf"
# ==========================================
# CHAT (NVL) PRESETS
# ==========================================

style nvl_window:
    xalign 1.0 
    yalign 0.5 
    xsize 550 
    ysize 1000 
    xoffset -40 
    background Solid("#0D0E13E6") # Onyx background[cite: 6]
    padding (30, 30, 60, 30) 

style nvl_dialogue:
    size 20
    xalign 0.0 
    layout "tex" 
    color "#FFFFFF" 
    xmaximum 450 

style nvl_label:
    bold True
    size 22
    xalign 0.0