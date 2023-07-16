import pyautogui as pt
from time import sleep

sleep(3)

position1 = pt.locateOnScreen("smiley.png", confidence=.6)
x = position1[0]
y = position1[1]

def post_response(message):
    global x, y

    position = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)



#new messages check
def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence = .2)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = "Hello, It's Bot generated reply....'\n' Sanat will reply you soon...In case of emergency please call him."
                post_response(processed_message)
                sleep(5)
            else:
                print("No messages")
                sleep(10)

        except(Exception):
            print("No new messages")





check_for_new_messages()
