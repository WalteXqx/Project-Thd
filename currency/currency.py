# TODO (future) add shop and inventory
# TODO (future) add help list when there is much commands
import random
import time

total = 1000
flag = True
abc = '1234567890'

print('--currency--')
while True:
    print()
    print('1 = check your money, \n2 = flip coins, \n3 = beg to random people, \n4 = earn money from waiting, \nend = end to program (your money will reset)')
    cmd = input('=====>  ')
    print()
    # shows persons money
    if cmd == '1':
        print('##########')
        print('#', str(total).center(6), '#')
        print('##########')

    # flips coins
    elif cmd == '2':
        cf = random.randint(1, 2)

        print('if u win u get double money if u lose u all the money (%50 wins %50 loses)')

        put = input('how much money u would want to put : ')
        print()

        # money correct checker
        for i in put:
            if i not in abc:
                flag = False
        if not flag:
            print('u wrote something wrong')

        else:
            put = int(put)
            if put > total:
                print("u don't have enough money")
                flag = False

        # coin flip if answers
        if cf == 1 and flag:
            total += put * 2
            print('Congratulations! u WON! now u have {} added in your money'.format(put * 2))

        elif cf == 2 and flag:
            total -= put
            print('unfortunately u lose all the money u put')

    # begging system
    elif cmd == '3':
        print()
        tf = random.randint(0, 1)

        # begging good results
        if tf:
            rand = random.randint(1, 4)
            if rand == 1:
                print('a man gave u 10 bucks')
                total += 10
            elif rand == 2:
                print('while u going to beg u found 5 dolar on floor')
                total += 5
            elif rand == 3:
                print('u got a dolar')
                total += 1
            elif rand == 4:
                print('a woman gave u a half eaten sandwich and u sell it for 12 dolar')
                total += 12

        # begging bad results
        else:
            rand = random.randint(1, 4)
            if rand == 1:
                print('nobody gave u money :(')

            elif rand == 2:
                print('a dog barked at u and u gave him 2 bucks????')
                total -= 2

            elif rand == 3:
                print('elon musk gave u 1000 tesla coin but it worthless XD')

            elif rand == 4:
                print('u gave 10 bucks to someone begging bruh')
                total -= 10
    # end system
    elif cmd == 'end':
        print('system closing...')
        print()
        yn = input('r u sure about it? y = yes, n = no : ')
        if yn == 'y':
            break

    # earn for waiting system
    elif cmd == '4':
        print('earn money for waiting', '1 minute = 10 coin', '', sep='\n')
        yn = input('r u sure? 1 = yes, 2 = no : ')
        if yn == '1':
            put = input('how long u want to wait (as minutes) (u cant stop waiting!) : ')

            # money correct checker
            for i in put:
                if i not in abc:
                    flag = False
            if not flag:
                print('u wrote something wrong')

            else:
                put = int(put)
                time.sleep(put / 60)
                total += put * 10
                print('waiting done {} added on your wallet.'.format(put * 10))

    # developer mode system
    elif cmd == 'devmode97':
        print('developer mode activated')
        cmd = input('1 = total changer (will be added more then)')

        # money changer
        if cmd == '1':
            print('total right now : ', total)
            total = int(input('type the total : '))

        else:
            print('u wrote something wrong')

    else:
        print('u wrote something wrong')
    time.sleep(1)
    