#coding:utf-8
""" commencons par afficher du texte """

print("bonjout tout le monde !")

""" les variable """

""" int
    float
    str
    bool
"""

age_Personne = 18 
nom_Personne = "ASSION"
taille = 1.87
valeur = True
 
""" afficher le type des variables """

print(type(age_Personne))
print(type(nom_Personne))
print(type(taille))
print(type(valeur))


""" afficher le contenu de la variable """

print(age_Personne)

""" ajouter texte en affichant la valeur de la variable """

print("le nom de la personne est:", nom_Personne,".")

""" affichage avec technique format """

texte = "l'age de la personne est {} et sa taille est {} mettres"
print(texte.format(age_Personne, taille))
print("le nom de la personne est {} et sa valeur est {}".format(nom_Personne, valeur))

""" lire au clavier """

prenom = input(" votre prenom svp:\n")

"""caster la variable """

prenom = str(prenom)

print("l'utilisateur actuel est : {} {}".format(nom_Personne, prenom))


"""condition et boucle"""
print("Choisissez votre operation:\n")
print("1-S'identifier.")
print("2-Verifier une lettre.")
print("3-Faire un calcule.")
print("4-Exit")

plateforme = True
while plateforme:
    operation = input(">")
    operation = int(operation)
    if operation == 1:
        """and/or"""
        
        connexion = True
        while connexion:
            user_id = "guillaume"
            passWord = "88443678"
            identifiant = input("entrer votr id: ")
            mot_de_passe = input("taper votre mots de passe: ")
            if identifiant == user_id and mot_de_passe == passWord :
                print("vous etes connectés", identifiant)
                connexion = False
            else:
                print("identifiant ou mots de passe incorrect!")
        print("Merci")
    elif operation == 2:
        """in/not_in"""
        
        check = True
        check = bool(check)
        while check:
            print("Entrez une lettre:\n" )
            print("Tapez out pour quitter.\n")
            lettre = input(">")
            if lettre in "aeyuioAEIYOU":
                print("c'est une voyelle.")
                continue
            elif lettre in "0123456789":
                print("ce n'est pas une lettre c'est un chiffre.")
                continue
            elif lettre in "zrtpmlkjhgfdqswxcvbZRTPMLKJHGFDSQWXCVBN":
                print("c'est une consone.")
                continue
            elif lettre == "out":
                break
            else:
                lettre = input("Evitez ca !!! Entrez une lettre:\n")
        print("Merci")
    elif operation == 3:
        """ petite calculatrice """
        
        print("choisissez votre operation:\n")
        print("1-Addition:\n")
        print("2-Soustration:\n")
        print("3-Mutiplication:\n")
        print("4-Division:\n")
        print("5-Modulo:\n")
        print("6-Exit \n")

       
        calcule = True
        while calcule:
            choix = input("> ")
            choix = int(choix)
            a = input("Entrez le premier nombre:\n")
            a = float(a)
            b = input("Entrez le second nombre:\n")
            b = float(b)
            if choix == 1:
                print("Resultat =  " ,a + b)
                continue
            elif choix == 2:
                print("Resultat = " ,a - b)
                continue
            elif choix == 3:
                print("Resultat = " ,a * b)
                continue
            elif choix == 4:
                print("Resultat = " ,a / b)
                continue
            elif choix == 5:
                print("Resultat = " ,a % b)
                continue
            elif choix == 6:
                break
            else:
                choix = input("Choisissez entre 1 et 5 :\n")
        print("Merci")
    elif operation == 4:
        break
    else:
        print("choissisez entre 1 et 3:\n")
print("Merci")