import msvcrt

pressed = msvcrt.getch().decode('utf-8')

if str(pressed) == 'p':
    print('almog')
else:
    print('Pressed: ' + str(pressed))