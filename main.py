import pyautogui as pg
import time

time.sleep(10)

txt = open('C:/cod-python/animals.txt', 'r')

a = 'saben is a'

for  i in txt:
    pg.write(a + ' ' + i)
    pg.press('Enter')