# ==========================================
# 1. THE TERMINAL (Left-Aligned Boot Sequence)
# ==========================================

screen term_nvl(dialogue, items=None):
    zorder 20 # Sits above the desktop layer
    
    window:
        style "term_window"
        vbox:
            spacing 10 
            for d in dialogue:
                text d.what id d.what_id style "term_text"

style term_window:
    xalign 0.0 
    yalign 0.0 
    xoffset 50 
    yoffset 50 
    background None 

style term_text:
    color "#08D3A4"     # Empathy Green[cite: 6]
    size 24             
    bold True
    # font "fonts/JetBrainsMonoNL-Regular.ttf" 
    outlines [(1, "#000000", 1, 1)]
    layout "tex"
    xalign 0.0 


# ==========================================
# 2. THE CHAT APP (Right-Aligned NVL Box)
# ==========================================

screen os_nvl(dialogue, items=None):
    zorder 20 # Sits above the desktop layer, sharing priority with the terminal
    
    window:
        style "os_nvl_window"
        has vbox:
            spacing 15 

        vpgrid:
            cols 1
            yinitial 1.0 
            scrollbars "vertical"
            mousewheel True
            draggable True
            xfill True
            yfill True

            vbox:
                spacing 20 
                use os_nvl_dialogue(dialogue)

        if items:
            vbox:
                xalign 0.5
                spacing 10
                for i in items:
                    textbutton i.caption action i.action style "os_nvl_button"

screen os_nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            style "os_nvl_entry"
            vbox:
                spacing 2
                if d.who is not None:
                    text d.who id d.who_id style "os_nvl_label"
                text d.what id d.what_id style "os_nvl_dialogue_text"

# --- Chat Styles ---
style os_nvl_window:
    xalign 1.0 
    yalign 0.5 
    xsize 550 
    ysize 1000 
    xoffset -40 
    background Solid("#0D0E13E6") # Onyx background with E6 transparency[cite: 6]
    padding (30, 30, 60, 30) 

style os_nvl_entry:
    xfill True
    padding (10, 10, 10, 10)

style os_nvl_label:
    bold True
    size 22
    xalign 0.0 

style os_nvl_dialogue_text:
    size 20
    xalign 0.0 
    layout "tex" 
    color "#FFFFFF" 
    xmaximum 450 

style os_nvl_button:
    xalign 0.5
    xfill True
    padding (10, 10, 10, 10)
    background Solid("#2E1131") # Midnight Violet[cite: 6]
    hover_background Solid("#AC3231") # Danger Red[cite: 6]

style os_nvl_button_text:
    xalign 0.5
    size 20
    color "#FFFFFF"
    hover_color "#FFFFFF"


# ==========================================
# 3. TERMINAL INPUT PROMPT
# ==========================================

screen input(prompt):
    zorder 50 # Highest priority, forces player attention over everything else
    style_prefix "term_input"

    # A sleek, centered OS Terminal box
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        padding (40, 40, 40, 40)
        background Solid("#0D0E13F2") # Almost solid Onyx[cite: 6]

        vbox:
            spacing 20
            # The prompt text
            text prompt style "term_prompt" 
            # The actual typing field
            input id "input" style "term_input_field"

# Custom styles for the terminal input
style term_prompt:
    color "#08D3A4" # Empathy Green[cite: 6]
    size 22
    bold True
    textalign 0.5
    xalign 0.5

style term_input_field:
    color "#FFFFFF"
    size 28
    xalign 0.5