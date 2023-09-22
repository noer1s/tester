import sys, random, time, importlib
import threading, settings

def loadingHack(importlib):
	chaine = "[*]"+' Start terrox...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			time.sleep(0.06)

def thread_loading():
	num = random.choice([1])

	importlib = threading.Thread(target=settings.init)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))

	load.start()
	importlib.join()
	load.join()
