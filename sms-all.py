import os,sys,time,requests,bs4
#Target
def target():
	print ("\033[1;90m    ! \033[1;97mExample: \033[1;96m08xx")
	no = input("\033[1;96m    [\033[1;90m•\033[1;96m] \033[1;97mNomor Target: 0")
	ammar = ("0"+no)
	hah = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':no}).text
	req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':no}).text
	if 'terkirim' in req and hah:
		print ('\033[1;95m{\033[1;97m√\033[1;95m} \033[1;93mSpam Success')
	else:
		print ('\033[1;95m{\033[1;97mx\033[1;95m} \033[1;93mSpam Failed')

target()
