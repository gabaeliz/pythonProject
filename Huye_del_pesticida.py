import random

print("Sal de los departamentos antes de que sea demasiado tarde\n"
      "----------------------------------------------------------\n"
      "Eres un pequeño conejillo de indias, que vive en un bloque de departamentos con su pequeño dueño.\n"
      "Un fin de semana tu dueño y tu deben de dejar los departamentos debido a una grave infestación de cucarachas.\n" 
      "Tu dueño te mete a tu transportadora... o eso cree.\n"
      "En tu lugar coloca a una cucaracha disfrazada de ti. Ahora es tu deber salir antes de que llegue el equipo\n"
      "de fumigación y acabe con todo... incluido tu.\n Sales del departamento y te encuentras con dos pasillos,\n"
      "desconoces a donde van pues nunca has salido del departamento: el primero te lleva a la izquierda y el segundo\n" 
      "a la derecha. ¿Cual eliges? ")

opcion = input("A.- Pasillo a la izquierda / B.- Pasillo a la derecha ")
if opcion == "B":
    print("El pasillo te lleva hasta un elevador. Coges el elevador:\n")
    opcion = input("A.- Si /  B.-No")
    if opcion == "A":
        print("Entras al elevador y las puertas se cierran...mueres intoxicado. Recuerda: los conejillos de indias no saben leer. FIN\n")
        exit()
    elif opcion == "B":
        print("Sigues por el pasillo hasta encontrarte una ventana que 	da directo a la calle. Estas de suerte, decides bajar por\n"
              "la escalera de emergencia, ves pasar a tu dueño, estas a salvo. FIN")
        exit()

elif opcion == "A":
    print("El pasillo te lleva a unas escaleras, Decides bajar las escaleras:\n")
    opcion = input("A.- Si / B.- No")
    if opcion == "A":
      print("Decides bajar las escaleras, te encuentras a un tierno chihuahua que ha aceptado su final. Pero, antes \n"
             "solo quiere tener una charla. ¿Aceptas la charla con el?")
      opcion = input("A.- Si / B.- No")
      if opcion == "A":
            print("Resulta que el chihuahua es un amante de las matemáticas y tiene un ultimo deseo, que tu realices una operación matemática:\n" 
            "¿Aceptas el reto?\n")
      opcion = input("A.- Si / B.- No")
    elif opcion == "B":
      print("Decides no bajar las escaleras, de repente una manada de cucarachas hambrienta y salvaje se acerca a ti, es tu fin... mueres. FIN")
      exit()


if opcion == "A":
    numero_random_chihuahua = random.randint(1,100)
    print("Decides aceptar el reto. Cuanto es 7 * {}".format(numero_random_chihuahua))
    opcion = int(input("Cual es el resultado:"))
    if opcion == 7 * numero_random_chihuahua:
       print("Felicidades, acertaste a la respuesta, pero te tengo noticias...\n El chihuahua es un embustero, no sabe de matematicas,\n" 
             "te ha engañado, credulo. Mueres, te ha dado un infarto del coraje. FIN")
       exit()
    else:
       print("No acertaste, era de esperar... eres un conejillo de indias. Sigues el pasillo donde encuentras una manzana, tienes hambre.\n"
              "Te comes la manzana?\n")
opcion = input("A.- Si / B.- No")
if opcion == "A":
         print("Bienvenido al cielo de los conejillos de indias, has sido envenenado. FIN")
         exit()
elif opcion == "B":
     print("Bien hecho, la manzana contenia veneno. A lo lejos ves a tu dueño ha	regresado por ti ganaste.FIN")
     exit()
elif opcion == "B":
     print("Sigues de largo. Bien hecho, ese chihuahua es un embustero. Como si los chihuahuas supieran matematicas. Felicidades, tu dueño se ha\n"
           "dado cuenta del engaño y regresa por ti. Has ganado! FIN")
exit()



