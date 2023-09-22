import sys, os, time, random
from core.Profiler import *
from colorama import Fore
import settings
from datetime import date
from txt.text import text
from txt.header import lb_header


def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" python3 is must installed to use this best tool.")

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def menu():

	menu = """"""

	print(lb_header())
	print(menu)
