with open("./out.txt", "r") as open_file:
    for lines in open_file:
        data_list = eval(lines)
        
import pyautogui as pg
import time
from datetime import datetime


target_hour = 14
target_minute = 25
target_second = 0

while True:
    current_time = datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    
    if current_hour == target_hour and current_minute == target_minute:

        for i in data_list:

            list_i = eval(i)
            if list_i[2] == "Button.left":
                pg.click(int(list_i[0]),int(list_i[1]))
                time.sleep(5)
        
            elif list_i[2] == "Button.right":
                pg.rightClick(int(list_i[0]),int(list_i[1]))
                time.sleep(5)
        break
