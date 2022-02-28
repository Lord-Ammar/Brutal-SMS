#Kode Warna Python
#Hijau=\033[1;92m
#putih=\033[1;97m
#abu=\033[1;90m
#kuning=\033[1;93m
#ungu=\033[1;95m
#merah=33[37;1m
#biru=\033[1;96m
#Tulisan Background Merah
#\033[1;0m\033[1;41mText\033[1;0m
from colorama import init, Fore, Back
from requests.exceptions import ConnectionError
try:
	import os,sys,time,requests
except ImportEror:
	print ("Module Not installed\n[!] Ketik:pip install reuests && pip2 install requests")
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK

IP = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))

def tes():
	os.system("clear")
	print("\033[1;0m\033[1;41mJoin Executed Team..\033[1;0m")
	time.sleep(3)
	os.system("xdg-open https://bit.ly/ExecutedTeam")
	os.system("clear")
	print(""+Fore.WHITE+"       ‎╮╰╮╮"+Fore.RED+"▕╲"+Fore.WHITE+"╰╮╭╯"+Fore.RED+"╱▏"+Fore.WHITE+"╭╭╭╭   \033[1;95m╔╗ \033[1;97m┬─┐┬ ┬┌┬┐┌─┐┬   \033[1;96m╔═╗\033[1;97m┌┬┐┌─┐")
	print("       ╰╰╮╰╭╱▔▔▔▔╲╮╯╭╯   "+Fore.RED+"\033[1;95m ╠╩╗"+Fore.WHITE+"├┬┘│ │ │ ├─┤│───\033[1;96m╚═╗\033[1;97m│││└─┐")
	print("\033[1;90m       ┏━┓"+Fore.WHITE+"┏┫╭▅╲╱▅╮┣┓╭\033[1;93m║║║"+Fore.RED+"\033[1;95m  ╚═╝"+Fore.WHITE+"┴└─└─┘ ┴ ┴ ┴┴─┘ \033[1;96m╚═╝\033[1;97m┴ ┴└─┘")
	print("\033[1;90m       ╰┳╯"+Fore.WHITE+"╰┫┗━╭╮━┛┣╯╯\033[1;93m╚╬╝        "+Fore.GREEN+"╔╦╗\033[1;97m┌─┐┌─┐┬  ┌─┐")
	print("\033[1;90m       ╭┻╮"+Fore.RED+"╱\033[1;97m╰╮╰━━╯╭╯"+Fore.RED+"╲\033[1;97m┊\033[1;93m ║		 "+Fore.GREEN+"║\033[1;97m │ ││ ││  └─┐")
	print(""+Fore.BLACK+"       ╰┳┫"+Fore.RED+"▔╲\033[1;97m╰┳━━┳╯"+Fore.RED+"╱▔\033[1;97m┊\033[1;93m ║		 \033[1;92m╩\033[1;97m └─┘└─┘┴─┘└─┘")
	print("       ┈┃╰━━"+Fore.RED+"╲▕╲╱▏"+Fore.RED+"╱"+Fore.WHITE+"━━━┬╨╮\033[1;90m────────────────────────────────────────────")
	print("\033[1;97m       ┈╰━━╮"+Fore.RED+"┊▕╱╲▏┊"+Fore.WHITE+"╭━━┴╥╯\033[1;96m["+Back.WHITE+Fore.BLACK+"Copyright By ©AmmarBN ©2022 Sunday 20 Feb \033[00m"+Fore.RED+"\033[1;96m]")
	print("")
	print(""+Fore.WHITE+"       Time Local:\033[1;92m"+localtime)
	print(""+Fore.WHITE+"       Youtube:\033[1;92mbit.ly/AmmarExecuted")
	print(""+Fore.WHITE+"       You Ip:\033[1;92m"+IP)
	print(""+Fore.WHITE+"       User:\033[1;92m37 user")
	print("")
tes()
