from gesture import process_gesture
from voice import listen_command, execute_command
import threading

def run_voice():
    while True:
        cmd = listen_command()
        execute_command(cmd)

# Run voice in background
threading.Thread(target=run_voice).start()

# Run gesture in main thread
process_gesture()