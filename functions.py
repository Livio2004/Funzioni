import math
import numpy as np
from scipy.integrate import quad


def media(x): #MEDIA
    m = 0.0
    for i in x:
        m += i # += incrementa la variabile somma di i
    m /= len(x) # /= divide la variabile m per len(x)
    return m

def devst(x): #DEVIAZIONE STANDARD
  s = 0.0
  N = len(x)
  m = mean(x)
  for i in x:
    s = s + (i-m)**2 #attenzione: potevo usare +=

  v = math.sqrt(s/(N-1))
  return v


def erroreStandardMedia(x): #ERRORE STANDARD DELLA MEDIA
  N = len(x)
  e = devst(x)/math.sqrt(N)
  return e



def minimi_quadrati1(x, y, s_y) :   #Minimi quadrati per interpolazione lineare Y = A + BX con sigma_y singola
  s = np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y)
  s2 = len(x)*np.sum(x*y)-np.sum(x)*np.sum(y)
  d  = len(x)*np.sum(x**2)-(np.sum(x))**2
  A = s/d
  B = s2/d
  sigma_a = (np.sqrt(np.sum(x**2)/d))*s_y
  sigma_b = np.sqrt(len(x)/d)*s_y

  return A, B, sigma_a, sigma_b


def minimi_quadrati2(x, y, s_y) :   #Minimi quadrati per interpolazione lineare Y = A + BX con sigma_y diverse (array)
  f=np.sum(y)/np.sum(s_y**2)
  g=np.sum(x**2)/np.sum(s_y**2)
  h=np.sum(x)/np.sum(s_y**2)
  j=(np.sum(x*y))/np.sum(s_y**2)
  k=np.sum(1/s_y**2)
  l=h**2

  A= (f*g-h*j)/(k*g-l)
  B= (k*j-h*f)/(k*g-l)

  sigma_a = np.sqrt(np.absolute(g/(k*g-l)))
  sigma_b = np.sqrt(np.absolute(k/(k*g-l)))

  return A, B, sigma_a, sigma_b

def chi2(A,B, x, y, sy) :  #Chi quadro relativo all'interpolazione lineare
  s=np.sum(np.power(y-A-B*x,2)/sy**2)
  return s

def chi2Gauss(E, O) :  #Chi quadro distribuzioni Gaussiane
  s = O - E
  q = np.sqrt(E)
  r = np.sum(np.power(s/q , 2))
  return r


def Gaussian(z):
  return (1/np.sqrt(2*np.pi))*np.exp((-z**2)/2) #Gaussiana standardizzata



def Test_hp1(x1,x2,s1,s2) :  #test di ipotesi con due valori calcolati
  t = np.absolute(x1-x2)/np.sqrt(s1**2+s2**2)  #t di confronto
  R = quad(Gaussian,-t,t) #calcolo del rapporto con l'integrale
  S = 1 -(R[0]/2)
  return S

def Test_hp2(x1,X,s) :  #test di ipotesi con un valore calcolato
  t = np.absolute(x1-X)/s  #t di confronto
  R = quad(Gaussian,-t,t) #calcolo del rapporto con l'integrale
  S = 1 -(R[0]/2)
  return S