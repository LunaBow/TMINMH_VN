# game/core/char.rpy

# Terminal Character
define boot = Character(None, 
    kind=nvl, 
    nvl_screen="term_nvl", # Matches the screen in os_ui.rpy
    what_style="term_text")

# Chat Characters
define c = Character("Chloe", kind=nvl, nvl_screen="os_nvl", color="#454E7E") # Dusk Blue[cite: 6]
define s = Character("[s_name]", kind=nvl, nvl_screen="os_nvl", color="#08D3A4") # Empathy Green[cite: 6]
define sys = Character("System", kind=nvl, nvl_screen="os_nvl", color="#D6D6D6")


# Characters communicating through the desktop messenger
define v = Character("???", kind=nvl, color="#AC3231") 


# --- 3. INTERNAL NARRATION (Bottom, Minimalist) ---
# Used for thoughts, environmental descriptions, and action beats
define n = Character(None, 
    what_italic=True, 
    what_color="#A0A0A0", 
    window_background=Solid("#0D0E13CC"), 
    window_yalign=0.95) # Pinned to the bottom