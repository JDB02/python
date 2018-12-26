import os
from time import sleep

def timer(seconds):
	
	while seconds:
		min, sec = divmod(seconds, 60)
		count = '{:02d}:{:02d}'.format(min, sec)
		print(count, end="\r")
		print()
		sleep(1)
		seconds -= 1
		if os.name == 'nt':
			os.system('cls')
		elif os.name == 'posix':
			os.system('clear')
	print("Countdown finished!")

answer = int(input("How many seconds do you want to countdown?\n"))

timer(answer)
