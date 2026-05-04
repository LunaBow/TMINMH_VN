# game/core/os_programs.rpy

# ==========================================
# DESKTOP ENVIRONMENT
# ==========================================

screen os_desktop_interface():
    zorder 10 # Base OS layer
    
    # Background (you can swap this for the webcam POV later)
    add "images/bg/bg_room_pitch_black.png" 

    # The "Invasive" Overlay
    # add "images/general/webcam_overlay.png" 

    # Desktop Icons (Programs)
    vbox:
        xpos 30 
        ypos 30
        spacing 40
        
        # Program 1: The Chat App
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5
                idle "gui/bubble.png" 
                hover Transform("gui/bubble.png", matrixcolor=BrightnessMatrix(0.2))
                action Show("os_nvl") 
            text "Chat.exe" color "#D6D6D6" size 16 xalign 0.5 outlines [(1, "#000", 1, 1)]

        # Program 2: File Explorer (Bridge Folder)
        if perm_pc_files: 
            vbox:
                spacing 5
                imagebutton:
                    xalign 0.5
                    idle "gui/window_icon.png" 
                    hover Transform("gui/window_icon.png", matrixcolor=BrightnessMatrix(0.2))
                    action Show("os_file_viewer", filename="bridge/") 
                text "bridge/" color "#D6D6D6" size 16 xalign 0.5 outlines [(1, "#000", 1, 1)]

    # Call the taskbar to render on top of the desktop
    use os_taskbar


# ==========================================
# TASKBAR
# ==========================================

screen os_taskbar():
    zorder 11 # Sits just above the desktop background
    
    frame:
        xfill True
        ysize 50
        yalign 1.0 # Pinned to the bottom
        background Solid("#25171D") # Base darkness/isolation color[cite: 6]
        
        hbox:
            yalign 0.5
            xpos 20
            spacing 20
            
            # Start Menu Button
            textbutton "SYS":
                text_color "#08D3A4" # Empathy Green[cite: 6]
                text_bold True
                action NullAction() # Replace with a menu toggle later
            
            # Clock (Optional OS immersion)
            text "11:42 PM" color "#D6D6D6" yalign 0.5 xpos 1750


# ==========================================
# UNIVERSAL WINDOW TEMPLATE
# ==========================================

screen os_window_template(app_title, content_text):
    zorder 15 # Floats above the desktop (10) and taskbar (11), behind chat (20)
    
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