# game/core/os/apps/explorer.rpy

# ==========================================
# APP: FILE EXPLORER
# ==========================================

screen os_file_viewer(filename):
    zorder 15 
    modal True # Prevents clicking the desktop while open
    
    frame:
        background Solid("#0D0E13E6") 
        align (0.5, 0.5)
        padding (40, 40)
        vbox:
            text "[filename]" color "#08D3A4" size 30 
            null height 20
            
            # Future-proofing: We can add if/elif statements here for different files
            if filename == "poems.txt":
                text "longing for dissociation\nbecause I can't stand\nthis blanket scraping at my skin" size 22 color "#FFFFFF"
            
            null height 30
            
            textbutton "Close":
                action Hide("os_file_viewer") 
                xalign 1.0