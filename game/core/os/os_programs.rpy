# game/core/os_programs.rpy

# ==========================================
# MASTER PROGRAMS OVERVIEW
# Contains the Desktop grid and notification logic
# ==========================================

screen os_desktop_interface():
    zorder 10 
    
    # Desktop Background / Camera Feed
    add "images/bg/bg_room_pitch_black.png" 

    # Desktop Icons Container
    vbox:
        xpos 40 
        ypos 40
        spacing 50 
        
        # 1. CHAT ICON
        fixed:
            xsize 100
            ysize 120
            vbox:
                spacing 5
                imagebutton:
                    xalign 0.5
                    idle "gui/phone/button/idle_background.png" 
                    hover Transform("gui/phone/button/hover_background.png", matrixcolor=BrightnessMatrix(0.2))
                    action [SetVariable("unread_chats", 0), Show("os_nvl")] 
                text "Chat.exe" style "desktop_icon_text"

            if unread_chats > 0:
                frame:
                    xalign 1.0
                    yalign 0.0
                    xoffset 10
                    yoffset -10
                    background Solid("#AC3231") 
                    padding (8, 4)
                    text str(unread_chats) size 14 color "#FFF" bold True

        # 2. FILE EXPLORER ICON
        if perm_pc_files: 
            fixed:
                xsize 100
                ysize 120
                vbox:
                    spacing 5
                    imagebutton:
                        xalign 0.5
                        idle "gui/phone/button/idle_background.png" 
                        hover Transform("gui/phone/button/hover_background.png", matrixcolor=BrightnessMatrix(0.2))
                        action [SetVariable("unread_files", 0), Show("os_file_viewer", filename="bridge/")] 
                    text "Explorer" style "desktop_icon_text"

                if unread_files > 0:
                    frame:
                        xalign 1.0
                        yalign 0.0
                        xoffset 10
                        yoffset -10
                        background Solid("#AC3231") 
                        padding (8, 4)
                        text str(unread_files) size 14 color "#FFF" bold True

        # 3. TERMINAL ICON
        fixed:
            xsize 100
            ysize 120
            vbox:
                spacing 5
                imagebutton:
                    xalign 0.5
                    idle "gui/phone/button/idle_background.png" 
                    hover Transform("gui/phone/button/hover_background.png", matrixcolor=BrightnessMatrix(0.2))
                    action [SetVariable("unread_terminal", 0), Show("term_nvl")] 
                text "Terminal" style "desktop_icon_text"

            if unread_terminal > 0:
                frame:
                    xalign 1.0
                    yalign 0.0
                    xoffset 10
                    yoffset -10
                    background Solid("#AC3231") 
                    padding (8, 4)
                    text str(unread_terminal) size 14 color "#FFF" bold True

        # 4. SETTINGS ICON
        vbox:
            spacing 5
            imagebutton:
                xalign 0.5
                idle "gui/phone/button/idle_background.png" 
                hover Transform("gui/phone/button/hover_background.png", matrixcolor=BrightnessMatrix(0.2))
                action ShowMenu("preferences") 
            text "Settings" style "desktop_icon_text"

    # Overlay the Taskbar from os_ui.rpy
    use os_taskbar

style desktop_icon_text:
    color "#D6D6D6" 
    size 16 
    xalign 0.5 
    outlines [(1, "#000", 1, 1)]