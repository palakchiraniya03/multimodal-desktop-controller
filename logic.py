last_gesture = ""
last_voice = ""

def process_combined(gesture, voice):
    if gesture == "point" and "open" in voice:
        print("Opening selected item")

    if gesture == "click" and "select" in voice:
        print("Selecting item")