#network config change to comptuer to adjust IP for device you are connection to
#Created by Matthew Dievendorf
#For Tilson Technology

##V 1.2 - Adjusted the times to perform faster | Also updated the subnet mask. The subnet mask typically doesnt change. Created a constants - 7.8.20
##V 1.0 - Opening CMD in admin mode and changing network configuration on Ethernet Adapter
#****IMPORTANT!! - Make sure you are in an admin mode command prompt to run this script** Will not work if you are not in ADMIN CMD**!!

import os, pyautogui, shutil, time

pyautogui.FAILSAFE = False
ipchange = input('IP that you are wanting to change to > ')
destip = input('IP that you will ping too > ')
subm = '255.255.255.0'
eadapt = 'Ethernet' + ' ' + input('What Ethernet Adapter you are changing> ')
dnss = '0.0.0.0'

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('cmd')
#pyautogui.press(['shift', 'ctrl', 'enter'])#doesnt work
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
pyautogui.keyUp('shift')
pyautogui.keyUp('ctrl')  

time.sleep(0.5)
#confirmation screen should pop through
pyautogui.press('left')
pyautogui.press('enter')

time.sleep(1)

pyautogui.typewrite('ipconfig')
pyautogui.typewrite(['enter'])
time.sleep(3)
print('*Take note of what current IP scheme is*')
time.sleep(3)

pyautogui.typewrite('netsh interface ipv4 set address' + ' ' + '"' + eadapt + '"' + ' '+ 'static' + ' '  + ipchange + ' '  + subm + ' ' + dnss)

pyautogui.typewrite(['enter'])

time.sleep(3)
pyautogui.typewrite('ipconfig')
pyautogui.typewrite(['enter'])
print('**Confirm change, If change did not go through correctly perform retry of script**')
time.sleep(3)
print('**Ping test to confirm destination is reachable**')
pyautogui.typewrite('ping' + ' ' + destip)
pyautogui.typewrite(['enter'])
time.sleep(6)

print('**As long as pings are good - continue on to your next step**')
time.sleep(4)
pyautogui.typewrite('exit')
pyautogui.typewrite(['enter'])
time.sleep(3)


