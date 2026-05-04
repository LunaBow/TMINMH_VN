# game/scenes.rpy

## General images & Overlays
image splash_logo = "images/general/splash_logo.mp4"
image overlay rec_dot_blink = "images/general/overlay_rec_dot.png" # The blinking VHS symbol
image overlay battery_low = "images/general/overlay_battery.png"
image overlay dirty_lens = "images/general/overlay_dirty_lens.png"
image overlay vhs_fragments = "images/general/overlay_vhs_fragments.png"

## Backgrounds: PC Webcam (Static, Horizontal)
image bg room grayscale = "images/bg/room_grayscale.png" # Power off/Empty
image bg room monitor_glow = "images/bg/room_monitor_glow.png" # Default harsh blue lighting
image bg room pitch_black = "images/bg/bg_room_pitch_black.png" # Pulled plug
image bg kitchen = "images/bg/kitchen.png" # Act V

## Backgrounds: Phone Camera (Dynamic, Vertical)
image bg phone_pov normal = "images/bg/phone_pov_normal.png"
image bg phone_pov shaky = "images/bg/phone_pov_shaky.png"
image bg phone_pov blackout = Solid("#000000") # Face down, ambient audio only

## Backgrounds: The Mind / Convergence
image bg forest lush = "images/bg/forest_lush.png" # Act II image file
image bg forest corrupted = "images/bg/forest_corrupted.png" # Act IV, green sky of numbers
image bg hospital_tiles = "images/bg/hospital_tiles.png" # Act IV memory flash

## CGs & Cutscenes
# Intro sequence
image cg intro_sunny_wake = Movie(play="images/movie/intro_sunny_wake.webm") # Buzzing, lights flickering
image cg intro_chloe_collapse = "images/general/cg_intro_collapse.png" # Hard cut

# Narrative Close-ups
image cg cursor_heart = "images/general/cg_cursor_heart.png" # The mouse moving by itself
image cg hardware_box = "images/general/cg_hardware_box.png" # USB hub, patch, wires
image cg chipped_mug = "images/general/cg_chipped_mug.png" # The coffee ring mug in Act V
image cg mirror_stranger = "images/general/cg_mirror_stranger.png" # Bathroom reflection feeling wrong
image cg microwave_reflection = "images/general/cg_microwave_reflection.png" # Stuttering code reflection