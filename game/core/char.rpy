# --- DYNAMIC VARIABLES ---
# Default name fallback for the player
default s_name = "Sunny"

# Terminal Boot Sequence
define boot = Character(None, 
    kind=nvl, 
    nvl_screen="term_nvl", # Hooks into your custom prefix!
    what_style="term_text") 

# Chat Application
define c = Character("Chloe", kind=nvl, nvl_screen="os_nvl", color="#454E7E")
define s = Character("[s_name]", kind=nvl, nvl_screen="os_nvl", color="#08D3A4")


# Characters communicating through the desktop messenger[cite: 4]
define v = Character("???", kind=nvl, color="#AC3231") # Danger Red[cite: 6]


# --- 3. INTERNAL NARRATION (Bottom, Minimalist) ---
# Used for thoughts, environmental descriptions, and action beats[cite: 4]
define n = Character(None, 
    what_italic=True, 
    what_color="#A0A0A0", 
    window_background=Solid("#0D0E13CC"), # Semi-transparent Onyx box[cite: 6]
    window_yalign=0.95) # Pinned to the bottom