import os, pyautogui, shutil, time

pyautogui.FAILSAFE = False

print('***Auto change to DHCP mode****')
time.sleep(2)

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('cmd')
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
print('*** Confirm what current IP is***')
time.sleep(3)

pyautogui.typewrite('netsh interface ipv4 set address "Ethernet 4" source=dhcp ')
pyautogui.typewrite(['enter'])
time.sleep(2)
print('*** Confirm IP was changed***')
time.sleep(0.5)
pyautogui.typewrite('ipconfig')
pyautogui.typewrite(['enter'])
time.sleep(3)
print('*** Once done please EXIT*** ')

pyautogui.typewrite('exit')
pyautogui.typewrite(['enter'])
time.sleep(2)