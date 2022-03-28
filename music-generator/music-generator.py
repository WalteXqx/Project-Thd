import pyautogui
import random
import time

print('--music-generator--')
playm = int(input('1 = manual play 2 = auto play 3 = play all :'))

cm = '-p sad', '-p look at me', '-p moonlight', '-p one is the loneliest number', '-p venom 2 trailer music', '-p sunflower', '-p pigstep remix', '-p pan slash master', '-p i am so sorry', '-p go crazy'
if playm == 1:
    print(cm[random.randint(0, 9)])


elif playm == 2:
    print('go to discord now!')
    print('go to discord now!')
    print('go to discord now!')
    time.sleep(2.5)
    pyautogui.write(cm[random.randint(0, 9)])
    pyautogui.press('enter')

else:
    token = ''
    m1 = random.randint(0, 9)
    token += str(m1)

    m2 = random.randint(0, 9)
    while str(m2) in token:
        m2 = random.randint(0, 9)

    token += str(m2)

    m3 = random.randint(0, 9)
    while str(m3) in token:
        m3 = random.randint(0, 9)

    token += str(m3)

    m4 = random.randint(0, 9)
    while str(m4) in token:
        m4 = random.randint(0, 9)

    token += str(m4)

    m5 = random.randint(0, 9)
    while str(m5) in token:
        m5 = random.randint(0, 9)

    token += str(m5)

    m6 = random.randint(0, 9)
    while str(m6) in token:
        m6 = random.randint(0, 9)

    token += str(m6)

    m7 = random.randint(0, 9)
    while str(m7) in token:
        m7 = random.randint(0, 9)

    token += str(m7)

    m8 = random.randint(0, 9)
    while str(m8) in token:
        m8 = random.randint(0, 9)

    token += str(m8)

    m9 = random.randint(0, 9)
    while str(m9) in token:
        m9 = random.randint(0, 9)

    token += str(m9)

    m0 = random.randint(0, 9)
    while str(m0) in token:
        m0 = random.randint(0, 9)

    token += str(m0)

    print('go to discord now!')
    print('go to discord now!')
    print('go to discord now!')

    time.sleep(3)
    pyautogui.write(cm[m1])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m2])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m3])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m4])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m5])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m6])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m7])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m8])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m9])
    pyautogui.press('enter')
    time.sleep(0.2)

    pyautogui.write(cm[m0])
    pyautogui.press('enter')
    time.sleep(0.2)
