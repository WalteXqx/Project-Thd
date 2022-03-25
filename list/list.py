



List = []

while True:
    print()
    print('1 = show list, 2 = add something to list, 3 = remove something from list, 4 = end code')

    dec = input('input : ')

    # show list==========
    if dec == '1':
        print(List)

    # add to list=========
    elif dec == '2':
        add = input('what you want to add? (keep blank to cancel) : ')

        while True:

            # cancels by leaving blank===========
            if not add:
                break

            print()
            dec1 = input('do you want this to add to last?\n(keep blank to cancel)\ny = yes, n = no : ')

            # add to last=========
            if not dec1:
                break

            elif dec1 == 'y':
                List.append(add)
                break

            # add anywhere=========
            elif dec1 == 'n':
                while True:
                    dec1 = input('what number you want add this to?\n(keep blan to cancel) : ')

                    # cancels by keeping blank =========
                    if not dec1:
                        break

                    # add to anywhere int error=========
                    try:
                        dec1 = int(dec1)

                    except ValueError:
                        print('please only input number')

                    else:
                        List.insert(dec1 - 1, add)
                        break
                break

            else:
                print('you wrote something wrong\n')

    # remove from list===========
    elif dec == '3':
        while True:

            # decide remove with name or number=========
            print()
            print('do you want to remove with name or number,\n(keep blank to cancel)\n1 = name, 2 = number')
            dec1 = input('input : ')

            if not dec1:
                break

            # remove with name ==============
            if dec1 == '1':
                dec1 = input('what you want to remove\n(keep blank to cancel) : ')

                if not dec1:
                    break

                # name existed test==========
                if dec1 in List:
                    List.remove(dec1)
                    break

                else:
                    print('this is not exist in list')

            # remove with number ===========
            elif dec1 == '2':
                dec1 = input('what number you want remove to \n(keep blank to cancel) : ')

                if not dec1:
                    break

                try:
                    dec1 = int(dec1)

                except ValueError:
                    print('please only input numbers')

                else:
                    List.remove(List[dec1 - 1])
                    break

            else:
                print('you wrote something wrong')

    elif dec == '4':
        while True:
            dec1 = input('are you sure you want to quit (list will be gone), y = yes, n = no :')
            if dec1 == 'y':
                print('system quiting', end='')
                quit()

            elif dec1 == 'n':
                break

            else:
                print('you wrote something wrong')
    else:
        print('you wrote something wrong')
