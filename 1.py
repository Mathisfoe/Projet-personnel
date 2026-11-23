bonjour = input("Bonjour, tu t'appelles : ")

age = int(input("Tu as(age) : "))

if age <= 14:
    print("Tu n'as pas l'age requis")
else:
    print("Tu peux continuer")
    
    # On met tout en minuscules avec .lower() pour éviter les problèmes de majuscules
    sport = input("Quel est ton sport (Football, Natation ou Boxe) : ").lower()

    if sport == "football":
        print("Mettre le programme de foot")
    elif sport == "natation":
        print("Mettre le programme de natation")
    elif sport == "boxe":
        print("Mettre le programme de boxe")
    else:
        print("Nous n'avons pas de programme pour cette discipline")




