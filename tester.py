 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style
from lib.menu import checkVersion, clear, menu
import sys, random, time, importlib
from lib.loading import thread_loading
from termcolor import colored


clear()
print("\033[31mвыполняется проверка данных,подождите.\033[0m")
time.sleep(1.55)
print("\033[31mдобро пожаловать в Terrox! перенаправляем вас в меню...\033[0m")
time.sleep(2.55)
clear()
redtext = colored("""
\033[31m▄▄▄█████▓▓█████  ██▀███   ██▀███   ▒█████  ▒██   ██▒
\033[31m▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░
\033[31m▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░
\033[31m░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒ 
\033[31m  ▒██▒ ░ ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒
\033[31m  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
\033[31m    ░     ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
\033[31m  ░         ░     ░░   ░   ░░   ░ ░ ░ ░ ▒   ░    ░  
\033[31m            ░  ░   ░        ░         ░ ░   ░    ░  
""", "red")

whitetext = """
▄▄▄█████▓▓█████  ██▀███   ██▀███   ▒█████  ▒██   ██▒
▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░
▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░
░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒ 
  ▒██▒ ░ ░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒
  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
    ░     ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
  ░         ░     ░░   ░   ░░   ░ ░ ░ ░ ▒   ░    ░  
            ░  ░   ░        ░         ░ ░   ░    ░  
"""

print(redtext)
time.sleep(1.2)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(0.1)
clear()
print(redtext)
time.sleep(0.1)
clear()
print(whitetext)
time.sleep(1.2)
print("\n                 лучший инструмент в своём роде.")
time.sleep(1.2)
clear()
mainOption = """                 лучший инструмент в своём роде.

 [\033[31m1\033[0m] поиск по данным    |    [\033[31m4\033[0m] фишинг
 [\033[31m2\033[0m] смс-бомбер         |    [\033[31m5\033[0m] генераторы
 [\033[31m3\033[0m] ддос-атаки         |    [\033[31m6\033[0m] паспорт для верификации киви

 [\033[31m7\033[0m] - выйти из утилиты
 [\033[31m8\033[0m] - информация и помощь об утилите.
 """


SearchMenu = """
 [1] поиск по IP
 
 [0] назад"""

otherToolOption = """
 [1] Hash decrypter
 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles
 [3] Create profile
 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg)
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)
 [b] back main menu   [c] Clear screen   [h] Help message
"""

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n"+Fore.RED + "terrox $ " + Fore.RESET)

		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:

				choix = input("\n"+Fore.RED + "terrox $ " + Fore.RESET)

				info = {"URL": {}}
				
				if choix.lower() == 'h':
					print(helpProfiler)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e' or choix.lower() == 'exit':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					if pr.count >= 1:
						while True: 
							profile = input(" Profile: ")
							if profile != '':
								break
						data = pr.searchDatabase(profile, database=database)
						profilerFunc(data, path=settings.pathDatabase)
					else:
						print(warning+" No profile found. Please create one.")
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: First name Last name)"+Fore.RESET)
					while True: 
						name = input(" Profile Name: ")
						if name != '':
							break
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					while True:
						print(question+" Want to register a Twitter account to profile ?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							twitter = input("\n Twitter: ")
							info['URL']['Twitter'] = twitter
							break
					# print(found+" %s" % (twitter))
					while True:
						print(question+" Want to register a Instagram account to profile ?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							instagram = input("\n Instagram: ")
							info['URL']['Instagram'] = instagram
							break
					while True:
						print(question+" want to register a Facebook account to profile ?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							facebook = input("\n Facebook: ")
							info['URL']['Facebook'] = facebook
							break

					create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

					if create:
						print("\n"+found+" Profile '% s' was created successfully." % (name))
					else:
						print("\n"+warning+" An error has occurred. Profile '% s' could not be created." % (name))

		elif choix.lower() == 'e' or choix.lower() == 'exit':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(SearchMenu)
			while True:
				lookup = input("\n"+Fore.RED + "terrox ~ " + Fore.RESET)
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchtestbyterrox()
				elif lookup.lower() == "0":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(SearchMenu)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					exit()
                    
				else:
					pass
					# print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n Waseem Akram("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n Hacker wasii("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					settings.codemonpays = "FR"
					settings.monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					settings.codemonpays = "BE"
					settings.monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					settings.codemonpays = "CH"
					settings.monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					settings.codemonpays = "LU"
					settings.monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					settings.codemonpays = "XX"
					settings.monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMain)
		else:
			pass
			# print("Command not found")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")
