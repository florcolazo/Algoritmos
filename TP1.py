#5. Desarrollar una función que permita convertir un número romano en un número decimal.
'''
def romano_adecimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    
    for i in range(0, len(romano)):
        if i > 0 or valores[romano[i]] <= valores[romano[i - 1]]:
            resultado += valores[romano[i]]
        else:
            resultado += valores[romano[i]] - 2 * valores[romano[i - 1]]
    return resultado
 
 
romano = input('INGRESE NUMERO ROMANO')
print(romano_adecimal(romano))
'''
'''
#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
decimal=int(input('Ingrese numero a convertir'))
def decimal_abinario(decimal):
    binario= ''
    while decimal// 2!= 0:  #si el cociente  es distinto de 0 #
        binario = str(decimal % 2) + binario  #se asigna a binario el resto#
        decimal = decimal //2
        
    return binario
            

print('Conversion de numero decimal a binario:',decimal_abinario(decimal))       
          
'''

    


#Ejercicio 22
'''
mochila = ['linterna','llaves','campera','sable de luz','botella','galletitas']
elem = input('ingrese elemento a buscar')

def usar_fuerz(mochila,pos):
    if(len(mochila)>pos):
        if(mochila[pos] == elem):
            return  pos
        else:
                return usar_fuerz(mochila,pos+1)
                
    else:
        print('no se encontro el elemento buscado')
        return -1
            
        

        
print('Se encontro el',elem,'despues de sacar',usar_fuerz(mochila,0),'elementos')
'''

#Ejercicio 24

def salida_laberinto(matriz, x, y, caminos=[]):
    
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            print("mover a la derecha")
            salida_laberinto(matriz, x, y+1, caminos)
            print("mover a la izquierda")
            salida_laberinto(matriz, x, y-1, caminos)
            print("mover hacia arriba")
            salida_laberinto(matriz, x-1, y, caminos)
            print("mover hacia abajo")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab =  [[1, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1 ,1, 0, 0, 0],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 2],
      ]
print ('encontraste la salida!:',salida_laberinto(lab, 0, 0))
