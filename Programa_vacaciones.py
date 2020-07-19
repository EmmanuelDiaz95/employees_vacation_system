print('=============================================================')
print('Conoce los dias de vacaciones a los que tienes derecho')
print('=============================================================')

nombre = input('\n¿Cual es tu nombre?: ')
clave = int(input('\n¿Cual es la clave de tu departamento?: '))
antiguedad = int(input('\n¿Cuantos años tienes trabajando en la empresa?: '))

if clave == 1 and antiguedad == 1:
    print('\nFelicidades', nombre, 'tienes 6 dias de vacaciones')
    print('\nFin.')

elif clave == 1 and antiguedad <= 6:
    print('\nFeliciades', nombre, 'tienes 14 dias de vacaciones')
    print('\nFin.')

elif clave == 1 and antiguedad >= 7:
    print('\nFelicidades', nombre, 'tienes 20 dias de vacaciones\n')
    print('Fin')

else:
    
    if clave == 2 and antiguedad == 1:
        print('\nFelicidades', nombre, 'tienes 7 dias de vacaciones')
        print('\nFin.')

    elif clave == 2 and antiguedad <= 6:
        print('\nFeliciades', nombre, 'tienes 15 dias de vacaciones')
        print('\nFin.')
    
    elif clave == 2 and antiguedad >= 7:
        print('\nFelicidades', nombre, 'tienes 22 dias de vacaciones')
        print('\nFin.')

    else:

        if clave == 3 and antiguedad == 1:
            print('\nFelicidades', nombre, 'tienes 10 dias de vacaciones')
            print('\nFin.')

        elif clave == 3 and antiguedad <= 6:
            print('\nFeliciades', nombre, 'tienes 20 dias de vacaciones')
            print('\nFin.')

        elif clave == 3 and antiguedad >= 7:
            print('\nFelicidades', nombre, 'tienes 30 dias de vacaciones')
            print('\nFin.')
        else:
            print('Sin derecho a vacaciones')
            print('Fin.')

            
            

    
            
    

    
    
