import hashlib

flag = 0
counter = 0

def banner():
	print("This Tool Is Created By Krisna Pranav")
	print("Github Link https://www.github.com/krishpranav")
	print("Do Not Forget To Follow Me :)")
	
pass_hash = input("Enter Your md5 hash >> ")
word_list = input("Enter Your Path To Password List >> ")

try:
	pass_file = open(wordlist, "r")
except:
	print("No File Found :( :(")
	print("Exiting....")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	print(word)
	print(digest)
	print(pass_hash)
	if digest == pass_hash:
		print("Password Found")
		print("Password Is " + word)
		flag = 1
		break

if flag == 0:
	print("Password/Passphrase is not in the list :( :(")
	banner()
