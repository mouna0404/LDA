# Analyse discriminant linéaire
Nous travaillerons sur le fichier WINE_QUALITY.XLS. Il recense 34 crus du bordelais répartis en 3 groupes « bon », « moyen », « médiocre » ; les descripteurs correspondent à des variables météorologiques (somme des températures journalières, jours d’ensoleillement, jours de chaleur, pluie).
Nous calculons la distribution relative des classes, qui sont assez équilibrées.
<p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/1.png">
</p>
La matrice est de dimension (3, 4) puisque nous avons un problème à (K = 3) classes (le
nombre de modalités de la variable cible Quality) et 4 descripteurs.
<p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/2.png">
</p>
Nous pouvons dès lors adopter une présentation plus sympathique des fonctions de
classement en y associant les noms des variables explicatives et des modalités de
QUALITY.
<p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/3.png">
</p>
Il ne faut pas oublier les constantes (intercept) des fonctions linéaires.
<p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/4.png">
</p>
## Evaluer le modèle global
 ### 1- Calcul de matrice de covariance intra‐classe
 <p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/5.png">
</p>
 ### 2- Calcul de Matrice de covariance totale
 <p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/6.png">
</p>
<p align="center">
<img src="https://github.com/mouna0404/LDA/blob/f6d09503069993d0b1196cd1efc5f63d2f2b992e/imgs/7.png">
</p>
