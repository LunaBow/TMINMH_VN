# game/core/os_ui.rpy

# ==========================================
# MASTER UI OVERVIEW
# Contains universal templates and OS navigation
# ==========================================

# --- TASKBAR ---
screen os_taskbar():
    zorder 11 
    
    frame:
        xfill True
        ysize 50
        yalign 1.0 
        background Solid("#25171D") # Isolation Base[cite: 6]
        
        hbox:
            yalign 0.5
            xpos 20
            spacing 20
            
            textbutton "SYS":
                text_color "#08D3A4" # Empathy Green[cite: 6]
                text_bold True
                action NullAction() 
            
            text "11:42 PM" color "#D6D6D6" yalign 0.5 xpos 1750

        button:
            action If(chat_open, Hide("os_nvl"), Show("os_nvl")) # Toggle behavior
            background If(chat_open, Solid("#444"), Solid("#222")) # Highlight if active
            xsize 150
            ysize 40
            
            hbox:
                spacing 8
                xalign 0.5
                add "icon_chat_micro" size (20, 20) yalign 0.5
                text "Chat.exe" size 14 color "#FFF" yalign 0.5

# --- UNIVERSAL WINDOW TEMPLATE ---
# Used to build new apps quickly without rewriting borders and close buttons
screen os_window_template(app_title, content_text):
    zorder 15 
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        background Solid("#0D0E13") # Onyx[cite: 6]
        
        vbox:
            spacing 0
            
            # Header
            frame:
                xfill True
                ysize 40
                background Solid("#2E1131") # Midnight Violet[cite: 6]
                
                hbox:
                    xfill True
                    text app_title color "#FFFFFF" size 18 xalign 0.0 yalign 0.5 xoffset 15
                    
                    textbutton "X":
                        xalign 1.0
                        yalign 0.5
                        text_color "#FFFFFF"
                        text_hover_color "#AC3231" 
                        action Hide("os_window_template") 
            
            # Content
            frame:
                xfill True
                yfill True
                background Solid("#0D0E13F2") 
                padding (25, 25, 25, 25)
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    text content_text color "#D6D6D6" size 20 layout "tex"

# --- GLOBAL FALLBACK INPUT ---
screen input(prompt):
    zorder 50 
    style_prefix "os_input"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        padding (40, 40, 40, 40)
        background Solid("#0D0E13F2") 

        vbox:
            spacing 20
            text prompt style "os_input_prompt" 
            input id "input" style "os_input_field"

style os_input_prompt:
    color "#08D3A4" 
    size 22
    bold True
    textalign 0.5
    xalign 0.5

style os_input_field:
    color "#FFFFFF"
    size 28
    xalign 0.5