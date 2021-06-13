'''ejercicio11 Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
b. indicar el plantea natal de Luke Skywalker y Han Solo
c. insertar un nuevo personaje antes del maestro Yoda
d. eliminar el personaje ubicado después de Jar Jar Binks'''



from cola import Cola

'''

cola_personaje = Cola()
class Personaje(object):

    
    def __init__(self,nombre,planeta):
        self.nombre = nombre
        self.planeta = planeta
        


    def __str__(self):
        return self.nombre + '-'+str(self.planeta)

cola_personaje = Cola()

personaje_StarW = Personaje('Luke Skywalker','Tatooine')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Sheev Palpatine','Nabbo')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Yoda','Dagobah ')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Jar Binks','Endor')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Leia Organa','Alderaan')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Mace Windu','Tierra')
cola_personaje.arribo(personaje_StarW)
personaje_StarW = Personaje('Han Solo','Dagobah')
cola_personaje.arribo(personaje_StarW)

# mostrar los personajes del planeta Alderaan, Endor y Tatooine
cola_aux = Cola()
cantidad_elemento = 0
while (cantidad_elemento <cola_personaje.tamanio ()):
    dato = cola_personaje.mover_final()
    cantidad_elemento+=1
    if (dato.planeta== 'Alderaan'):
            print('Personaje del planeta',dato.planeta,':',dato.nombre)
    if (dato.planeta== 'Endor'):
            print('Personaje del planeta',dato.planeta,':',dato.nombre)
    elif (dato.planeta== 'Tatooine'):
            print('Personaje del planeta',dato.planeta,':',dato.nombre)
            #. indicar el plantea natal de Luke Skywalker y Han Solo
    
    if (dato.nombre== 'Luke Skywalker'):
            print('Personaje',dato.nombre,'es del planeta natal:',dato.planeta)
    elif (dato.nombre== 'Han Solo'):
            print('personaje',dato.nombre,'es del planeta natal:',dato.planeta)
    if (dato.nombre == 'Yoda'):
        cola_personaje.arribo(Personaje('NUEVO','PLANETA'))
    #d. eliminar el personaje ubicado después de Jar Jar Binks
    if (dato.nombre == 'Jar Binks'):
        cola_personaje.atencion()


cola_aux =Cola()
while (not cola_personaje.cola_vacia()):
            dato = cola_personaje.atencion()
            cola_aux.arribo(dato)
            print(cola_aux.atencion())


            
'''   

#12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
#nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#ni métodos de ordenamiento.

cola_uno = Cola()
cola_dos = Cola()
cola_valores_ordenados = Cola()
caux = Cola()


datos1= [7,15,26,41,85,94]
datos2= [4,21,24,36,54,89]



cola_uno.arribo(datos1)
cola_dos.arribo(datos2)



while(not cola_uno.cola_vacia()):
    datos_cola1= cola_uno.atencion()
    while(not cola_dos.cola_vacia()):
        datos_cola2=cola_dos.atencion()
        if(datos_cola1 < datos_cola2):
            cola_valores_ordenados.arribo(datos_cola1)
        caux.arribo(datos_cola2)
    while (not caux.cola_vacia()):
        cola_dos.arribo(caux.atencion())
        cola_valores_ordenados.arribo(cola_dos.atencion())
        


cantidad_elementos=0
while(cantidad_elementos < cola_valores_ordenados.tamanio()):
    datos = cola_valores_ordenados.mover_final()

    print(datos)
    cantidad_elementos+=1 



"""  while(not cola_uno.cola_vacia()):
        dato = cola_uno.en_frente()
        while(not cola_dos.en_frente()):
            dato2 = cola_dos.en_frente() 
            if(dato < dato2):
                cola_valores_ordenados.arribo(dato)


elementos=0
while(elementos < cola_valores_ordenados.tamanio()):
    datos = cola_valores_ordenados.mover_final()

    print(datos)
    elementos+=1
"""

#2. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
#F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.
'''
cola_personajes_marvel = Cola()

class Personaje_Marvel(object):
    def __init__(self,personaje,superheroe,genero):
            self.personaje = personaje
            self.superheroe = superheroe
            self.genero = genero

    
    def __str__(self):
        return self.personaje+ '-'+str(self.superheroe)+'-'+str(self.genero)


personaje_Marvel = Personaje_Marvel('Peter Benjamin Parker','Spider-Man','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Natalia Alianovna Romanova​ ','Viuda Negra','F')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Matthew Michael​ ','Daredevil','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Carol Danvers','Capitana Marvel','F')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Gal Gadot','Mujer Maravilla ','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Scott Lang','Hombre Hormiga','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('David Thewlis','Ares','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Soldier','Rajeev Pahuja','M')
cola_personajes_marvel.arribo(personaje_Marvel)
personaje_Marvel = Personaje_Marvel('Lisa Loven','Menalippe','F')
cola_personajes_marvel.arribo(personaje_Marvel)





while(not cola_personajes_marvel.cola_vacia()):
    dato = cola_personajes_marvel.atencion()
    if (dato.superheroe == 'Capitana Marvel'):
        print('Personaje:',dato.personaje,'-Superheroe:',dato.superheroe)
    #b. mostrar los nombre de los superhéroes femeninos;
    if (dato.genero=='F'):
        print('Superheroes de generos femeninos:',dato.superheroe)
    #c. mostrar los nombres de los personajes masculinos;
    if (dato.genero=='M'):
        print('Superheroes de generos masculinos:',dato.superheroe)
    #d. determinar el nombre del superhéroe del personaje Scott Lang;
    if (dato.personaje =='Scott Lang'):
            print('nombre del superhéroe del personaje',dato.personaje,':',dato.superheroe)
    #e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S
    if (dato.personaje[0] =='S') or dato.superheroe[0]=='S':
            print('datos de personaje o superheroe cuyo nombre empieza con S:','-Personaje:',dato.personaje,'-Superheroe:',dato.superheroe,'Genero:',dato.genero)
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.
    if (dato.personaje=='Carol Danvers'):
        print('El personaje',dato.personaje,'se encuentra en la Cola ','.Personaje que representa',dato.superheroe)
    


    
    

    

cantidad_elemento=0
while (not cantidad_elemento<cola_personajes_marvel.tamanio()):
            datos = cola_personajes_marvel.mover_final()
            cantidad_elemento+=1
            print(datos)
'''