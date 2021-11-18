#changement de dossier 
import os 
os.chdir("C:/Users/MouNa/Desktop/LDA")

# Load the Pandas libraries with alias 'pandas' 
import pandas as pandas

#importation de l'échantillon train import pandas 
DTrain = pandas.read_excel("wine_quality.xls",sheet_name="Bordeaux Wine") 
print(DTrain.info())

#préparation des structures – vecteur cible 
yTrain = DTrain.iloc[:,4] 
#préparation des structures – matrice des explicatives 
XTrain = DTrain.iloc[:,0:4] 
#effectif  
n = DTrain.shape[0]

#nombre de descripteurs --
p = XTrain.shape[1] 
#nombre de classes 
K = len(yTrain.value_counts())
print(p)
print(K)
#distribution des classes 
print(yTrain.value_counts(normalize=True))

#importation
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#instanciation
lda = LinearDiscriminantAnalysis(solver="eigen",store_covariance=True)
#apprentissage
lda.fit(XTrain,yTrain)
#affichage brut des coefficients
print(lda.coef_)
#dimensions
print(lda.coef_.shape)
#liste des modalités
print(lda.classes_)
#structure temporaire pour affichage des coefficients 
tmp= pandas.DataFrame(lda.coef_.transpose(),columns=lda.classes_,index=XTrain.columns) 
print(tmp)
#et les constantes pour chaque classe 
print(lda.intercept_)
#modifier le mode d'affichage des matrices numpy
#pas de notation scientifique
import numpy
numpy.set_printoptions(suppress=True,linewidth=120,precision=4)
#pour retrouver la matrice W de SAS
W=n/(n-K)*lda.covariance_
print(W)
#calculons son déterminant
detW = numpy.linalg.det(W)
print("Déterminant de la matrice : %.4f" % (detW))
#et son logarithme
logDetW = numpy.log(detW)
print("Logarithme du déterminant : %.4f" % (logDetW))
#covariance totale avec Numpy
T = numpy.cov(XTrain.values,rowvar=False) 
print(T)
#lambda de Wilks 
LW = numpy.linalg.det(lda.covariance_)/numpy.linalg.det((n-1)/n*T)  
print("Lambda de Wilks : %.4f" % (LW)) 
#ddl numérateur 
ddlNum = p * (K-1) 
print("DDL numérateur : %.d" % (ddlNum))
#valeur intermédiaire pour calcul du ddl dénominateur 
temp = p**2 + (K-1)**2 - 5 
temp = numpy.where(temp > 0,numpy.sqrt(((p**2) * ((K-1)**2) - 4)/temp),1)
#ddl dénominateur 
ddlDenom = (2*n-p-K-2)/2 * temp - (ddlNum - 2)/2 
print("DDL dénominateur : %.d" % (ddlDenom))
#stat de test 
FRao = LW**(1/temp) 
FRao = ((1-FRao)/FRao)*(ddlDenom/ddlNum) 
print("Statistique F de Rao : %.4f" % (FRao))
#p-value 
import scipy 
print("P-value du test : %.4f" % (1-scipy.stats.f.cdf(FRao,ddlNum,ddlDenom)))














