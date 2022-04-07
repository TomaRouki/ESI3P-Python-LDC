########################################################################################################################
####                                        Projet Python : Ligue  des Champions                                    ####
####                                        Réalisé par : De Sousa Thomas  
####                                                      Mohamed Jaouni
########################################################################################################################

########################################################################################################################
####                                            Importation des modules                                             ####
########################################################################################################################
import pygame
import random
########################################################################################################################
####                                   Liste des 32 équipes de la Ligue des Champions                               ####
########################################################################################################################

liste_equipes = [
    "Chelsea",
    "Bayern Munich",
    "Manchester City",
    "Atlético de Madrid",
    "Villarreal",
    "Inter",
    "Sporting CP",
    "Lille",
    "Real Madrid",
    "FC Barcelone",
    "Juventus",
    "Manchester United",
    "Paris SG",
    "Liverpool",
    "Séville FC",
    "Borussia Dortmund",
    "Ajax",
    "FC Porto",
    "RB Leipzig",
    "Atalanta",
    "Zenith",
    "Club Brugge",
    "Besiktas",
    "Dynamo Kiev",
    "AC Milan",
    "VfL Wolfsbourg",
    "Malmö",
    "YB Berne",
    "Benfica",
    "Salzbourg",
    "Shakhtar",
    "Sheriff",
]

########################################################################################################################
####                                       Détermination des différents seeds                                       ####
########################################################################################################################

# Chapeau 1
list_seeds_1 = ["Manchester City", #ENG 
                "Atlético de Madrid", #ESP 
                "Sporting", #POR
                "Inter", #IT
                "Bayern Munich", #GER 
                "Lille", #FR                 
                "Chelsea", #ENG
                "Villarreal", #ESP
]

# Chapeau 2
list_seeds_2 = ["Paris SG", #FR
                "Liverpool", #ENG
                "Borussia Dortmund", #GER
                "Real Madrid", #ESP 
                "FC Barcelone", #ESP
                "Séville FC", #ESP                         
                "Manchester United", #ENG                
                "Juventus", #IT
]

# Chapeau 3
list_seeds_3 = ["RB Leipzig", #GER
                "FC Porto", #POR
                "Ajax", #ESP
                "Shakhtar", #UK
                "Benfica", #POR
                "Salzbourg", #GER               
                "Atalanta", #IT         
                "Zenith", #IT
                
]

# Chapeau 4
list_seeds_4 = ["Club Bruges", #BEL
               "AC Milan", #IT
               "Besiktas", #TUR
               "Sheriff", #MOL
               "Dynamo Kiev", #UK               
               "VfL Wolfsbourg", #GER
               "YB Berne", #SUI  
               "Malmö", #SWE
               
]

########################################################################################################################
####                            On a attribue à chaque poule une équipe de chaque chapeau                           ####
########################################################################################################################

# Poule A
list_poule_A =  [[list_seeds_1[0],0,0],
                [list_seeds_2[0],0,0],
                [list_seeds_3[0],0,0],
                [list_seeds_4[0],0,0]]

# Poule B
list_poule_B = [[list_seeds_1[1],0,0],
                [list_seeds_2[1],0,0],
                [list_seeds_3[1],0,0],
                [list_seeds_4[1],0,0]]

# Poule C
list_poule_C = [[list_seeds_1[2],0,0],
                [list_seeds_2[2],0,0],
                [list_seeds_3[2],0,0],
                [list_seeds_4[2],0,0]]

# Poule D
list_poule_D = [[list_seeds_1[3],0,0],
                [list_seeds_2[3],0,0],
                [list_seeds_3[3],0,0],
                [list_seeds_4[3],0,0]]

# Poule E
list_poule_E = [[list_seeds_1[4],0,0],
                [list_seeds_2[4],0,0],
                [list_seeds_3[4],0,0],
                [list_seeds_4[4],0,0]]

# Poule F
list_poule_F = [[list_seeds_1[5],0,0],
                [list_seeds_2[5],0,0],
                [list_seeds_3[5],0,0],
                [list_seeds_4[5],0,0]]

# Poule G
list_poule_G = [[list_seeds_1[6],0,0],
                [list_seeds_2[6],0,0],
                [list_seeds_3[6],0,0],
                [list_seeds_4[6],0,0]]
# Poule H
list_poule_H = [[list_seeds_1[7],0,0],
                [list_seeds_2[7],0,0],
                [list_seeds_3[7],0,0],
                [list_seeds_4[7],0,0]]

########################################################################################################################
####                                            Listes des fonctions                                                ####
########################################################################################################################

# Fonction qui permet de faire jouer les équipes d'une poule contre les autres sans les faire jouer contre eux-même
def match_poule(list_poule):
    # On crée une liste qui va contenir les différents matchs de la poule A
    list_match_poule = []
    # Chaque équipe joue une fois contre toutes les autres équipes de son chapeau sauf contre lui même
    for i in range(0, len(list_poule)):
        for j in range(0, len(list_poule)):
            # Il n'est pas possible de jouer contre lui même
            if i != j:
                # On crée une liste pour chaque match
                list_match_poule.append([list_poule[i], list_poule[j]])
    return list_match_poule
# Fonction qui permet de voir l'intégralité des matchs aller et retour d'une poule
def affichage_match_aller_retour(list_match_poule, poule):
    # On affiche les matchs de la poule
    print("\nMatchs aller - retour de la poule "+ poule)
    for i in range(0, len(list_match_poule)):
        print(list_match_poule[i][0][0] + " - " + list_match_poule[i][1][0])
# Fonction qui permet de voir l'intégralité des matchs aller d'une poule en comptabilisant les points et les buts de chaque équipe
def affichage_match_aller(list_match_poule, poule):
    # On affiche les matchs aller 
    # Première journée
    print("\nMatch aller de la première journée de la poule "+ poule)
    # Match aller A
    print(list_match_poule[0][0][0],"vs" ,list_match_poule[0][1][0])
    # Créer un score aléatoire pour le match aller A
    score_match_aller_A = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_A[0],"-",score_match_aller_A[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_A[0] > score_match_aller_A[1]) :
        print("Victoire de",list_match_poule[0][0][0])
        list_match_poule[0][0][1] += 3
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[0][0][2] += score_match_aller_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[0][1][2] += score_match_aller_A[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_A[0] == score_match_aller_A[1]) :
        print("Match nul")
        list_match_poule[0][0][1] += 1
        list_match_poule[0][1][1] += 1
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[0][0][2] += score_match_aller_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[0][1][2] += score_match_aller_A[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[0][1][0])
        list_match_poule[0][1][1] += 3
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[0][0][2] += score_match_aller_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[0][1][2] += score_match_aller_A[1]

    # Match aller B
    print(list_match_poule[11][0][0],"vs" ,list_match_poule[11][1][0]) 
    # Créer un score aléatoire pour le match aller B
    score_match_aller_B = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_B[0],"-",score_match_aller_B[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_B[0] > score_match_aller_B[1]) :
        print("Victoire de",list_match_poule[11][0][0])
        list_match_poule[11][0][1] += 3
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[11][0][2] += score_match_aller_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[11][1][2] += score_match_aller_B[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_B[0] == score_match_aller_B[1]) :
        print("Match nul")
        list_match_poule[11][0][1] += 1
        list_match_poule[11][1][1] += 1
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[11][0][2] += score_match_aller_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[11][1][2] += score_match_aller_B[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[11][1][0])
        list_match_poule[11][1][1] += 3
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[11][0][2] += score_match_aller_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[11][1][2] += score_match_aller_B[1]
    
    
    # Deuxième journée
    print("\nMatch aller de la deuxième journée de la poule "+ poule)
    # Match aller C
    print(list_match_poule[1][0][0],"vs" ,list_match_poule[1][1][0]) 
    # Créer un score aléatoire pour le match aller C
    score_match_aller_C = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_C[0],"-",score_match_aller_C[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_C[0] > score_match_aller_C[1]) :
        print("Victoire de",list_match_poule[1][0][0])
        list_match_poule[1][0][1] += 3
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[1][0][2] += score_match_aller_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[1][1][2] += score_match_aller_C[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_C[0] == score_match_aller_C[1]) :
        print("Match nul")
        list_match_poule[1][0][1] += 1
        list_match_poule[1][1][1] += 1
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[1][0][2] += score_match_aller_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[1][1][2] += score_match_aller_C[1]
    # Si le score de la première équipe est inférieur à la seconde alors	
    else:
        print("Victoire de",list_match_poule[1][1][0])
        list_match_poule[1][1][1] += 3
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[1][0][2] += score_match_aller_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[1][1][2] += score_match_aller_C[1]
        
    # Match aller D
    print(list_match_poule[10][0][0],"vs" ,list_match_poule[10][1][0])
    # Créer un score aléatoire pour le match aller D
    score_match_aller_D = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_D[0],"-",score_match_aller_D[1]) 
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_D[0] > score_match_aller_D[1]) :
        print("Victoire de",list_match_poule[10][0][0])
        list_match_poule[10][0][1] += 3
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[10][0][2] += score_match_aller_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[10][1][2] += score_match_aller_D[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_D[0] == score_match_aller_D[1]) :
        print("Match nul")
        list_match_poule[10][0][1] += 1
        list_match_poule[10][1][1] += 1
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[10][0][2] += score_match_aller_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[10][1][2] += score_match_aller_D[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[10][1][0])
        list_match_poule[10][1][1] += 3
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[10][0][2] += score_match_aller_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[10][1][2] += score_match_aller_D[1]
    
    # Troisième journée
    print("\nMatch aller de la troisième journée de la poule "+ poule)
    # Match aller E
    print(list_match_poule[2][0][0],"vs" ,list_match_poule[2][1][0]) 
    # Créer un score aléatoire pour le match aller E
    score_match_aller_E = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_E[0],"-",score_match_aller_E[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_E[0] > score_match_aller_E[1]) :
        print("Victoire de",list_match_poule[2][0][0])
        list_match_poule[2][0][1] += 3
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[2][0][2] += score_match_aller_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[2][1][2] += score_match_aller_E[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_E[0] == score_match_aller_E[1]) :
        print("Match nul")
        list_match_poule[2][0][1] += 1
        list_match_poule[2][1][1] += 1
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[2][0][2] += score_match_aller_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[2][1][2] += score_match_aller_E[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[2][1][0])
        list_match_poule[2][1][1] += 3
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[2][0][2] += score_match_aller_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[2][1][2] += score_match_aller_E[1]
        
    # Match aller F
    print(list_match_poule[7][0][0],"vs" ,list_match_poule[7][1][0]) 
    # Créer un score aléatoire pour le match aller F
    score_match_aller_F = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_aller_F[0],"-",score_match_aller_F[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_aller_F[0] > score_match_aller_F[1]) :
        print("Victoire de",list_match_poule[7][0][0])
        list_match_poule[7][0][1] += 3
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[7][0][2] += score_match_aller_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[7][1][2] += score_match_aller_F[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_aller_F[0] == score_match_aller_F[1]) :
        print("Match nul")
        list_match_poule[7][0][1] += 1
        list_match_poule[7][1][1] += 1
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[7][0][2] += score_match_aller_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[7][1][2] += score_match_aller_F[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[7][1][0])
        list_match_poule[7][1][1] += 3
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[7][0][2] += score_match_aller_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[7][1][2] += score_match_aller_F[1]
# Fonction qui permet de voir l'intégralité des matchs retour d'une poule en comptabilisant les points et les buts de chaque équipe
def affichage_match_retour(list_match_poule, poule):
    # On affiche les matchs retour 
    # Quatrième journée
    print("\nMatch retour de la quatrième journée de la poule "+ poule)
    # Match retour A
    print(list_match_poule[3][0][0],"vs" ,list_match_poule[3][1][0]) 
    # Créer un score aléatoire pour le match retour A
    score_match_retour_A = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_A[0],"-",score_match_retour_A[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_A[0] > score_match_retour_A[1]) :
        print("Victoire de",list_match_poule[3][0][0])
        list_match_poule[3][0][1] += 3
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[3][0][2] += score_match_retour_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[3][1][2] += score_match_retour_A[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_A[0] == score_match_retour_A[1]) :
        print("Match nul")
        list_match_poule[3][0][1] += 1
        list_match_poule[3][1][1] += 1
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[3][0][2] += score_match_retour_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[3][1][2] += score_match_retour_A[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[3][1][0])
        list_match_poule[3][1][1] += 3
        # On attribue score_match_A[0] à la première équipe
        list_match_poule[3][0][2] += score_match_retour_A[0]
        # On attribue score_match_A[1] à la seconde équipe
        list_match_poule[3][1][2] += score_match_retour_A[1]
        
    # Match retour B
    print(list_match_poule[8][0][0],"vs" ,list_match_poule[8][1][0]) 
    # Créer un score aléatoire pour le match retour B
    score_match_retour_B = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_B[0],"-",score_match_retour_B[1])
     # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_B[0] > score_match_retour_B[1]) :
        print("Victoire de",list_match_poule[8][0][0])
        list_match_poule[8][0][1] += 3
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[8][0][2] += score_match_retour_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[8][1][2] += score_match_retour_B[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_B[0] == score_match_retour_B[1]) :
        print("Match nul")
        list_match_poule[8][0][1] += 1
        list_match_poule[8][1][1] += 1
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[8][0][2] += score_match_retour_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[8][1][2] += score_match_retour_B[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[8][1][0])
        list_match_poule[8][1][1] += 3
        # On attribue score_match_B[0] à la première équipe
        list_match_poule[8][0][2] += score_match_retour_B[0]
        # On attribue score_match_B[1] à la seconde équipe
        list_match_poule[8][1][2] += score_match_retour_B[1]
    
    # Cinquième journée
    print("\nMatch retour de la cinquième journée de la poule "+ poule)
    # Match retour C
    print(list_match_poule[4][0][0],"vs" ,list_match_poule[4][1][0])
    # Créer un score aléatoire pour le match retour C
    score_match_retour_C = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_C[0],"-",score_match_retour_C[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_C[0] > score_match_retour_C[1]) :
        print("Victoire de",list_match_poule[4][0][0])
        list_match_poule[4][0][1] += 3
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[4][0][2] += score_match_retour_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[4][1][2] += score_match_retour_C[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_C[0] == score_match_retour_C[1]) :
        print("Match nul")
        list_match_poule[4][0][1] += 1
        list_match_poule[4][1][1] += 1
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[4][0][2] += score_match_retour_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[4][1][2] += score_match_retour_C[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[4][1][0])
        list_match_poule[4][1][1] += 3
        # On attribue score_match_C[0] à la première équipe
        list_match_poule[4][0][2] += score_match_retour_C[0]
        # On attribue score_match_C[1] à la seconde équipe
        list_match_poule[4][1][2] += score_match_retour_C[1]
        
    # Match retour D
    print(list_match_poule[9][0][0],"vs" ,list_match_poule[9][1][0]) 
    # Créer un score aléatoire pour le match retour D
    score_match_retour_D = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_D[0],"-",score_match_retour_D[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_D[0] > score_match_retour_D[1]) :
        print("Victoire de",list_match_poule[9][0][0])
        list_match_poule[9][0][1] += 3
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[9][0][2] += score_match_retour_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[9][1][2] += score_match_retour_D[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_D[0] == score_match_retour_D[1]) :
        print("Match nul")
        list_match_poule[9][0][1] += 1
        list_match_poule[9][1][1] += 1
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[9][0][2] += score_match_retour_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[9][1][2] += score_match_retour_D[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[9][1][0])
        list_match_poule[9][1][1] += 3
        # On attribue score_match_D[0] à la première équipe
        list_match_poule[9][0][2] += score_match_retour_D[0]
        # On attribue score_match_D[1] à la seconde équipe
        list_match_poule[9][1][2] += score_match_retour_D[1]
        
    # Sixième journée
    print("\nMatch retour de la sixième journée de la poule "+ poule)
    # Match retour E
    print(list_match_poule[5][0][0],"vs" ,list_match_poule[5][1][0]) 
    # Créer un score aléatoire pour le match retour E
    score_match_retour_E = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_E[0],"-",score_match_retour_E[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_E[0] > score_match_retour_E[1]) :
        print("Victoire de",list_match_poule[5][0][0])
        list_match_poule[5][0][1] += 3
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[5][0][2] += score_match_retour_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[5][1][2] += score_match_retour_E[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_E[0] == score_match_retour_E[1]) :
        print("Match nul")
        list_match_poule[5][0][1] += 1
        list_match_poule[5][1][1] += 1
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[5][0][2] += score_match_retour_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[5][1][2] += score_match_retour_E[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[5][1][0])
        list_match_poule[5][1][1] += 3
        # On attribue score_match_E[0] à la première équipe
        list_match_poule[5][0][2] += score_match_retour_E[0]
        # On attribue score_match_E[1] à la seconde équipe
        list_match_poule[5][1][2] += score_match_retour_E[1]
    # Match retour F
    print(list_match_poule[6][0][0],"vs" ,list_match_poule[6][1][0])
    # Créer un score aléatoire pour le match retour F
    score_match_retour_F = [random.randint(0,4), random.randint(0,4)]
    print("Score :",score_match_retour_F[0],"-",score_match_retour_F[1])
    # Insertion des points pour le classement
    # Si le score de la première équipe est supérieur à la seconde alors 
    if(score_match_retour_F[0] > score_match_retour_F[1]) :
        print("Victoire de",list_match_poule[6][0][0])
        list_match_poule[6][0][1] += 3
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[6][0][2] += score_match_retour_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[6][1][2] += score_match_retour_F[1]
    # Si les deux équipes ont le même score alors
    elif(score_match_retour_F[0] == score_match_retour_F[1]) :
        print("Match nul")
        list_match_poule[6][0][1] += 1
        list_match_poule[6][1][1] += 1
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[6][0][2] += score_match_retour_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[6][1][2] += score_match_retour_F[1]
    # Si le score de la première équipe est inférieur à la seconde alors
    else:
        print("Victoire de",list_match_poule[6][1][0])
        list_match_poule[6][1][1] += 3
        # On attribue score_match_F[0] à la première équipe
        list_match_poule[6][0][2] += score_match_retour_F[0]
        # On attribue score_match_F[1] à la seconde équipe
        list_match_poule[6][1][2] += score_match_retour_F[1]
# Fonction qui permet d'afficher le classement d'une poule en la triant par ordre décroissant des points et des buts
def affichage_classement(list_poule, poule):
    print("\nClassement de la poule "+ poule)
    # On affiche les matchs de la poule par ordre décroissant des points et des buts
    list_poule.sort(key=lambda x:(x[1],x[2]), reverse=True)
    for i in range(len(list_poule)):
        print(list_poule[i][0],":", list_poule[i][1],"pts", list_poule[i][2],"buts")
# Fonction qui selectionne les deux premiers de la poule par ordre décroissant de leur score et leur buts
def selection_huitieme(list_poule, poule):
    print("\nVoici les deux équipes qualifiés en huitième de la poule "+ poule)
    # On affiche les deux premiers de la poule par ordre décroissant des points et des buts
    list_poule.sort(key=lambda x:(x[1],x[2]), reverse=True)
    for i in range(2):
        print(list_poule[i][0],"avec", list_poule[i][1],"pts","et", list_poule[i][2],"buts")
    # Boucle qui met dans une list les deux premiers de la poule
    list_huitieme = []
    for i in range(2):
        # On ajoute les deux premiers de la poule dans une liste
        list_huitieme.append(list_poule[i])
    return list_huitieme
# Fonction qui permet de mettre les deux premiers de chaque poule dans une seul list
def affichage_equipe_huitiemes(list_huitieme_A, list_huitieme_B, list_huitieme_C, list_huitieme_D, list_huitieme_E, list_huitieme_F, list_huitieme_G, list_huitieme_H):
    # On crée une list vide qui va contenir les deux premiers de chaque poule
    list_huitieme = []
    # On ajoute les deux premiers de chaque poule dans la liste
    for i in range(2):
        list_huitieme.append(list_huitieme_A[i])
        list_huitieme.append(list_huitieme_B[i])
        list_huitieme.append(list_huitieme_C[i])
        list_huitieme.append(list_huitieme_D[i])
        list_huitieme.append(list_huitieme_E[i])
        list_huitieme.append(list_huitieme_F[i])
        list_huitieme.append(list_huitieme_G[i])
        list_huitieme.append(list_huitieme_H[i])
    # On affiche la liste des 16 équipes qualifiés en huitième de finale avec un retour a la ligne
    for i in range(len(list_huitieme)):
        print(list_huitieme[i][0])
    return list_huitieme
# Fonction qui permet de voir l'intégralité des matchs aller et retour des huitièmes de finale
def match_huitieme(list_huitieme):
    # On mélange la liste
    list_huitieme_rdm = random.sample(list_huitieme, len(list_huitieme))
    # On crée des binomes pour faire jouer les équipes de huitième de finale
    list_match_huitieme = [list_huitieme_rdm[i:i+2] for i in range(0, len(list_huitieme_rdm), 2)]
    # Affichage des 8 matchs de huitième de finale
    for i in range(len(list_match_huitieme)):
        print("Match", i+1, ":", list_match_huitieme[i][0][0],"vs", list_match_huitieme[i][1][0])
    return list_match_huitieme
# Fonction qui permet de voir l'intégralité des matchs aller des huitièmes de finale 
def match_aller_huitieme(list_huitieme):
    print("Match aller des huitièmes de finale")
    print("\n")
    # On crée un list qui va contenir les scores de tout les matchs
    list_score_match_aller_huitieme = []
    for i in range(len(list_huitieme)):
        # On affiche les équipes qui jouent en aller
        print("Match aller",i+1, ":",list_huitieme[i][0][0],"vs", list_huitieme[i][1][0])
        # On crée un score aléatoire 
        score_match_aller_huitieme = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_aller_huitieme[0], "-", score_match_aller_huitieme[1])
        # On crée une liste vide qui va contenir tout les scores des matchs aller
        # Si le score de la première équipe est supérieur à la seconde alors
        if(score_match_aller_huitieme[0] > score_match_aller_huitieme[1]):
            # On ajoute les buts marqués par la première équipe
            list_huitieme[i][0][2] += score_match_aller_huitieme[0]
            # On ajoute les buts marqués par la seconde équipe
            list_huitieme[i][1][2] += score_match_aller_huitieme[1]
            # On ajoute le score du match dans la liste list_score_match_aller_huitieme
            list_score_match_aller_huitieme.append(score_match_aller_huitieme)
        # Si les deux équipes ont le même score alors
        elif(score_match_aller_huitieme[0] == score_match_aller_huitieme[1]):
            # On ajoute les buts marqués par la première équipe
            list_huitieme[i][0][2] += score_match_aller_huitieme[0]
            # On ajoute les buts marqués par la seconde équipe
            list_huitieme[i][1][2] += score_match_aller_huitieme[1]
            # On ajoute le score du match dans la liste list_score_match_aller_huitieme
            list_score_match_aller_huitieme.append(score_match_aller_huitieme)
        # Si le score de la première équipe est inférieur à la seconde alors
        else:
            # On ajoute les buts marqués par la première équipe
            list_huitieme[i][0][2] += score_match_aller_huitieme[0]
            # On ajoute les buts marqués par la seconde équipe
            list_huitieme[i][1][2] += score_match_aller_huitieme[1]
            # On ajoute le score du match dans la liste list_score_match_aller_huitieme
            list_score_match_aller_huitieme.append(score_match_aller_huitieme)
    return list_score_match_aller_huitieme
# Fonction qui permet de voir l'intégralité des matchs retour des huitièmes de finale 
def match_retour_huitieme(list_huitieme):
    print("Match retour des huitièmes de finale")
    print("\n")
    # On crée un list qui va contenir les scores de tout les matchs
    list_score_match_retour_huitieme = []
    # On crée une list list_score_match_retour_huitieme qui va contenir la somme des buts des matchs aller et retour
    list_score_match_aller_retour_huitieme = []
    for i in range(len(list_huitieme)):
        # On affiche les équipes qui jouent en retour
        print("Match retour",i+1, ":",list_huitieme[i][0][0],"vs", list_huitieme[i][1][0])
        # On crée un score aléatoire 
        score_match_retour_huitieme = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_retour_huitieme[0], "-", score_match_retour_huitieme[1])
        list_huitieme[i][0][2] += score_match_retour_huitieme[0]
         # On ajoute les buts marqués par la seconde équipe
        list_huitieme[i][1][2] += score_match_retour_huitieme[1]  
        # On ajoute le score du match dans la list score_match_retour_huitieme
        list_score_match_retour_huitieme.append(score_match_retour_huitieme) 
        # On ajoute les buts 
        list_score_match_aller_retour_huitieme.append(list_score_match_aller_huitieme[i][0] + list_score_match_retour_huitieme[i][0])
        list_score_match_aller_retour_huitieme.append(list_score_match_aller_huitieme[i][1] + list_score_match_retour_huitieme[i][1])
        # Si les deux équipes ont le même score alors
        list_score_final_huitieme = []
    print("\n")
    list_quart = []
    for i in range(len(list_score_match_retour_huitieme)):
        # On met les scores des matchs dans la list x
        x = []
        x.append(list_score_match_aller_huitieme[i][0] + list_score_match_retour_huitieme[i][0])
        x.append(list_score_match_aller_huitieme[i][1] + list_score_match_retour_huitieme[i][1])
        # Puis dans list_score_final_huitieme
        list_score_final_huitieme.append(x)
        # On regarde si la première équipe a gagné en fonction du cumul des buts marqués
        if(list_score_final_huitieme[i][0] > list_score_final_huitieme[i][1]):
            print("Vainqueur du match",i+1,":",list_huitieme[i][0][0],"vs", list_huitieme[i][1][0])
            print(list_huitieme[i][0][0],"après addition du score")
            # On ajoute le gagnant a la liste list_quart
            list_quart.append(list_huitieme[i][0][0]) 
        # Si les deux équipes ont le même score alors 
            print("\n")
        elif(list_score_final_huitieme[i][0] == list_score_final_huitieme[i][1]):
            print("Vainqueur du match",i+1,":",list_huitieme[i][0][0],"vs", list_huitieme[i][1][0])
            # On fait un tirage au sort pour connaitre le gagant
            penalty = random.randint(0,1)
            if(penalty == 0):
                print(list_huitieme[i][0][0],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_quart
                list_quart.append(list_huitieme[i][0][0]) 
                print("\n")
            else:
                print(list_huitieme[i][1][0],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_quart
                list_quart.append(list_huitieme[i][1][0])
                print("\n")
        # On regarde si la deuxième équipe a gagné en fonction du cumul des buts marqués
        else:
            print("Vainqueur du match",i+1,":",list_huitieme[i][0][0],"vs", list_huitieme[i][1][0])
            print(list_huitieme[i][1][0],"après addition du score")
            # On ajoute le gagnant a la liste list_quart
            list_quart.append(list_huitieme[i][1][0])
            print("\n")
    return list_quart
# Fonction qui permet d'afficher les qualifiés pour les quarts de finale
def affichage_equipe_quart(list_quart):
    for i in range(len(list_quart)):
        print(list_quart[i])
    print("\n")
    return list_quart
# Fonction qui permet de voir l'intégralité des matchs aller et retour des quarts de finale
def match_quart(list_quart):
    # On mélange la liste
    list_quart_rdm = random.sample(list_quart, len(list_quart))
    # On crée des binomes pour faire jouer les équipes de quart de finale
    list_match_quart = [list_quart_rdm[i:i+2] for i in range(0, len(list_quart_rdm), 2)]
    # Affichage des 4 matchs des quarts de finale
    for i in range(len(list_match_quart)):
        print("Match", i+1, ":", list_match_quart[i][0],"vs", list_match_quart[i][1])
    return list_match_quart
# Fontion qui permet de voir l'intégralité des matchs aller des quarts de finale en comptabilisant les points et les buts de chaque équipe
def match_aller_quart(list_quart):
    print("Match aller des quarts de finale")
    print("\n")
    # On crée un list qui va contenir les scores des matchs aller
    list_score_match_aller_quart = []
    for i in range(len(list_quart)):
        # On affich les matchs aller des quarts de finale
        print("Match aller",i+1, ":",list_quart[i][0],"vs", list_quart[i][1])
        # On crée un score aléatoire 
        score_match_aller_quart = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_aller_quart[0], "-", score_match_aller_quart[1])
        # On ajoute les scores dans la liste
        list_score_match_aller_quart.append(score_match_aller_quart)
    return list_score_match_aller_quart
# Fontion qui permet de voir l'intégralité des matchs retour des quarts de finale en comptabilisant les points et les buts de chaque équipe
def match_retour_quart(list_quart):
    print("Match retour des quarts de finale")
    print("\n")
    # On crée un list qui va contenir les scores du matchs retour
    list_score_match_retour_quart = []
    # On crée une list list_score_match_retour_quart qui va contenir les scores des matchs aller et retour des quarts 
    list_score_match_aller_retour_quart = []
    for i in range(len(list_quart)):
        # On affiche les équipes qui jouent en retour
        print("Match retour",i+1, ":",list_quart[i][0],"vs", list_quart[i][1])
        # On crée un score aléatoire 
        score_match_retour_quart = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_retour_quart[0], "-", score_match_retour_quart[1])
        # On ajoute le score du match dans la list score_match_retour_quart
        list_score_match_retour_quart.append(score_match_retour_quart) 
        # On ajoute les 2 scores des 2 mêmes matchs dans la liste list_score_match_aller_retour_quart
        list_score_match_aller_retour_quart.append(list_score_match_aller_quart[i][0] + list_score_match_retour_quart[i][0])
        list_score_match_aller_retour_quart.append(list_score_match_aller_quart[i][1] + list_score_match_retour_quart[i][1])
        # On crée un list qui va contenir les scores des matchs aller et retour des quarts
        list_score_final_quart = []
    print("\n")
    list_demi = []
    for i in range(len(list_score_match_retour_quart)):
        # On met les scores des matchs dans la list x
        x = []
        x.append(list_score_match_aller_quart[i][0] + list_score_match_retour_quart[i][0])
        x.append(list_score_match_aller_quart[i][1] + list_score_match_retour_quart[i][1])
        # Puis dans list_score_final_quart
        list_score_final_quart.append(x)
        # On regarde si la première équipe a gagné en fonction du cumul des buts marqués
        if(list_score_final_quart[i][0] > list_score_final_quart[i][1]):
            print("Vainqueur du match",i+1,":",list_quart[i][0],"vs", list_quart[i][1])
            print(list_quart[i][0],"après addition du score")
            # On ajoute le gagnant a la liste list_quart
            list_demi.append(list_quart[i][0]) 
            print("\n")
        # Si les deux équipes ont le même score alors 
        elif(list_score_final_quart[i][0] == list_score_final_quart[i][1]):
            print("Vainqueur du match",i+1,":",list_quart[i][0],"vs", list_quart[i][1])
            # On fait un tirage au sort pour connaitre le gagant
            penalty = random.randint(0,1)
            if(penalty == 0):
                print(list_quart[i][0],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_quart
                list_demi.append(list_quart[i][0]) 
                print("\n")
            else:
                print(list_quart[i][1],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_quart
                list_demi.append(list_quart[i][1])
                print("\n")
        # On regarde si la deuxième équipe a gagné en fonction du cumul des buts marqués
        else:
            print("Vainqueur du match",i+1,":",list_quart[i][0],"vs", list_quart[i][1])
            print(list_quart[i][1],"après addition du score")
            # On ajoute le gagnant a la liste list_quart
            list_demi.append(list_quart[i][1])
            print("\n")
    return list_demi
# Fonction qui permet d'afficher les qualifiés pour les demi-finales
def affichage_equipe_demi(list_demi):
    for i in range(len(list_demi)):
        print(list_demi[i])
    print("\n")
    return list_demi
# Fonction qui permet de voir l'intégralité des matchs aller et retour des demi-finales
def match_demi(list_demi):
    # On mélange la liste
    list_demi_rdm = random.sample(list_demi, len(list_demi))
    # On crée des binomes pour faire jouer les équipes de demi de finale
    list_match_demi = [list_demi_rdm[i:i+2] for i in range(0, len(list_demi_rdm), 2)]
    # Affichage des 4 matchs des demis de finale
    for i in range(len(list_match_demi)):
        print("Match", i+1, ":", list_match_demi[i][0],"vs", list_match_demi[i][1])
    return list_match_demi
# Fontion qui permet de voir l'intégralité des matchs aller des demi-finales en comptabilisant les points et les buts de chaque équipe
def match_aller_demi(list_demi):
    print("Match aller des demi-finales")
    print("\n")
    # On crée un list qui va contenir les scores des matchs aller
    list_score_match_aller_demi = []
    for i in range(len(list_demi)):
        # On affich les matchs aller des demis de finale
        print("Match aller",i+1, ":",list_demi[i][0],"vs", list_demi[i][1])
        # On crée un score aléatoire 
        score_match_aller_demi = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_aller_demi[0], "-", score_match_aller_demi[1])
        # On ajoute les scores dans la liste
        list_score_match_aller_demi.append(score_match_aller_demi)
    return list_score_match_aller_demi
# Fontion qui permet de voir l'intégralité des matchs retour des demi-finales en comptabilisant les points et les buts de chaque équipe
def match_retour_demi(list_demi):
    print("Match retour des demis de finale")
    print("\n")
    # On crée un list qui va contenir les scores du matchs retour
    list_score_match_retour_demi = []
    # On crée une list list_score_match_retour_demi qui va contenir les scores des matchs aller et retour des demis 
    list_score_match_aller_retour_demi = []
    for i in range(len(list_demi)):
        # On affiche les équipes qui jouent en retour
        print("Match retour",i+1, ":",list_demi[i][0],"vs", list_demi[i][1])
        # On crée un score aléatoire 
        score_match_retour_demi = [random.randint(0,4), random.randint(0,4)]
        # On affiche ce score
        print("Score :", score_match_retour_demi[0], "-", score_match_retour_demi[1])
        # On ajoute le score du match dans la list score_match_retour_demi
        list_score_match_retour_demi.append(score_match_retour_demi) 
        # On ajoute les 2 scores des 2 mêmes matchs dans la liste list_score_match_aller_retour_demi
        list_score_match_aller_retour_demi.append(list_score_match_aller_demi[i][0] + list_score_match_retour_demi[i][0])
        list_score_match_aller_retour_demi.append(list_score_match_aller_demi[i][1] + list_score_match_retour_demi[i][1])
        # On crée un list qui va contenir les scores des matchs aller et retour des demis
        list_score_final_demi = []
    print("\n")
    list_finale = []
    for i in range(len(list_score_match_retour_demi)):
        # On met les scores des matchs dans la list y
        y = []
        y.append(list_score_match_aller_demi[i][0] + list_score_match_retour_demi[i][0])
        y.append(list_score_match_aller_demi[i][1] + list_score_match_retour_demi[i][1])
        # Puis dans list_score_final_demi
        list_score_final_demi.append(y)
        # On regarde si la première équipe a gagné en fonction du cumul des buts marqués
        if(list_score_final_demi[i][0] > list_score_final_demi[i][1]):
            print("Vainqueur du match",i+1,":",list_demi[i][0],"vs", list_demi[i][1])
            print(list_demi[i][0],"après addition du score")
            # On ajoute le gagnant a la liste list_demi
            list_finale.append(list_demi[i][0]) 
            print("\n")
        # Si les deux équipes ont le même score alors 
        elif(list_score_final_demi[i][0] == list_score_final_demi[i][1]):
            print("Vainqueur du match",i+1,":",list_demi[i][0],"vs", list_demi[i][1])
            # On fait un tirage au sort pour connaitre le gagant
            penalty = random.randint(0,1)
            if(penalty == 0):
                print(list_demi[i][0],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_demi
                list_finale.append(list_demi[i][0]) 
                print("\n")
            else:
                print(list_demi[i][1],"après une séance de pénaltys")
                # On ajoute le gagnant a la liste list_demi
                list_finale.append(list_demi[i][1])
                print("\n")
        # On regarde si la deuxième équipe a gagné en fonction du cumul des buts marqués
        else:
            print("Vainqueur du match",i+1,":",list_demi[i][0],"vs", list_demi[i][1])
            print(list_demi[i][1],"après addition du score")
            # On ajoute le gagnant a la liste list_demi
            list_finale.append(list_demi[i][1])
            print("\n")
    return list_finale
# Fonction qui permet d'afficher les qualifiés pour la finale
def affichage_equipe_finale(list_finale):
    for i in range(len(list_finale)):
        print(list_finale[i])
    print("\n")
    return list_finale
# Fonction qui permet de voir le match de la finale
def match_finale(list_finale):
    # On mélange la liste
    list_finale_rdm = random.sample(list_finale, len(list_finale))
    # On crée des binomes pour faire jouer les équipes de huitième de finale
    list_match_finale = [list_finale_rdm[i:i+2] for i in range(0, len(list_finale_rdm), 2)]
    # On crée une liste qui va contenir le vainqueur
    vainqueur = []
    # Affichage des 8 matchs de huitième de finale
    for i in range(len(list_match_finale)):
        print("Grande finale de la Ligue des Champions")
        print("\n")
        print(list_match_finale[i][0],"vs", list_match_finale[i][1])
        # On crée un score aléatoire
        score_match_finale = [random.randint(0,4), random.randint(0,4)]
        # On affiche le score
        print("Score :", score_match_finale[0], "-", score_match_finale[1])
        print("\n")
        if(score_match_finale[0] > score_match_finale[1]):
            print("Vainqueur de la Ligue des Champions :",list_match_finale[i][0])
            vainqueur.append(list_match_finale[i][0])
            print("\n")
        elif(score_match_finale[0] == score_match_finale[1]):
            penalty = random.randint(0,1)
            if(penalty == 0):
                print("Egalité... une séance de pénaltys s'impose !")
                print("Vainqueur de la Ligue des Champions après pénalty :",list_match_finale[i][0])
                vainqueur.append(list_match_finale[i][0])
                print("\n")
            else:
                print("Egalité... une séance de pénaltys s'impose !")
                print("Vainqueur de la Ligue des Champions après pénalty :",list_match_finale[i][1])
                vainqueur.append(list_match_finale[i][1])
                print("\n")
        else:
            print("Vainqueur de la Ligue des Champions :",list_match_finale[i][1])
            vainqueur.append(list_match_finale[i][1])
            print("\n")
    return vainqueur
# Fonction qui affiche le gagnant de la finale en une chaine de caractères
def affichage_gagnant_finale(vainqueur):
    # list to string
    vainqueur_str = str(vainqueur[0])
    return vainqueur_str

    
########################################################################################################################
####                                          AFFICHAGE DU DEROULEMENT DU CHAMPIONNAT                               ####
########################################################################################################################
print("\n")
print("                                                                 LIGUE DES CHAMPIONS")
print("\n")
print("                                                 EXPLICATION DU DEROULEMENT DE LA LIGUE DES CHAMPIONS\n")
print("Déroulement de la phase de poule : 32 équipes en jeu")
print("Début des premiers matchs, une équipe fera un match aller puis un match retour contre les 3 autres équipes de sa poule.")
print("Une victoire apportera 3 points, une égalité 1 point et une défaite 0 point.")
print("Attention ! En cas d'égalité entre le second et le troisième, le nombre de buts les départageront.")
print("Seulement les deux équipes qui feront le meilleur nombre de points pourront se qualifier en 8ième de finale.")
print("\n")
print("Déroulement de la 8ième de finale : 16 équipes en jeu")
print("Une équipe affrontera en match aller-retour une seule autre équipe.")
print("Attention ! En cas d'égalité, une séance de tir au but sera alors présente lors de la fin du match retour.")
print("Seulement une équipe pourra se qualifier a l'issu de chaque match.")
print("\n")
print("Déroulement du 1/4 de finale : 8 équipes en jeu")
print("Même scénario que lors des 8ième, match aller-retour contre une seule autre équipe.")
print("Attention ! En cas d'égalité, une séance de tir au but sera alors présente lors de la fin du match retour. ")
print("Seulement une équipe pourra se qualifier a l'issu de chaque match.")
print("\n")
print("Déroulement de la 1/2 finale : 4 équipes en jeu")
print("Même scénario que lors des 8ième ou des 1/4, match aller-retour contre une seule autre équipe.")
print("Attention ! En cas d'égalité, une séance de tir au but sera alors présente lors de la fin du match retour. ")
print("Seulement une équipe pourra se qualifier a l'issu de chaque match.")
print("\n")
print("Déroulement de la finale : 2 équipes en jeu")
print("Les deux équipes s'affronteront lors d'un seul et unique match.")
print("Attention ! Si à la fin du temps additionnelle et des prolongations aucune équipe ne sort victorieuse, une séance de tir au but les départagera.")
print("Le gagnant du match sera le grand vainqueur de la LIGUE DES CHAMPIONS.")
print("\n")
continuer = input("A présent vous savez tout, afin de voir les 8 poules, appuyez sur la touche ENTREE !")

########################################################################################################################
####                                               AFFICHAGE DES 32 EQUIPES                                         ####
########################################################################################################################
print("\n")
print("Voici la liste des 32 équipes qualifiées pour la Ligue des Champions :")
print("\n")
list_equipe = " - ".join(liste_equipes)
print(list_equipe)
print("\n")
continuer = input("Appuyez sur ENTREE pour consulter les 8 poules !")

########################################################################################################################
####                                               AFFICHAGE DES POULES                                             ####
########################################################################################################################

print("\n")
print("Voici les 8 poules !")
print("\n")
print("Poule A :", list_poule_A[0][0], "-", list_poule_A[1][0], "-", list_poule_A[2][0], "-", list_poule_A[3][0])
print("Poule B :", list_poule_B[0][0], "-", list_poule_B[1][0], "-", list_poule_B[2][0], "-", list_poule_B[3][0])
print("Poule C :", list_poule_C[0][0], "-", list_poule_C[1][0], "-", list_poule_C[2][0], "-", list_poule_C[3][0])
print("Poule D :", list_poule_D[0][0], "-", list_poule_D[1][0], "-", list_poule_D[2][0], "-", list_poule_D[3][0])
print("Poule E :", list_poule_E[0][0], "-", list_poule_E[1][0], "-", list_poule_E[2][0], "-", list_poule_E[3][0])
print("Poule F :", list_poule_F[0][0], "-", list_poule_F[1][0], "-", list_poule_F[2][0], "-", list_poule_F[3][0])
print("Poule G :", list_poule_G[0][0], "-", list_poule_G[1][0], "-", list_poule_G[2][0], "-", list_poule_G[3][0])
print("Poule H :", list_poule_H[0][0], "-", list_poule_H[1][0], "-", list_poule_H[2][0], "-", list_poule_H[3][0])
print("\n")
continuer = input("Appuyez sur ENTREE pour consulter la liste des matchs 96 matchs des phases de poule !")

########################################################################################################################
####                                 AFFICHAGE DE TOUS MATCHS ALLER-RETOUR DE CHACUNE DES POULES                    ####
########################################################################################################################

# On affiche les matchs aller-retour de la poule A
a = match_poule(list_poule_A)
affichage_match_aller_retour(a,"A")

# On affiche les matchs aller-retour de la poule B
b = match_poule(list_poule_B)
affichage_match_aller_retour(b, "B")

# On affiche les matchs aller-retour de la poule C
c = match_poule(list_poule_C)
affichage_match_aller_retour(c, "C")

# On affiche les matchs aller-retour de la poule D
d = match_poule(list_poule_D)
affichage_match_aller_retour(d, "D")

# On affiche les matchs aller-retour de la poule E
e = match_poule(list_poule_E)
affichage_match_aller_retour(e, "E")

# On affiche les matchs aller-retour de la poule F
f = match_poule(list_poule_F)
affichage_match_aller_retour(f, "F")

# On affiche les matchs aller-retour de la poule G
g = match_poule(list_poule_G)
affichage_match_aller_retour(g, "G")

# On affiche les matchs aller-retour de la poule H
h = match_poule(list_poule_H)
affichage_match_aller_retour(h, "H")

# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
print("\n")
print("Voici l'intégralité des matchs qui se joueront prochainement...")
print("\n")
continuer = input("Appuyez sur ENTREE pour commencer les matchs des trois premières journées pour chacune des poules !")

########################################################################################################################
####                       AFFICHAGE DE TOUS LES MATCH ALLER AVEC SCORE ET BUT DE CHACUNE DES POULES                ####
########################################################################################################################

# On affiche les 3 premières journées de la poule A
a = match_poule(list_poule_A)
affichage_match_aller(a, "A")

# On affiche les 3 premières journées de la poule B
b = match_poule(list_poule_B)
affichage_match_aller(b, "B")

# On affiche les 3 premières journées de la poule C
c = match_poule(list_poule_C)
affichage_match_aller(c, "C")

# On affiche les 3 premières journées de la poule D
d = match_poule(list_poule_D)
affichage_match_aller(d, "D")

# On affiche les 3 premières journées de la poule E
e = match_poule(list_poule_E)
affichage_match_aller(e, "E")

# On affiche les 3 premières journées de la poule F
f = match_poule(list_poule_F)
affichage_match_aller(f, "F")

# On affiche les 3 premières journées de la poule G
g = match_poule(list_poule_G)
affichage_match_aller(g, "G")

# On affiche les 3 premières journées de la poule H
h = match_poule(list_poule_H)
affichage_match_aller(h, "H")

print("\n")
print("Fin des 3 premières journées de la ligue des champions !")
print("\n")
continuer = input("Appuyez sur ENTREE pour consulter le classement de ses 3 premières journées !")
print("Classement de chacun des poules suite au 3 premières journées :")
# Affichage du classement de chacune des poules
a = affichage_classement(list_poule_A, "A")
b = affichage_classement(list_poule_B, "B")
c = affichage_classement(list_poule_C, "C")
d = affichage_classement(list_poule_D, "D")
e = affichage_classement(list_poule_E, "E")
f = affichage_classement(list_poule_F, "F")
g = affichage_classement(list_poule_G, "G")
h = affichage_classement(list_poule_H, "H")
print("\n")
continuer = input("Appuyez sur ENTREE pour continuer sur les trois dernières journées !")
print("\n")

########################################################################################################################
####                        AFFICHAGE DE TOUS LES MATCHS RETOUR AVEC SCORE ET BUT DE CHACUNE DES POYLES             ####
########################################################################################################################

# On affiche les 3 dernières journées de la poule A
a = match_poule(list_poule_A)
affichage_match_retour(a, "A")

# On affiche les 3 premières journées de la poule B
b = match_poule(list_poule_B)
affichage_match_retour(b, "B")

# On affiche les 3 premières journées de la poule C
c = match_poule(list_poule_C)
affichage_match_retour(c, "C")

# On affiche les 3 premières journées de la poule D
d = match_poule(list_poule_D)
affichage_match_retour(d, "D")

# On affiche les 3 premières journées de la poule E
e = match_poule(list_poule_E)
affichage_match_retour(e, "E")

# On affiche les 3 premières journées de la poule F
f = match_poule(list_poule_F)
affichage_match_retour(f, "F")

# On affiche les 3 premières journées de la poule G
g = match_poule(list_poule_G)
affichage_match_retour(g, "G")

# On affiche les 3 premières journées de la poule H
h = match_poule(list_poule_H)
affichage_match_retour(h, "H")

print("\n")
print("Fin des 3 dernières journées de la ligue des champions !")
print("\n")
print("Fin des poules ! Tous les matchs ont été jouer.")
print("\n")
continuer = input("Afin de voir le classement final de chacune des poules, appuyez sur la touche ENTREE !")
print("\n")

########################################################################################################################
####                       AFFICHAGE DU CLASSEMENT DE CHACUNE DES POULES AVEC SCORE ET BUT                          ####
########################################################################################################################

# Affichage du classement de chacune des poules
a = affichage_classement(list_poule_A, "A")
b = affichage_classement(list_poule_B, "B")
c = affichage_classement(list_poule_C, "C")
d = affichage_classement(list_poule_D, "D")
e = affichage_classement(list_poule_E, "E")
f = affichage_classement(list_poule_F, "F")
g = affichage_classement(list_poule_G, "G")
h = affichage_classement(list_poule_H, "H")
print("\n")
print("Voici le classement de chaque poule ! Vous y retrouvez le nom des équipes mais également leurs score puis leurs nombres de buts.")
print("\n")
print("Prenez place les huitièmes de finale vont bientôt commencer !")
print("\n")
continuer = input("Appuyez sur ENTREE afin de voir les qualifiés en huitième de chacune des poules !")
print("\n")

########################################################################################################################
####                                               8ième de final                                                   ####
####                       AFFICHAGE DU CLASSEMENT DE CHACUNE DES POULES AVEC SCORE ET BUT                          ####
########################################################################################################################

# On affiche les deux premiers de chacune des poules
a = selection_huitieme(list_poule_A, "A")
b = selection_huitieme(list_poule_B, "B")
c = selection_huitieme(list_poule_C, "C")
d = selection_huitieme(list_poule_D, "D")
e = selection_huitieme(list_poule_E, "E")
f = selection_huitieme(list_poule_F, "F")
g = selection_huitieme(list_poule_G, "G")
h = selection_huitieme(list_poule_H, "H")
print("\n")
print("Voici les équipes qualités de chacune des poules. ")

########################################################################################################################
####                  AFFICHAGE DE TOUTES LES EQUIPES QUALIFIES EN HUITIEME AVEC LEUR SCORE ET LEUR BUT             ####
########################################################################################################################

print("\n")
continuer = input("Appuyez sur ENTREE afin de voir la liste complète des équipes en huitième de finale !")
print("\n")
print("Voici la liste complète des équipes en huitième de finale. ")
print("\n")
affichage_equipe_huitieme = affichage_equipe_huitiemes(list_poule_A, list_poule_B, list_poule_C, list_poule_D, list_poule_E, list_poule_F, list_poule_G, list_poule_H)
print("\n")
print("Voici les équipes qualifiés en huitième de finale. Un tirage au sort se fera afin de déterminer les futurs rencontres...")
########################################################################################################################
####                                 AFFICHAGE DE TOUS MATCHS ALLER-RETOUR DES HUITIEMES DE FINALE                  ####
########################################################################################################################

# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
print("\n")
continuer = input("Appuyez sur ENTREE afin de voir les matchs de la huitième de finale !")
# On affiche les équipes qui s'affronteront en huitième de finale en match aller-retour
print("\n")
print("Tirage au sort effectué ! Voici la liste des 8 matchs de la 8ième finale")
print("\n")
huitieme = match_huitieme(affichage_equipe_huitieme)

########################################################################################################################
####                                 AFFICHAGE DES MATCHS ALLER DES HUITIEMES DE FINALE                             ####
########################################################################################################################

# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
print("\n")
print("Les matchs vont bientôt commencer...")
print("\n")
# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
continuer = input("Appuyez sur ENTREE afin de commencer les matchs aller de la huitième de finale !")
print("\n")
list_score_match_aller_huitieme = match_aller_huitieme(huitieme)
print("\n")
print("Voici les résultats des matchs aller des huitièmes de finale...")
print("\n")
# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
continuer = input("Appuyez sur ENTREE afin de commencer les matchs retour de la huitième de finale !")
print("\n")
########################################################################################################################
####                                 AFFICHAGE DES MATCHS RETOUR DES HUITIEMES DE FINALE                            ####
########################################################################################################################

# On demande à l'utilisateur d'appuyer sur ENTREE pour continuer
match_retour_huitieme = match_retour_huitieme(huitieme)
list_quart = match_retour_huitieme
print("Voici la liste des vainqueurs de chaque match de la huitième de finale.")
print("\n")
continuer = input("Appuyez sur ENTREE afin de voir la liste des qualifiés en quart de finale!")
print("\n")

########################################################################################################################
####                    AFFICHAGE DE TOUTES LES EQUIPES QUALIFIES EN QUART AVEC LEUR SCORE ET LEUR BUT              ####
########################################################################################################################

print("Voici le classement récapitulatif des qualifiés en quart de finale")
print("\n")
affichage_equipe_quart = affichage_equipe_quart(list_quart)
print("Voici les équipes qualifiés en quart de finale. Un tirage au sort se fera afin de déterminer les futurs rencontres...")

########################################################################################################################
####                                 AFFICHAGE DE TOUS MATCHS ALLER-RETOUR DES QUARTS DE FINALE                     ####
########################################################################################################################

print("\n")
continuer = input("Appuyez sur ENTREE afin de voir les matchs des quarts de finale !")
print("\n")
print("Tirage au sort effectué ! Voici la liste des 4 matchs des quarts de finale")
print("\n")
quart = match_quart(affichage_equipe_quart)

########################################################################################################################
####                                 AFFICHAGE DES MATCHS ALLER DES QUARTS DE FINALE                                ####
########################################################################################################################

print("\n")
print("Les matchs vont bientôt commencer...")
print("\n")
continuer = input("Appuyez sur ENTREE afin de commencer les matchs aller des quarts de finale !")
print("\n")
list_score_match_aller_quart = match_aller_quart(quart)
print("\n")
print("Voici les résultats des matchs aller des quarts de finale...")
print("\n")
continuer = input("Appuyez sur ENTREE afin de commencer les matchs retour des quarts de finale !")
print("\n")

########################################################################################################################
####                                 AFFICHAGE DES MATCHS RETOUR DES QUARTS DE FINALE                               ####
########################################################################################################################

match_retour_quart = match_retour_quart(quart)
list_demi = match_retour_quart
print("Voici la liste des vainqueurs des quart de finale")
print("\n")
continuer = input("Appuyez sur ENTREE afin de voir la liste des qualifiés de demi finale!")
print("\n")

########################################################################################################################
####                                 AFFICHAGE DE TOUTES LES EQUIPES QUALIFIES EN DEMI                              ####
########################################################################################################################

print("Voici le classement récapitulatif des qualifiés en quart de finale")
print("\n")
affichage_equipe_demi = affichage_equipe_demi(list_demi)
print("Voici les équipes qualifiés en huitième de finale. Un tirage au sort se fera afin de déterminer les futurs rencontres...")

########################################################################################################################
####                                 AFFICHAGE DE TOUS MATCHS ALLER-RETOUR DES DEMI-FINALES                         ####
########################################################################################################################

print("\n")
continuer = input("Appuyez sur ENTREE afin de voir les matchs des demi-finales !")
print("\n")
print("Tirage au sort effectué ! Voici la liste des 2 matchs des demi-finales")
print("\n")
demi = match_demi(affichage_equipe_demi)

########################################################################################################################
####                                 AFFICHAGE DES MATCHS ALLER DES DEMI-FINALES                                    ####
########################################################################################################################

print("\n")
print("Les matchs vont bientôt commencer...")
print("\n")
continuer = input("Appuyez sur ENTREE afin de commencer les matchs aller des demi-finales !")
print("\n")
list_score_match_aller_demi = match_aller_demi(demi)
print("\n")
print("Voici les résultats des matchs aller des demi-finales...")
print("\n")
continuer = input("Appuyez sur ENTREE afin de commencer les matchs retour des demi-finales !")
print("\n")

########################################################################################################################
####                                 AFFICHAGE DES MATCHS RETOUR DES DEMI-FINALES                                   ####
########################################################################################################################

match_retour_demi = match_retour_demi(demi)
list_finale = match_retour_demi
print("Voici la liste des vainqueurs des demi-finales")
print("\n")
continuer = input("Appuyez sur ENTREE afin de voir les deux qualifiés pour la GRANDE FINALE !")
print("\n")

########################################################################################################################
####                                 AFFICHAGE DE TOUTES LES EQUIPES QUALIFIES EN DEMI                              ####
########################################################################################################################

print("Voici nos deux finalistes") 
affichage_equipe_finale = affichage_equipe_finale(list_finale)
print("Voici les équipes qualifiés en finale. Prenez place.... la grande finale va commencer!")

########################################################################################################################
####                                          AFFICHAGE DU MATCH DE LA FINALE                                       ####
########################################################################################################################

print("\n")
continuer = input("Appuyez sur ENTREE afin de voir la grande finale!")
print("\n")
finale = match_finale(affichage_equipe_finale)
print("\n")
# On met le vainqueur dans une variable string
vainqueur_str = affichage_gagnant_finale(finale)
continuer = input("Appuyez sur ENTREE afin de célébrer cette victoire !")

########################################################################################################################
####                               AFFICHAGE GRAPHIQUE DU GAGNANT DE LA LIGUE DES CHAMPIONS                         ####
########################################################################################################################


# On met l'url avec comme nom de vainqueur dans le chemin de l'url
url = "Logos/{vainqueur_str}.png".format(vainqueur_str=vainqueur_str)

# On utilise pygame pour l'interface graphique 
pygame.init()

# On crée une fenêtre de taille 800x600
ecran = pygame.display.set_mode((400, 400))
# On intégre le logo dans la fenêtre
image = pygame.image.load(url).convert_alpha()

# On affiche une phrase de félicitations
phrase = pygame.font.Font('freesansbold.ttf', 18)
phrase_felicitation = phrase.render("GAGNANT DE LA LIGUE DES CHAMPIONS", True, (255, 255, 255))
phraseFelicitation = phrase_felicitation.get_rect()
phraseFelicitation.center = (200, 20)

# On affiche le gagnant en haut du logo
equipe = pygame.font.Font('freesansbold.ttf', 32)
nom_equipe = equipe.render(vainqueur_str, True, (255, 255, 255))
nomEquipe = nom_equipe.get_rect()
nomEquipe.center = (200,100)

# On modifie le titre de la fenêtre
pygame.display.set_caption("Vainqueur de la ligue des champions")
 
continuer = True

# Boucle infinie pour afficher la fenetre, l'utilisateur peut fermer la fenêtre en appuyant sur échap
while continuer:
    ecran.blit(phrase_felicitation, phraseFelicitation)
    ecran.blit(nom_equipe, nomEquipe)
    ecran.blit(image, (150, 150))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
 
pygame.quit()