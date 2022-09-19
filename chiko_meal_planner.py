import random

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

	proteine_li = [p1.nome, p2.nome, p3.nome, p4.nome, p5.nome, p6.nome]
	contorni_li = [c1.nome, c2.nome, c3.nome, c4.nome, c5.nome, c6.nome]
	salse_li = [s1.nome, s2.nome, s3.nome]
	
	#proteine_pr = [p1.prezzo, p2.prezzo, p3.prezzo, p4.prezzo, p5.prezzo, p6.prezzo]
	#contorni_pr = [c1.prezzo, c2.prezzo, c3.prezzo, c4.prezzo, c5.prezzo, c6.prezzo]
	#salse_pr = [s1.prezzo, s2.prezzo, s3.prezzo]

	random_1 = random.choice(proteine_li)
	random_2 = random.choice(contorni_li)
	random_3 = random.choice(salse_li)
	random_phrase = random.choice(frasi)
	
	print (random_1 + random_2 + random_3 + random_phrase)
	return 1
	
	
print(f"{bcolors.CYAN}LUNEDI: {bcolors.END}")
randomizzatore()
print(f"{bcolors.CYAN}MARTEDI: {bcolors.END}")
randomizzatore()
print(f"{bcolors.CYAN}MERCOLEDI: {bcolors.END}")
randomizzatore()
print(f"{bcolors.CYAN}GIOVEDI: {bcolors.END}")
randomizzatore()
print(f"{bcolors.CYAN}SABATO: {bcolors.END}")
randomizzatore()
print(f"{bcolors.CYAN}DOMENICA: {bcolors.END}")
randomizzatore()

print (" \n")
print (f"{bcolors.YELLOW} >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< {bcolors.END} ")


# TODO Devi implementare il fatto dei prezzi!


