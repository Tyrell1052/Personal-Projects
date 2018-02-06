import time
import webbrowser

break_counter = 0



while break_counter < 2:
    time.sleep(60)
    print("Take a break")
    webbrowser.open('https://ccp.instructure.com/login/canvas')

