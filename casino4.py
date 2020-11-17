from random import randrange
from retry import retry
import select
import sys
import time
import threading



nb_coup=0
solde=10
nb_total1=0
nb_total2=0
nb_total3=0
reussi1=0
reussi2=0
reussi3=0



user_name=input('Je suis Python. Quel est votre pseudo ?')#Definition pseudo



# Definition des règles
print('Bienvenue ',user_name," Vous avez ",solde,"€" """\n
    Nous sommes le """ ,time.ctime(), """"
		\t- Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?\n
	\t- Att : vous avez le droit à trois essais !\n
	\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n
	\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n
	\t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n    
	\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et
	\tvous avez le droit : 
	\t\t- de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
	\t\t- de quitter le jeu.\n
	\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n """ )


nb_ordi1=randrange(0,11,1)#L'ordinateur choisit au hasard un nombre entre 0 et 10
nb_ordi2=randrange(0,21,1)#L'ordinateur choisit au hasard un nombre entre 0 et 20
nb_ordi3=randrange(0,31,1)#L'ordinateur choisit au hasard un nombre entre 0 et 30

"""def timer(t): #Ne fonctionne pas. Ancienne fonction timer
    start = time.time()
    print(start)
    decompte = True
    while decompte : 
        if time.time() - start >= t:
            print("Temps écoulé")
            decompte = False
        else:
            pass"""

"""def close(seconds):
    time.sleep(seconds)
    if time.sleep > 10 :
        sys.exit()
    else: 
        pass"""

mise = int(input("Rentrer votre mise. Maximum 10€, minimum 1€ :€" ))

while mise > solde or mise < 1 : #Définition de la mise
    print("Erreur")
    
    if mise > 10: #Si la mise est trop grande alors on demande au joueur de rentrer une nouvelle valeur
        print("Votre mise est trop grande")
    
    elif mise < 1 : #Si la mise est trop petite alors on demande au joueur de rentrer une nouvelle valeur
        print("Votre mise est trop petite")

    mise = int(input("Rentrer votre mise. Maximum 10€, minimum 1€ :€" ))

while nb_coup<3: #Tant que le nombre de coup est inférieur à 3, alors le joueur peut continuer à jouer
    print(nb_ordi1)
    nb_user=int(input("Entrer un nombre entre 0 et 10 : "))
    """t = threading.Thread(target=close,args=(10,))
    t.start()"""

    if nb_user != nb_ordi1 or nb_user == nb_ordi1:
        nb_total1 = nb_total1 + 1
    
    while nb_user > 10 or nb_user < 0: #Si le nombre donné par le joueur n'est pas compris entre 0 et 10, alors on demande au joueur d'entrer une
                                       #autre valeur

        if nb_user > 10:
            print("La valeur ne peut pas être supérieur à 10")


        if nb_user < 0:
            print("La valeur ne peut pas être inférieur à 0")
            
        nb_user=int(input("Entrer un nombre entre 0 et 10 : "))
    
    nb_coup = nb_coup +1

   

    if nb_coup == 3: #Si le joueur n'a pas trouvé le nombre au bout de 3 essais, alors il on se trouve dans 2 cas

        if nb_user == nb_ordi1: #Si le joueur a trouvé au bout du 3ème essais
            reussi1 = reussi1 + 1
            gain = mise / 2
            solde = solde - mise + gain
            print("Votre nouveau solde est de : ", solde)
            print("Félicitation", user_name, ". Vous avez gagné en {} coup(s)".format(nb_coup))
            niv2=int(input("""Vous pouvez passer au niveau 2. Si vous souhaitez vous continuer taper 1, \n
            sinon taper 0 pour arrêter """))

        if nb_user != nb_ordi1:
            nb_ordi1 = int(nb_ordi1)#Si le joueur n'a pas trouvé au bout du 3ème essais
            print('Le nombre était ' , nb_ordi1)
            solde = solde - mise
            suite=int(input('Vous avez perdu. Voulez-vous essayer à nouveau (Oui = 1 / Non = 0) : '))

            if suite == 1:
                nb_coup=0
                print(solde)
                mise = int(input("Entrer votre mise: €"))
                    
                while mise > solde or mise < 1 : #Si la mise est plus grande que le solde ou plus petite que 1 alors on lui demande de rentrer une nouvelle valeur
                    print("Erreur. Votre solde est de ",solde,"€. Vous ne pouvez excéder cette somme")
                    mise = int(input("Rentrer votre mise. Maximum (voir votre solde) / Minimum 1€ : €")) 

        
            if suite == 0: #Si le joueur ne veut pas rejouer alors le programme s'arrête
                print('Votre nouveau solde est de : €', solde)
                sys.exit()
        

    if nb_user < nb_ordi1: #Si le nombre indiqué par le joueur est plus petit que celui de l'ordinateur
       print('Votre nombre est trop petit')
   
    elif nb_user > nb_ordi1: #Si le nombre indiqué par le joueur est plus grand que celui de l'ordinateur
       print('Votre nombre est trop grand') 

    elif nb_user == nb_ordi1: #Si le joueur gagne en 1 ou 2 essais
        reussi1 = reussi1+1

        if nb_coup == 1:
            gain = mise * 2
            solde = solde - mise + gain
            print(solde)
            print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
            niv2=int(input("""Félicitation,  vous pouvez passer au niveau 2. Si vous souhaiter vous continuer taper 1, \n
            sinon taper 0 pour arrêter """))

        if nb_coup == 2:
            gain = mise - mise
            solde = solde -mise + gain
            print(solde)
            print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
            niv2=int(input("""Vous pouvez passer au niveau 2. Si vous souhaiter vous continuer taper 1, \n
            sinon taper 0 pour arrêter """))


        if niv2==1:
            print("Vous avez mis au total", nb_total1, "essai(s)")
            reussi1 = 100 / nb_total1
            print("Votre pourcentage de réussite est de ", reussi1)
            nb_coup=0
            print("Votre nouveau solde est de : €", solde)
            mise = int(input("Rentrer votre mise. Maximum : votre solde€, minimum 1€ :€" ))
            

            while mise > solde or mise < 1 : #Définition de la mise
                print("Erreur")
    
                if mise > 10: #Si la mise est trop grande alors on demande au joueur de rentrer une nouvelle valeur
                    print("Votre mise est trop grande")
                
                elif mise < 1 : #Si la mise est trop petite alors on demande au joueur de rentrer une nouvelle valeur
                    print("Votre mise est trop petite")

                mise = int(input("Rentrer votre mise. Maximum 10€, minimum 1€ :€" ))
            print(nb_ordi2)

            while nb_coup < 5:

                if nb_user != nb_ordi2 or nb_user == nb_ordi2:
                    nb_total2 = nb_total2 + 1

                while nb_user > 20 or nb_user < 0: #Si le nombre donné par le joueur n'est pas compris entre 0 et 10, alors on demande au joueur d'entrer une
                                       #autre valeur

                    if nb_user > 20:
                        print("La valeur ne peut pas être supérieur à 20")


                    if nb_user < 0:
                        print("La valeur ne peut pas être inférieur à 0")
            
                nb_user=int(input("Entrer un nombre entre 0 et 20 : "))

                nb_coup = nb_coup +1

                if nb_coup == 5:
                    if nb_user == nb_ordi2: #Si le joueur a trouvé au bout du 5ème essais
                        gain = mise * 0.1
                        solde = solde - mise + gain
                        print(solde)
                        niv3=int(input("""Félicitation, vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                        sinon taper 2 pour arrêter """))

                    if nb_user != nb_ordi2:
                        nb_ordi1 = int(nb_ordi1)#Si le joueur n'a pas trouvé au bout du 5ème essais
                        print('Le nombre était ' , nb_ordi1)
                        suite2=int(input('Vous avez perdu. Voulez-vous essayer à nouveau (Oui = 1 / Non = 0) : '))
                        nb_ordi1=randrange(0,11,1)

                        if suite2 == 1: #Si le joueur souhaite rejouer après sa défaite on lui demande d'entrer la mise 
                            nb_coup=0
                            solde = solde-mise
                            print(solde)
                            mise = int(input("Entrer votre mise: €"))
                    
                            while mise > solde or mise < 1 : #Si la mise est plus grande que le solde ou plus petite que 1 alors on lui demande de rentrer une nouvelle valeur
                                print("Erreur. Votre solde est de ",solde,"€. Vous ne pouvez excéder cette somme")
                                mise = int(input("Rentrer votre mise. Maximum (voir votre solde) / Minimum 1€ : €"))   
                        
                        if suite2 == 0: #Si le joueur ne veut pas rejouer alors le programme s'arrête
                            print('Voici votre solde', solde)
                            sys.exit()


    
                

                if nb_user > nb_ordi2:
                    print("Le nombre est trop grand")

                if nb_user < nb_ordi2:
                    print("Le nombre est trop petit")

                if nb_user == nb_ordi2:#Faire les différents cas

                    if nb_coup == 1:
                        gain = mise * 2
                        solde = solde - mise + gain
                        print(solde)
                        print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                        niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                        sinon taper 0 pour arrêter """))

                    if nb_coup == 2:
                        gain = mise * 1.5
                        solde = solde - mise + gain
                        print(solde)
                        print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                        niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                        sinon taper 0 pour arrêter """))

                    if nb_coup == 3:
                        gain = mise * 1
                        solde = solde - mise + gain
                        print(solde)
                        print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                        niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                        sinon taper 0 pour arrêter """))

                    if nb_coup == 4:
                        gain = mise * 0.5
                        solde = solde - mise + gain
                        print(solde)
                        print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                        niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                        sinon taper 0 pour arrêter """))
                    
                    if niv3==1:
                        nb_coup=0
                        nb_total2 = nb_total2 + nb_total1 
                        print('Vous avez mis au total', nb_total2, 'essai(s)')
                        reussi2 = 2 / nb_total2
                        print("Votre pourcentage de réussite est de ", reussi1)

                        print(nb_ordi3)
                        print("Votre nouveau solde est de : €", solde)
                        mise = int(input("Rentrer votre mise. Maximum : votre solde, minimum 1€ :€" ))

                        while mise > solde or mise < 1 : #Définition de la mise
                            print("Erreur")
    
                            if mise > 10: #Si la mise est trop grande alors on demande au joueur de rentrer une nouvelle valeur
                                print("Votre mise est trop grande")
                
                            elif mise < 1 : #Si la mise est trop petite alors on demande au joueur de rentrer une nouvelle valeur
                                print("Votre mise est trop petite")
                        
                        while nb_coup < 7:


                            nb_user=int(input("Entrer un nombre entre 0 et 30 : "))

                            while nb_user > 30 or nb_user < 0: #Si le nombre donné par le joueur n'est pas compris entre 0 et 10, alors on demande au joueur d'entrer une
                                       #autre valeur

                                if nb_user > 30:
                                    print("La valeur ne peut pas être supérieur à 30")


                                if nb_user < 0:
                                    print("La valeur ne peut pas être inférieur à 0")
                
                                nb_user=int(input("Entrer un nombre entre 0 et 30 : "))
                            
                            nb_coup = nb_coup + 1
                            if nb_user != nb_ordi3 or nb_user == nb_ordi3:
                                nb_total3 = nb_total3 + 1

                            if nb_coup == 7: #Si le joueur n'a pas trouvé le nombre au bout de 3 essais, alors il on se trouve dans 2 cas

                                if nb_user == nb_ordi3: #Si le joueur a trouvé au bout du 3ème essais
                                    gain = mise * 0.25
                                    solde = solde - mise + gain
                                    print("Votre nouveau sole est de : ", solde)
                                    print("Félicitation", user_name, ". Vous avez gagné en {} coup(s)".format(nb_coup))
                                    continuer=int(input(""" Si vous souhaitez vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_user != nb_ordi3:
                                    nb_ordi1 = int(nb_ordi1)#Si le joueur n'a pas trouvé au bout du 3ème essais
                                    print('Le nombre était ' , nb_ordi1)
                                    suite3=int(input('Vous avez perdu. Voulez-vous essayer à nouveau (Oui = 1 / Non = 0) : '))
                                    

                                    if suite3 == 1: #Si le joueur souhaite rejouer après sa défaite on lui demande d'entrer la mise 
                                        nb_ordi3=randrange(0,31,1)
                                        nb_coup=0
                                        solde = solde-mise
                                        print(solde)
                                        mise = int(input("Entrer votre mise: €"))
                                        
                                        while mise > solde or mise < 1 : #Si la mise est plus grande que le solde ou plus petite que 1 alors on lui demande de rentrer une nouvelle valeur
                                            print("Erreur. Votre solde est de ",solde,"€. Vous ne pouvez excéder cette somme")
                                            mise = int(input("Rentrer votre mise. Maximum (voir votre solde) / Minimum 1€ : €"))
                        
                

                                    if suite3 == 0: #Si le joueur ne veut pas rejouer alors le programme s'arrête
                                        print('Votre nouveau solde est de : €', solde)
                                        sys.exit()

                            if nb_user > nb_ordi3:
                                print("Le nombre est trop grand")

                            if nb_user < nb_ordi3:
                                print("Le nombre est trop petit")

                            if nb_user == nb_ordi3:
                                reussi3 = reussi3 + 1

                                if nb_coup == 1:
                                    gain = mise * 3
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_coup == 2:
                                    gain = mise * 2.5
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_coup == 3:
                                    gain = mise * 2
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_coup == 4:
                                    gain = mise * 1
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_coup == 5:
                                    gain = mise * 0.75
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))

                                if nb_coup == 6:
                                    gain = mise * 0.5
                                    solde = solde - mise + gain
                                    print(solde)
                                    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))
                                    niv3=int(input("""Félicitation,  vous pouvez passer au niveau 3. Si vous souhaiter vous continuer taper 1, \n
                                    sinon taper 0 pour arrêter """))
                                
                                if niv3 == 1:
                                    nb_coup==0
                                    nb_ordi3 = randrange(0,31,1)
                                    print("Votre nouveau solde est de €", solde)
                                    mise = int(input("Entrer votre mise: €"))
                                        
                                    while mise > solde or mise < 1 : #Si la mise est plus grande que le solde ou plus petite que 1 alors on lui demande de rentrer une nouvelle valeur
                                        print("Erreur. Votre solde est de ",solde,"€. Vous ne pouvez excéder cette somme")
                                        mise = int(input("Rentrer votre mise. Maximum (voir votre solde) / Minimum 1€ : €"))


                                if niv3==0:
                                    print('Voici votre solde: €', solde)
                                    nb_total3 = nb_total3 + nb_total2 + nb_total1
                                    print('Vous avez mis au total', nb_total3, 'essai(s)')
                                    reussi3 = (reussi1 + reussi2 + reussi3) / (nb_total1 + nb_total2 + nb_total3)
                                    print("Votre pourcentage de reussite est de : ", reussi3)
                                    sys.exit()

      
                    if niv3==0:
                        print('Voici votre solde: €', solde)

                        sys.exit()

        if niv2==0:
            print("Votre nouveau solde est de", solde,"€.")
            print('Vous avez mis au total', nb_total1, 'essai(s)')
            reussi2=1 / (nb_total1 )
            print("Votre pourcentage de reussite est de : ", reussi2)
            sys.exit()

    else :
        print('Erreur')
        nb_user=int(input("Entrer un nombre entre 0 et 10 : "))

if nb_user == nb_ordi1: #Quand le joueur gagne, on indique le nombre de coup(s)
    print("Félicitation", user_name, "Vous avez gagné en {} coup(s)".format(nb_coup))

if nb_user != nb_ordi1: #Que le joueur perde ou gagne, on indique la nombre qu'il fallait trouver.
    nb_ordi1=str(nb_ordi1)
    print('Le nombre était ', nb_ordi1)
    nb_ordi1=int(nb_ordi1)



