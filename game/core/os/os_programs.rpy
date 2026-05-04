# ==========================================
# DESKTOP ENVIRONMENT
# ==========================================

screen os_desktop_interface():
    zorder 10 # Base OS layer, sits behind the chat and terminal
    
    # The "Invasive" Overlay
    add "images/general/webcam_overlay.png" 

    # Fake Folder System
    if perm_pc_files:
        imagebutton:
            xpos 100 ypos 100
            idle "gui/button/folder_idle.png"
            hover "gui/button/folder_hover.png"
            action Show("os_file_viewer", filename="poems.txt")
            tooltip "Open Folder"


# ==========================================
# UNIVERSAL WINDOW TEMPLATE
# ==========================================

screen os_window_template(app_title, content_text):
    zorder 15 # Floats above the desktop, but behind the chat (zorder 20)
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        background Solid("#0D0E13") # Solid Onyx base[cite: 6]
        
        vbox:
            spacing 0
            
            # TOP BAR (Header & Close Button)
            frame:
                xfill True
                ysize 40
                background Solid("#2E1131") # Midnight Violet header[cite: 6]
                
                hbox:
                    xfill True
                    text app_title color "#FFFFFF" size 18 xalign 0.0 yalign 0.5 xoffset 15
                    
                    textbutton "X":
                        xalign 1.0
                        yalign 0.5
                        text_color "#FFFFFF"
                        text_hover_color "#AC3231" # Danger red hover[cite: 6]
                        action Hide("os_window_template") 
            
            # CONTENT AREA
            frame:
                xfill True
                yfill True
                background Solid("#0D0E13F2") # Onyx background[cite: 6]
                padding (25, 25, 25, 25)
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    
                    text content_text color "#D6D6D6" size 20 layout "tex"

# ==========================================
# SPECIFIC FILE VIEWER (Fallback example)
# ==========================================

screen os_file_viewer(filename):
    zorder 15 
    modal True # Forces the player to close it before clicking the desktop again
    
    frame:
        background Solid("#0D0E13E6") # Onyx semi-transparent[cite: 6]
        align (0.5, 0.5)
        padding (40, 40)
        vbox:
            text "[filename]" color "#08D3A4" size 30 # Empathy Green[cite: 6]
            null height 20
            
            if filename == "poems.txt":
                text "longing for dissociation\nbecause I can't stand\nthis blanket scraping at my skin" size 22 color "#FFFFFF"
            
            null height 30
            textbutton "Close":
                action Hide("os_file_viewer") 
                xalign 1.0