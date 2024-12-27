import pyautogui as pg
import time

pg.click(1346, 1072)
pg.click(351, 63)
pg.typewrite("http://127.0.0.1/Chatapp/login.php") # URL of site to visit
pg.press('enter')
time.sleep(4)
pg.click(859,518)
pg.typewrite("wildbear@thatsapp.web") # Email
time.sleep(2)
pg.click(852,593)
pg.typewrite("wild")  # Password
time.sleep(2)
pg.click(939,651)
time.sleep(1)
pg.click(860,561)
time.sleep(1)
pg.click(856,860)
time.sleep(1)
pg.typewrite("Happy BirthDay")
time.sleep(3)
pg.press('enter')
