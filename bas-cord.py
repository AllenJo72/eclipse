from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key

stop_program = False
key_store = []

def on_click(x, y,button, pressed):
    if pressed:
        print(f"[{x},{y},{button}]")
        key_store.append(f'["{x}","{y}","{button}"]')
        
def on_press(key):
    global stop_program
    try:
        if key == Key.esc:
            stop_program = True 
            print("Exit")
            return False
    except AttributeError:
        pass
    
mouse_listener = Listener(on_click=on_click)
mouse_listener.start()

keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()

while not stop_program:
    pass


mouse_listener.stop()
keyboard_listener.stop()
print(key_store)
with open('./out.txt', 'w+') as save_file:
    save_file.write(str(key_store))
