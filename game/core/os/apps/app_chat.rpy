# game/core/os/apps/app_chat.rpy

# ==========================================
# APP: CHAT.EXE (Draggable NVL Messenger)
# ==========================================

screen os_nvl(dialogue, items=None):
    zorder 20 

    # We use a draggroup so the window can be moved around the desktop
    draggroup:
        drag:
            drag_name "chat_window"
            xalign 1.0 # Default position: Right side
            yalign 0.5
            drag_handle (0, 0, 550, 40) # Top 40px is the "handle" to click and drag
            draggable True

            # THE ACTUAL WINDOW (The child of the drag)
            window:
                style "os_nvl_window"
                
                vbox:
                    spacing 15 

                    # Header/Title Bar for the App
                    frame:
                        xfill True
                        ysize 40
                        background Solid("#2E1131") # Midnight Violet header[cite: 6]
                        text "Chat.exe" size 18 color "#FFFFFF" xalign 0.5 yalign 0.5

                    # Scrolling content
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

                    # Choices (Sunny's Stances)
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

# --- Styles ---
style os_nvl_window:
    xsize 550 
    ysize 1000 
    background Solid("#0D0E13E6") # Onyx background[cite: 6]
    padding (10, 10, 30, 10) 

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