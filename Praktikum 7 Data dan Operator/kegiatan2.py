x = input('masukkan password: ')
if x == 'Zanzibar':
    print('Correct')
else:
    x = input('wrong, Please input again: ')
    if x == 'Zanzibar':
        print('Correct')
    else:
        x = input('wrong, please input again: ')
        if x == 'Zanzibar':
            print('Correct')
        else:
            print('Acces has been blocked')
