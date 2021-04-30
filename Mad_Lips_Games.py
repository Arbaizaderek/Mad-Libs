import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.GREEN + "Enter a option.\n""1 for English\n""2 para Español")
language = input("Option:")
if language == "1":
    print(Fore.GREEN + "Choose a text to play:\n"
                       "1 - A day at the zoo!\n"
                       "2 - The fun park!\n"
                       "3 - At the arcade!")
    option = input("Option:")
    if option == "1":
        words = int(12)
        word1 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adjective: ").lower()
        words = words - 1
        word2 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word3 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a verb past tense: ").lower()
        words = words - 1
        word4 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adverb: ").lower()
        words = words - 1
        word5 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adjective: ").lower()
        words = words - 1
        word6 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word7 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word8 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adjective:").lower()
        words = words - 1
        word9 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a verb:").lower()
        words = words - 1
        word10 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adverb:").lower()
        words = words - 1
        word11 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a verb past tense:").lower()
        words = words - 1
        word12 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a adjective:").lower()
        print(
            Fore.LIGHTWHITE_EX + "Today I went to the zoo. I saw a " + Fore.MAGENTA + word1 + " " + word2 + Fore.LIGHTWHITE_EX + " jumping up and down in its tree.\n"
                                                                                                                                 "He " + Fore.MAGENTA + word3 + " " + word4 + Fore.LIGHTWHITE_EX + " through the large tunnel that led to its " + Fore.MAGENTA + word5 + " " + word6 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                            "I got some peanuts and passed them though the cage to a gigantic gray " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + " towering above my head. \n"
                                                                                                                                                                                                                                                                                                                                                                                                                                   "Feeding that animal made me hungry. I went to get a " + Fore.MAGENTA + word8 + Fore.LIGHTWHITE_EX + " scoop of ice cream.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "It filled my stomach. Afterwards I had to " + Fore.MAGENTA + word9 + " " + word10 + Fore.LIGHTWHITE_EX + " to catch our bus.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "When I got home I " + Fore.MAGENTA + word11 + Fore.LIGHTWHITE_EX + " my mom for a " + Fore.MAGENTA + word12 + Fore.LIGHTWHITE_EX + " day at the zoo.")
    elif option == "2":
        words = int(10)
        word1 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adjective: ").lower()
        words = words - 1
        word2 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a plural noun: ").lower()
        words = words - 1
        word3 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word4 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adverb: ").lower()
        words = words - 1
        word5 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a number: ").lower()
        words = words - 1
        word6 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a past tense verb: ").lower()
        words = words - 1
        word7 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a adjective: ").lower()
        words = words - 1
        word8 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a past tense verb: ").lower()
        words = words - 1
        word9 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adverb: ").lower()
        words = words - 1
        word10 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter an adjective: ").lower()
        words = words - 1
        print(
            "Today, my fabulous camp group went to a " + Fore.MAGENTA + word1 + Fore.LIGHTWHITE_EX + " amusement park.\n"
                                                                                                     "It was a fun park with lots of cool " + Fore.MAGENTA + word2 + Fore.LIGHTWHITE_EX + " and enjoyable play structures. \n"
                                                                                                                                                                                          "When we got there, my kind counselor shouted loudly, 'Everybody off the " + Fore.MAGENTA + word3 + Fore.LIGHTWHITE_EX + "'.\n"
                                                                                                                                                                                                                                                                                                                   "We all pushed out in a terrible hurry.\n"
                                                                                                                                                                                                                                                                                                                   "My counselor handed out yellow tickets, and we scurried in. \n"
                                                                                                                                                                                                                                                                                                                   "I was so excited! I couldn't figure out what exciting thing to do first. \n"
                                                                                                                                                                                                                                                                                                                   "I saw a scary roller coaster I really liked so, I " + Fore.MAGENTA + word4 + Fore.LIGHTWHITE_EX + " ran over to get in the long line that had about " + Fore.MAGENTA + word5 + Fore.LIGHTWHITE_EX + " people in it. \n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "When I finally got on the roller coaster I was " + Fore.MAGENTA + word6 + Fore.LIGHTWHITE_EX + ". In fact I was so nervous my two knees were knocking together. \n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "This was the " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + " ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. \n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      "That’s when the ride began! When I got to the bottom, I was a little " + Fore.MAGENTA + word8 + Fore.LIGHTWHITE_EX + " but I was proud of myself. \n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "The rest of the day went " + Fore.MAGENTA + word9 + Fore.LIGHTWHITE_EX + " It was a " + Fore.MAGENTA + word10 + Fore.LIGHTWHITE_EX + "  day at the fun park.")
    elif option == "3":
        words = int(8)
        word1 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a plural noun: ").lower()
        words = words - 1
        word2 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a plural noun: ").lower()
        words = words - 1
        word3 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a verb: ").lower()
        words = words - 1
        word4 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word5 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a verb: ").lower()
        words = words - 1
        word6 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a plural noun: ").lower()
        words = words - 1
        word7 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a noun: ").lower()
        words = words - 1
        word8 = input(Fore.LIGHTWHITE_EX + str(words) + ") Please enter a plural noun: ").lower()
        words = words - 1
        print(
            "When I go to the arcade with my " + Fore.MAGENTA + word1 + Fore.LIGHTWHITE_EX + " there are lots of games to play. I spend lots of time there with my friends.\n"
                                                                                             "In the game X-Men you can be different " + Fore.MAGENTA + word2 + Fore.LIGHTWHITE_EX + ". The point of the game is to " + Fore.MAGENTA + word3 + Fore.LIGHTWHITE_EX + " every robot.\n"
                                                                                                                                                                                                                                                                    "You also need to save people. Then you can go to the next level.\n"
                                                                                                                                                                                                                                                                    "In the game Star Wars you are Luke Skywalker and you try to destroy every " + Fore.MAGENTA + word4 + Fore.LIGHTWHITE_EX + ". \n"
                                                                                                                                                                                                                                                                                                                                                                                               "In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are " + Fore.MAGENTA + word5 + Fore.LIGHTWHITE_EX + " against.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "There are a whole lot of other cool games. When you play some games you win " + Fore.MAGENTA + word6 + Fore.LIGHTWHITE_EX + " for certain scores.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "Once you're done you can cash in your tickets to get a big " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + ". You can save your " + Fore.MAGENTA + word8 + Fore.LIGHTWHITE_EX + " for another time.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "When I went to this arcade I didn't believe how much fun it would be.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "So far I have had a lot of fun every time I've been to this great arcade! ")
    else:
        print(Fore.RED + "Please choose a valid option.")


elif language == "2":
    print("Seleccione un texto para jugar:\n"
          "1 - Un día en el zoólogico.\n"
          "2 - El parque de diversiones.\n"
          "3 - En las salas de videojuegos.")
    option = input("Option:")
    if option == "1":
        words = int(12)
        word1 = input(str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word2 = input(str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word3 = input(str(words) + ") Ingrese un verbo pasado: ").capitalize()
        words = words - 1
        word4 = input(str(words) + ") Ingrese un adverbio: ").lower()
        words = words - 1
        word5 = input(str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word6 = input(str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word7 = input(str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word8 = input(str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word9 = input(str(words) + ") Ingrese un verbo: ").lower()
        words = words - 1
        word10 = input(str(words) + ") Ingrese un adverbio: ").lower()
        words = words - 1
        word11 = input(str(words) + ") Ingrese un verbo en primera persona: ").lower()
        words = words - 1
        word12 = input(str(words) + ") Ingrese un verbo adjetivo: ").lower()
        words = words - 1

        print(
            "Hoy fui al zoólogico. Vi un " + Fore.MAGENTA + word1 + Fore.LIGHTWHITE_EX + " " + Fore.MAGENTA + word2 + Fore.LIGHTWHITE_EX + " saltando arriba y abajo en su árbol.\n"
                                                                                                                                           "" + Fore.MAGENTA + word3 + " " + word4 + Fore.LIGHTWHITE_EX + " a través del largo túnel que lleva a su " + Fore.MAGENTA + word5 + " " + word6 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                  "Conseguí algo de manis y se los pasé a través de una jaula a un " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + " gigante gris imponente sobre mi cabeza.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                   "Alimentar a ese animal me hizo hambriento. Fui a conseguir una pelota de helado " + Fore.MAGENTA + word8 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "Llenó mi estómago. Después tuve que " + Fore.MAGENTA + word9 + " " + word10 + Fore.LIGHTWHITE_EX + " para alcanzar nuestro bus.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "Cuando llegué a casa, " + Fore.MAGENTA + word11 + Fore.LIGHTWHITE_EX + " a mi mamá por un " + Fore.MAGENTA + word12 + Fore.LIGHTWHITE_EX + " día en el zoólogico.")
    elif option == "2":
        words = int(10)
        word1 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word2 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo plural: ").lower()
        words = words - 1
        word3 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word4 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adverbio: ").lower()
        words = words - 1
        word5 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un número: ").lower()
        words = words - 1
        word6 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word7 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word8 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adjetivo: ").lower()
        words = words - 1
        word9 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un adverbio: ").lower()
        words = words - 1
        word10 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese adjetivo: ").lower()
        words = words - 1
        print(
            "Hoy, mi fabuloso grupo de campo fue a un " + Fore.MAGENTA + word1 + Fore.LIGHTWHITE_EX + " parque de diversiones.\n"
                                                                                                      "Fue un parque divertido con un montón de " + Fore.MAGENTA + word2 + Fore.LIGHTWHITE_EX + " espectaculares y estructuras de juego para disfrutar.\n"
                                                                                                                                                                                                "Cuando llegamos ahí, mi amable consejero gritó fuertemente 'Todos afuera de " + Fore.MAGENTA + word3 + Fore.LIGHTWHITE_EX + ".'\n"
                                                                                                                                                                                                                                                                                                                             "Todos nos salimos en un terrible apuro. Mi consejero entregó ticketes amarillos e ingresamos.\n"
                                                                                                                                                                                                                                                                                                                             "Estaba tan emocionado. No podía entender que cosa emocionante hacer primero.\n"
                                                                                                                                                                                                                                                                                                                             "Vi una montaña rusa que realmente me gustó, entonces, yo " + Fore.MAGENTA + word4 + Fore.LIGHTWHITE_EX + " corrí para entrar en la fila que tenía acerca de " + Fore.MAGENTA + word5 + Fore.LIGHTWHITE_EX + " personas.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          "Cuando finalmente llegué a la montaña rusa estaba " + Fore.MAGENTA + word6 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "De hecho estaba tan nervioso que mis rodillas se tocaban.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "Este fue el viaje que más he estado " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "Acerca de dos minutos, escucho palancas y engranajes. Ahí fue cuando el viaje comenzó.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "Cuando estaba en el fondo, estaba un poco " + Fore.MAGENTA + word8 + Fore.LIGHTWHITE_EX + " pero estaba orgulloso de mi mismo.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             "El resto del día fue " + Fore.MAGENTA + word9 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   "Fue un día " + Fore.MAGENTA + word10 + Fore.LIGHTWHITE_EX + " en el parque de diversiones.")
    elif option == "3":
        words = int(8)
        word1 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo plural: ").lower()
        words = words - 1
        word2 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo plural: ").lower()
        words = words - 1
        word3 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un verbo: ").lower()
        words = words - 1
        word4 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word5 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un verbo: ").lower()
        words = words - 1
        word6 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo plural: ").lower()
        words = words - 1
        word7 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo: ").lower()
        words = words - 1
        word8 = input(Fore.LIGHTWHITE_EX + str(words) + ") Ingrese un sustantivo plural: ").lower()
        words = words - 1
        print(
            "Cuando voy al centro de videojuegos con mis " + Fore.MAGENTA + word1 + Fore.LIGHTWHITE_EX + " hay muchos juegos que jugar.\n"
                                                                                                         "Paso mucho tiempo ahí con mis amigos.\n"
                                                                                                         "En el juego de X-Men puedes ser diferentes " + Fore.MAGENTA + word2 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                     "El objetivo del juego es " + Fore.MAGENTA + word3 + Fore.LIGHTWHITE_EX + " cada robot.\n"
                                                                                                                                                                                                                                                                               "También se necesita salvar persona. Entonces puedes ir al siguiente nivel.\n"
                                                                                                                                                                                                                                                                               "En el juego de Star Wars eres Luke Skywalker y tratas de destruir cada " + Fore.MAGENTA + word4 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                       "En el de carreras, necesitas vencer cada vehículo computarizado que estas " + Fore.MAGENTA + word5 + Fore.LIGHTWHITE_EX + " en contra.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "Hay un montón de otros juegos divertidos.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  "Cuando ganas en juegos, ganas " + Fore.MAGENTA + word6 + Fore.LIGHTWHITE_EX + " por cierto puntaje.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 "Se pueden canjear por un gran " + Fore.MAGENTA + word7 + Fore.LIGHTWHITE_EX + ".\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "Puedes guardar tus " + Fore.MAGENTA + word6 + Fore.LIGHTWHITE_EX + " para otra ocasión.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "Cuando yo fui al centro de videojuegos, no creía que tan divertido sería.\n"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "Hasta ahora, he tenido un monton de diversión cada vez que he estado en este genial centro de videojuegos.")

    else:
        print(Fore.RED + "Ingrese una opción válida.")

else:
    print(Fore.RED + "Choose a valid option\n"
                     "Seleccione una opción válida")
