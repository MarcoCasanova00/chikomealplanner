import random
import math

from ingredienti import *
from frasi_random import *

class bcolors:
	CYAN = '\033[92m'
	END = '\033[0m'
	BOLD = '\033[1m'
	YELLOW = '\033[93m'

print ( '''

                                      ████████████████                                          
                                  ████░░▒▒▒▒▒▒░░░░▒▒▒▒██████                                    
                                ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░████                                
                          ████████▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░████                            
                    ▒▒▒▒██▒▒▒▒░░▒▒██████▒▒░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒██                          
                ████░░▒▒░░▒▒░░░░░░░░░░░░████▒▒▒▒░░░░░░░░░░░░░░▒▒░░░░▒▒██                        
              ██░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░████▒▒░░░░░░░░░░░░░░░░░░░░░░██                      
            ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒████░░░░░░░░░░░░░░░░░░░░▒▒██                    
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒░░░░░░░░░░░░░░░░░░▒▒██                  
          ██░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒░░░░░░░░▒▒██▒▒░░▒▒░░░░░░░░░░░░░░░░██                
      ▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██▒▒░░░░░░░░░░░░░░░░▒▒██                
  ████░░░░░░░░░░░░▒▒░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒░░░░░░░░░░░░░░░░▒▒██              
██░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░██░░▒▒░░░░░░░░░░░░░░██              
██░░░░░░▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒░░▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒▒██            
  ██▒▒▒▒▒▒██████░░░░░░░░░░██████▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░▒▒░░░░██░░░░░░░░░░░░░░░░██            
  ████████      ██  ░░    ░░░░░░██████▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒░░██▒▒▒▒░░░░░░░░░░░░░░██          
                ██            ░░░░░░░░████▒▒▒▒░░▒▒░░░░░░░░░░░░▒▒░░██▒▒▒▒░░░░▒▒▒▒░░░░░░██        
                  ████    ░░    ░░    ░░░░████▒▒▒▒▒▒░░░░░░░░░░░░░░████▒▒░░░░░░░░░░░░░░▒▒██      
                      ████        ░░  ░░  ░░░░██▒▒░░▒▒░░░░░░░░░░░░▒▒████▒▒▒▒░░░░░░░░░░░░░░████  
                          ████                ░░██▒▒▒▒▒▒░░░░░░░░░░▒▒██░░██▒▒▒▒░░░░░░░░░░░░░░▒▒██
                              ▓▓▓▓  ░░    ░░░░  ░░██▒▒░░▒▒░░░░░░░░░░▒▒██  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
                                  ████████        ░░██▒▒▒▒▒▒░░░░░░░░░░▒▒██████▒▒▒▒░░░░▒▒████    
                                  ░░░░░░  ▓▓██████████▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒██▓▓▓▓▓▓  ░░    
                                                      ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒██                
                                                        ████▒▒▒▒▒▒░░░░░░▒▒▒▒██                  
                                                            ████▒▒▒▒▒▒▒▒████                    
                                                                ████████                        
''' )

print (f"{bcolors.BOLD}ଘ(੭ºัᴗºั)━☆ﾟ*:. I'm Chiko the Meal Planner Buddy! {bcolors.END}\n")
print ("coded by Marco Casanova \n")
print (f"{bcolors.YELLOW} >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< {bcolors.END} \n")


def randomizzatore():

	# LISTE DI TUTTO PER RANDOMIZZATORE

	proteine_li = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
	contorni_li = [c1, c2, c3, c4, c5, c6]
	salse_li = [s1, s2, s3]

	random_1 = random.choice(proteine_li)
	random_2 = random.choice(contorni_li)
	random_3 = random.choice(contorni_li)
	random_4 = random.choice(salse_li)
	random_phrase = random.choice(frasi)
	
	
	print (random_1.nome + random_2.nome + random_3.nome + random_4.nome + random_phrase)
	costo = (math.ceil(random_1.prezzo) + math.ceil(random_2.prezzo) + math.ceil(random_3.prezzo))
	print ("Il prezzo totale, escluse le salse, sara' di circa " + str(costo) + " Euro. \n") 

	
	return 1
	
	
print(f"{bcolors.CYAN}LUNEDI: {bcolors.END}")
randomizzatore()
randomizzatore()
print(f"{bcolors.CYAN}MARTEDI: {bcolors.END}")
randomizzatore()
randomizzatore()
print(f"{bcolors.CYAN}MERCOLEDI: {bcolors.END}")
randomizzatore()
randomizzatore()
print(f"{bcolors.CYAN}GIOVEDI: {bcolors.END}")
randomizzatore()
randomizzatore()
print(f"{bcolors.CYAN}SABATO: {bcolors.END}")
randomizzatore()
randomizzatore()
print(f"{bcolors.CYAN}DOMENICA: {bcolors.END}")
randomizzatore()
randomizzatore()

print (" \n")
print (f"{bcolors.YELLOW} >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< {bcolors.END} ")




