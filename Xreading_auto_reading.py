import pyautogui
import time

def main(wp):
    print(pyautogui.size())
    i = 0
    while(True):
        i += 1
        WaitReadTime()
        ScrollBottom(wp[0],wp[1])
        _ = FindClosebutton()
        p = FindNextbutton()
        ClickNextbutton(p)
        print("slide " + str(i) + " page")

def WaitReadTime():
    time.sleep(70)
    return

def ScrollBottom(px,py):
    pyautogui.moveTo(px, py, duration= 2)
    x, y = pyautogui.position()
    pyautogui.click( x, y)
    pyautogui.scroll(-2000, x, y)
    time.sleep(0.1)
    return


def FindClosebutton():
    p = pyautogui.locateOnScreen("./img/close_button2.png")
    close_button_list = ["./img/close_button.png","./img/close_button2.png"]
    for cb in close_button_list:
        p = pyautogui.locateOnScreen(cb)
        if p != None:
            close_x, close_y = pyautogui.center(p)
            time.sleep(1)
            pyautogui.click(close_x, close_y)
            print("click ")
            exit()
    return p

def FindNextbutton():
    next_button_list = ["./img/next_button.png","./img/next_button2.png","./img/next_button3.png","./img/next_button4.png"]
    for nb in next_button_list:
        p = pyautogui.locateOnScreen(nb)
        if p != None:
            break
    if p == None:
        print("cannot found next button")
        exit()
    return p


def ClickNextbutton(p):
    next_x, next_y = pyautogui.center(p)
    time.sleep(0.1)
    pyautogui.click(next_x, next_y)
    time.sleep(0.1)
    pyautogui.move(-100, 0)

if __name__ == '__main__':
    """
    必要なこと
    ・ウィンドウの座標
    ・Next及びCloseの画像の写真を撮ってimgフォルダに入れてください
    """
    window_point = [300, 1300]
    main(window_point)
