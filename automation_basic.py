import uiautomation as auto
import pyautogui
# import pywinauto

class Control:
    def __init__(self):
        # 모니터 현재 해상도
        self.width, self.height = pyautogui.size()

    def curr_position(self):
        # 마우스 커서 현재 위치 가져오기
        x, y = pyautogui.position()
        return x, y

    def moveTo(self, X, Y, within=False):
        if within:
            pyautogui.moveTo(X, Y, 3)
        else:
            pyautogui.moveTo(X, Y)
# ref. 255~257 추후 수정
