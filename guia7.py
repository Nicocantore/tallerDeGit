import math
import random
# ejercicio 1

#1
def pertenecePalabra (s:list[str] , e:str) -> bool:
    i:int = 0
    while i < len(s) and s[i] != e:
     i +=1
    return i <len(s)

#print (pertenece1 ([1,2,3,4,5,6], 5))
#print (pertenece1 ([1,2,3,4,5,6], 0))


def pertenece2 (s:list , e:int) -> bool:
    res:bool = False
    for i in range(0,len(s),1):
        if s[i] == e:
            res = True
    return res

#print (pertenece2 ([1,2,3,4,5,6],0))
#print (pertenece2 ([1,2,3,4,5,6],6))

#2
def divideATodos (s:list[int],e:int) -> bool:
   i:int = 0
   while i < len(s) and s[i] % e == 0:
      i += 1 
   return i == len(s)

#print(divideATodos((2,4,6,8,10),2))
#print(divideATodos((2,4,6,8,9),2))

#3
def sumaTotal (s:list[int]) -> int :
   res = 0
   for i in range(0,len(s),1):
    res += s[i]
   return res

#print(sumaTotal([5,5,10,20]))

#4
def ordenados (s:list[int]) ->bool:
   i:int = 0
   while i < (len(s)-1) and s[i] < s[i+1] :
    i += 1
   return i == (len(s)-1)

#print(ordenados([1,3,5,7,10]))
#print(ordenados([1,3,5,7,5]))
#print(ordenados([1,3,5,4,10]))

#5
def longMayASietre (s:list[str]) -> bool:
   res:bool = False
   i:int = 0
   while i < len(s) and res == False:
      if len(s[i]) > 7:
         res = True
      i += 1
   return res

#print(longMayASietre(["hola","como","va","todo bien amigo?"]))
#print(longMayASietre(["hola","como","va","todo","bien","amigo"]))

#6
def palindromo (palabra:str) -> bool:
   res:bool = False
   a:int = 0
   b:int = len(palabra) - 1
   while a < len(palabra) and palabra[a] == palabra[b]:
    a += 1
    b -= 1
   return a == len(palabra)

#print (palindromo("neuquen"))
#print (palindromo("neuuen"))
#print (palindromo ("hola"))

#7
def tieneMay (palabra:str) -> bool:
   i:int = 0 
   res:str = False
   while i < len(palabra)  :
    if ord(palabra[i]) > 64 and ord(palabra[i]) < 91:
          res = True
    i += 1
   return res
#print (tieneMay("hOla"))
#print (tieneMay("hola"))

def tieneMin (palabra:str) -> bool:
   i:int = 0 
   res:str = False
   while i < len(palabra)  :
    if ord(palabra[i]) > 96 and ord(palabra[i]) < 123:
          res = True
    i += 1
   return res 
#print (tieneMin("HOLA"))
#print (tieneMin("HoLA"))

def tieneAlgunoDelUnoAlDiez (palabra:str):
   i:int = 0 
   res:str = False
   while i < len(palabra):
      if pertenecePalabra((str([0,1,...,9])), palabra[i]):
         res = True
      i += 1
   return res
#print (tieneAlgunoDelUnoAlDiez("Buenastardes"))
#print (tieneAlgunoDelUnoAlDiez("Hola"))
#print (tieneAlgunoDelUnoAlDiez("Ho1a"))

def fortalza (contraseña:str) -> str:
   res:str = None
   if len(contraseña) > 8 and tieneMay(contraseña) and tieneMin(contraseña) and tieneAlgunoDelUnoAlDiez(contraseña):
      res = "VERDE"
   elif len(contraseña) < 5:
      res = "ROJA"
   else:
      res = "AMARILLA"
   return res  

#print (fortalza("ContraSena123"))
#print (fortalza("Cont"))
#print (fortalza("ContraSena"))

#8
#def movBanc (a:list[tuple]):
#   saldo:int = 0
#   i:int = 0
#   while i < len(a):
#   tupla:tuple[str,int] = a[i]
#    if tupla[0] == "I" :
#      saldo += tupla[1] 
#    elif tupla[0] == "R": 
#       saldo -=  tupla[1]
#    i =+ 1
#  return saldo
def movBanc (a:list[tuple]):
   saldo:int = 0
   i:int = 0
   while i < len(a):
    codigo , monto = a[i]
    if codigo == "I" :
      saldo += monto 
    elif codigo == "R": 
       saldo -=  monto
    i += 1
   return saldo  
#print(movBanc([("I",2000),("R",500)]))

#9
def tieneTresMayDistintas (palabra:str) -> bool:
   i:int = 0 
   res:int = 0
   l:list[chr] = []
   while i < len(palabra)  :
    if ord(palabra[i]) > 64 and ord(palabra[i]) < 91 and not pertenecePalabra(l,palabra[i]):
          res +=1
          l.append(palabra[i])
    i += 1
   return res == 3

#print (tieneTresMayDistintas("hOLA"))
#print (tieneTresMayDistintas("hOLAP"))
#print (tieneTresMayDistintas("hAAA"))
#print (tieneTresMayDistintas("hOLa"))

# ejercicio 2

#1
def ceroEnPares1 (s:list[int]) ->None: #INOUT
   for i in range(0,len(s),2):
      s[i] = 0

#print(ceroEnPares1([1,2,3,4,5,6]))

#2
def ceroEnPares2 (s:list[int]) -> list: 
   i:int= 0
   listacopy:list[int] = s.copy()
   while i < len(listacopy):
      listacopy[i] = 0
      i += 2
   return listacopy

#print(ceroEnPares2([1,2,3,4,5,6]))
    
#3
#def sinVocales (palabra:list[chr]):
#   vocales:list[chr] = ['a','e','i','o','u' ]
#   for i in range(0,len(palabra),1):
#      if palabra[i] in vocales:
#          palabra.remove(palabra[i])
#   return palabra
vocales:list[chr] = ['a','e','i','o','u' ]
def sinVocales (palabra:list[chr]):
   i:int = 0
   while i < len(palabra):
      if palabra[i] in vocales:
          palabra.pop(i)
      i += 1
   return palabra
   
#print(sinVocales(["H","o","l","a"]))

#4
def remplazaVocales (s:str) -> list[str]:
   res:str = ""
   for i in range (0,len(s),1):
    if s[i] in vocales:
       res += "_"
    else:
       res += (s[i])
   return res

#print (remplazaVocales("Hola"))

#5
def daVueltaStr (s:str) -> str:
   res:str = ""
   for i in range((len(s)-1),(-1),(-1)):
      res += s[i]
   return res

#print(daVueltaStr("aloH"))

#6
def elimRep (s:str) -> str:
   res:str = ""
   for i in range(0,len(s),1):
      if s[i] not in res:
         res += s[i]
   return res

#print (elimRep("Hoooooolllaaaa"))

# ejercicio 3
def promedio (lista:list[int]) ->float:
   res:(float)=0
   for i in range(0,len(lista),1):
      res += lista[i]
   return res/ len(lista)

#print(promedio([8,8,8,9,8]))

def aprobado_O_No (notas:list[int]) -> int:
   res:int = None
   i:int = 0
   mayoracuatro:bool=True
   while i < len(notas) and mayoracuatro == True:
      if notas[i] < 4:
         mayoracuatro = False
      i +=1  
   if mayoracuatro == False:
      res = 3
   elif mayoracuatro==True and promedio(notas) >= 7:
      res = 1
   else:
      res = 2
   return res 
      
#print(aprobado_O_No([9,9,9,10,8,7]))
#print(aprobado_O_No([6,7,7,7,4,5]))
#print(aprobado_O_No([4,4,4,5,3,2,1,2]))

# ejercicio 4
# 4.1
def nombres () -> list:
  res:list= []
  x:str = input ("Escribi nombres: ")
  while x != "listo":
   res.append(x)
   x = input ("Escribi nombres: ")
  return res 

#print(nombres())

# 4.2
def sube () -> list:
   res:list[tuple] = []
   x:tuple = input ("seleccione: C // D // X: ") , input ("importe: ")
   accion , monto = x
   while accion != "X" and accion != "x"  :
      if x == "C" or "c":
         res.append(x)
         x = input ("seleccione: C // D // X: ") , input ("importe: ")
      elif x == "D" or "d":
         res.append(x)
         x = input ("seleccione: C // D // X: ") , input ("importe: ")
      accion , monto  = x
   return res  

#print(sube())

# 4.3
def siete_y_medio () -> list[str]:
   posiblescartas:list= [0,1,2,3,4,5,6,7,10,11,12]
   res:list = []
   numeroTotal:int = 0
   i:int = 0
   print("Si ustede desea sacar carta diga carta sino diga plantarse")
   x:str = input ("¿Que hago?: ")
   while x != "plantarse":
      if x == "carta":
         res.append(random.choice(posiblescartas))
         if res[i] in [10,11,12]:
            numeroTotal += 0.5
            print(numeroTotal)
            if numeroTotal >= 7.5:
              print("¡Perdiste! te pasaste de los 7.5")
              print ("Tus cartas fueron: ")
              return res
         else:
            numeroTotal += res[i]
            print(numeroTotal)
            if numeroTotal >= 7.5:
              print("¡Perdiste! te pasaste de los 7.5")
              print ("Tus cartas fueron: ")
              return res
         i += 1
         x = input ("Nuevamente, ¿que hago?")
      else:
         print(" ingreso no valido")
         x = input ("Nuevamente, ¿que hago?")
   print ("Tus cartas fueron: ") 
   return res

#print(siete_y_medio())

# ejercicio 5

# 5.1

def pertenece_a_cada_uno_v1 (s:list[list[int]],n:int) ->list[bool]:
   res:list[bool] = []
   i = 0
   while i < len(s):
      res.append(pertenece2 (s[i],n))
      i += 1
   return res

def pertenece_a_cada_uno_v2 (s:list[list[int]],n:int) ->list[bool]:
   res:list[bool] = []
   i = 0
   while i < len(s):
      res += [(pertenece2 (s[i],n))]
      i += 1
   return res

#print(pertenece_a_cada_uno_v1([[1,2,3],[3,4,5],[5,7,8],[3,6,7]],(3)))

# 5.3

def es_matriz (s:list[list[int]]) -> bool:
   res:bool = True
   if len(s) > 0:
      if len(s[0]) > 0:
         i:int = 1
         while i < len(s):
            if len(s[i]) != len(s[0]):
               res = False
            i += 1
      else:
         res = False
   else:
      res = False
   return res

#print(es_matriz([[1,2,3,4],[4,3,2,1],[8,2,5,6]]))

# 5.4

def filas_ordenadas (m:list[list[int]]) -> list[bool]:
   res:list[bool] = []
   i:int = 0
   while i <len(m):
      res.append(ordenados(m[i]))
      i += 1
   return res

#print(filas_ordenadas(([[1,2,3,4],[4,6,7,10],[8,2,5,6]])))
