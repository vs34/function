
'''
incripet every file even if it is inside of other folder

'''

def fifo(path):
	import os
	folder=[]
	files=[]
	for a in os.listdir(path):
		if os.path.isdir(path+'/'+a):
			folder.append(path+'/'+a)
			continue
		if os.path.isfile(path+'/'+a):
			files.append(path+'/'+a)
			continue
	return(files,folder)


def incrip(file):
	from cryptography.fernet import Fernet
	key = Fernet.generate_key()
	for a in file:
		with open(a,'rb') as f:
			c = f.read()
		fe=Fernet(key).encrypt(c)
		with open(a,'wb') as f:
			f.write(fe)
	return(key)

def decrip(key,file):
	from cryptography.fernet import Fernet
	for a in file:
		with open(a,'rb') as f:
			c = f.read()
		fd=Fernet(key).decrypt(c)
		with open(a,'wb') as f:
			f.write(fd)





a=fifo('/home/vaibhav/function/function/faltu')
#decrip('WOUeAdCIJnH11-9Dky48ARg_LYoO_4tP_T2OwsvDpYA=',a[0])
key=incrip(a[0])

with open('key.key','wb') as ki:
	ki.write(key)

