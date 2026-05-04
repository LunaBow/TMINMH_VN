# game/core/os_chat.rpy

# ==========================================
# 1. THE TERMINAL (Left-Aligned Boot Sequence)
# ==========================================

screen terminal_nvl(dialogue, items=None):
    window:
        style "terminal_window"
        vbox:
            spacing 10 
            for d in dialogue:
                text d.what id d.what_id style "terminal_text"

style terminal_window:
    xalign 0.0 
    yalign 0.0 
    xoffset 50 
    yoffset 50 
    background None 

style terminal_text:
    color "#08D3A4"     
    size 24             
    bold True
    # font "fonts/JetBrainsMonoNL-Regular.ttf" 
    outlines [(1, "#000000", 1, 1)]
    layout "tex"
    xalign 0.0 


# ==========================================
# 2. THE CHAT APP (Right-Aligned NVL Box)
# ==========================================

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
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
                use nvl_dialogue(dialogue)

        if items:
            vbox:
                xalign 0.5
                spacing 10
                for i in items:
                    textbutton i.caption action i.action style "nvl_button"

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            style "nvl_entry"
            vbox:
                spacing 2
                if d.who is not None:
                    text d.who id d.who_id style "nvl_label"
                text d.what id d.what_id style "nvl_dialogue"

# --- Chat Styles ---
style nvl_window:
    xalign 1.0 
    yalign 0.5 
    xsize 550 
    ysize 1000 
    xoffset -40 
    background Solid("#0D0E13E6") # Onyx background with E6 transparency[cite: 6]
    padding (30, 30, 60, 30) 

style nvl_entry:
    xfill True
    padding (10, 10, 10, 10)

style nvl_label:
    bold True
    size 22
    xalign 0.0 

style nvl_dialogue:
    size 20
    xalign 0.0 
    layout "tex" 
    color "#FFFFFF" 
    xmaximum 450 

style nvl_button:
    xalign 0.5
    xfill True
    padding (10, 10, 10, 10)
    background Solid("#2E1131") # Midnight Violet[cite: 6]
    hover_background Solid("#AC3231") # Danger Red[cite: 6]

style nvl_button_text:
    xalign 0.5
    size 20
    color "#FFFFFF"
    hover_color "#FFFFFF"