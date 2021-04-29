print("Enter a option.\n""1 for English\n""2 para Español")
language = input("Option:")
if language == "1":
    print("Choose a text to play:\n"
          "1 - A day at the zoo!\n"
          "2 - The fun park!\n"
          "3 - At the arcade!")
    option = input("Option:")
    if option == "1":
        words = int(12)
        word1 = input(str(words) + ") Please enter a adjective:").lower()
        words = words - 1
        word2 = input(str(words) + ") Please enter a noun:").lower()
        words = words - 1
        word3 = input(str(words) + ") Please enter a verb past tense:").lower()
        words = words - 1
        word4 = input(str(words) + ") Please enter a adverb:").lower()
        words = words - 1
        word5 = input(str(words) + ") Please enter a adjective:").lower()
        words = words - 1
        word6 = input(str(words) + ") Please enter a noun:").lower()
        words = words - 1
        word7 = input(str(words) + ") Please enter a noun:").lower()
        words = words - 1
        word8 = input(str(words) + ") Please enter a adjective:").lower()
        words = words - 1
        word9 = input(str(words) + ") Please enter a verb:").lower()
        words = words - 1
        word10 = input(str(words) + ") Please enter a adverb:").lower()
        words = words - 1
        word11 = input(str(words) + ") Please enter a verb past tense:").lower()
        words = words - 1
        word12 = input(str(words) + ") Please enter a adjective:").lower()
        print("Today I went to the zoo. I saw a "+word1+" "+word2+" jumping up and down in its tree.\n"
            "He "+word3+" "+word4+" through the large tunnel that led to its "+word5+" "+word6+".\n"
            "I got some peanuts and passed them though the cage to a gigantic gray "+word7+" towering above my head. \n"
            "Feeding that animal made me hungry. I went to get a "+word8+" scoop of ice cream.\n"
            " It filled my stomach. Afterwards I had to "+word9+" "+word10+" to catch our bus.\n"
            "When I got home I "+word11+" my mom for a "+word12+ " day at the zoo.")

elif language == "2":
    print("Español")
    print("Seleccione un texto para jugar:\n"
          "1 - Un día en el zoólogico.\n"
          "2 - El parque divertido.\n"
          "3 - En las salas de videojuegos.")
    option = input("Option:")
    if option == "1":
        words = int(12)
        word1 = input(str(words) + ") Ingrese un sustantivo:").lower()
        words = words - 1
        word2 = input(str(words) + ") Ingrese un adjetivo:").lower()
        words = words - 1
        word3 = input(str(words) + ") Ingrese un verbo pasado:").lower()
        words = words - 1
        word4 = input(str(words) + ") Ingrese un adverbo:").lower()
        words = words - 1
        word5 = input(str(words) + ") Ingrese un sustantivo:").lower()
        words = words - 1
        word6 = input(str(words) + ") Ingrese un adjetivo:").lower()
        words = words - 1
        word7 = input(str(words) + ") Ingrese un sustantivo:").lower()
        words = words - 1
        word8 = input(str(words) + ") Ingrese un adjetivo:").lower()
        words = words - 1
        word9 = input(str(words) + ") Ingrese un verbo:").lower()
        words = words - 1
        word10 = input(str(words) + ") Ingrese un adverbio:").lower()
        words = words - 1
        word11 = input(str(words) + ") Ingrese un verbo pasado:").lower()
        words = words - 1
        word12 = input(str(words) + ") Ingrese un verbo adjetivo:").lower()
        words = words - 1

        print("Hoy fui al zoólogico. Vi un "+word1+" "+word2+" saltando arriba y abajo en su árbol.\n"
                "Él "+word3 +" "+word4+" a través del largo túnel que lleva a su "+word5+" "+word6+".\n"
                "Conseguí algo de manis y se los pasé a través de una jaula a un "+word7+" gigante gris imponente sobre mi cabeza.\n"
                "Alimentar a ese animal me hizo hambriento. Fui a conseguir una pelota de helado "+word8+".\n"
                "Llenó mi estómago. Después tuve que "+word9+" "+word10+" para alcanzar nuestro bus.\n"
                "Cuando llegué a casa, "+word11+" a mi mamá por un "+word12+" día en el zoólogico.")
else:
    print("Choose a valid option\n"
          "Seleccione una opción válida")
