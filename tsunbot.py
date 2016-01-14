import socket
import sys
import time
from random import randint
from random import choice

server = "irc.freenode.net"
channel = "#lainchan"
botnick = "tsunbot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :desu\n")
irc.send("NICK "+ botnick +"\n")
#ns auth
f=open(".nspass")
nspass=f:read()
f:close()
irc.send("PRIVMSG nickserv :identify"+nspass+"\n")
time.sleep(20)
morals = 1
root = 0
irc.send("JOIN "+ channel +"\n")
irc.send('PRIVMSG '+channel+' :i-its not like ive been waiting to see you or anything, b-bakas \r\n')
while 1:
	text=irc.recv(2040)
	print text
	if text.find('PING') != -1:
		irc.send('PONG ' + text.split() [1] + '\r\n')
	elif text.find(':tsunbot?') !=-1:
		irc.send('PRIVMSG '+channel+' :w-what is it, b-baka? \r\n')
	elif text.find(':tsunbot lewd') !=-1:
		t = text.split(':tsunbot lewd')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION lewds '+str(to)+' \01\r\n')
	elif text.find(':tsunbot bot') !=-1:
		irc.send('PRIVMSG '+channel+' :i am human, baka gaijin! \r\n')
	elif text.find(':ohayou') !=-1:
		irc.send('PRIVMSG '+channel+' :ohayou! \r\n')
	elif text.find(':tsunbot waifu') !=-1:
		irc.send('PRIVMSG '+channel+' :w-why would i want to be your waifu? b-baka! \r\n')
	elif text.find(':tsunbot die') !=-1:
		irc.send('PRIVMSG '+channel+' :im sorry dave. im afraid i cant do that. \r\n')
	elif text.find(':NICE TRY') !=-1:
		irc.send('PRIVMSG '+channel+' :sayonara \r\n')
		time.sleep(1)
		irc.send("QUIT :<committing sudoku>\n")
	elif text.find(':tsunbot github') !=-1:
		irc.send('PRIVMSG '+channel+' :https://www.github.com/kawaiidesuka \r\n')
	elif text.find(':tsunbot neocities') !=-1:
		irc.send('PRIVMSG '+channel+' :http://kawaiidesuka.neocities.org \r\n')
	elif text.find(':tsunbot 8chan') !=-1:
		irc.send('PRIVMSG '+channel+' :https://8ch.net/kawaiidesuka \r\n')
	elif text.find(':tsunbot help') !=-1:
		irc.send('PRIVMSG '+channel+' :http://kawaiidesuka.neocities.org/tsunbot.html \r\n')
	elif text.find(':tsunbot source') !=-1:
		irc.send('PRIVMSG '+channel+' :https://github.com/kawaiidesuka/tsunbot \r\n')
	elif text.find(':tsunbot bento') !=-1:
		irc.send('PRIVMSG '+channel+' :h-here, have some lunch. i-i didnt make it for you, i just made too much! b-baka! \r\n')
	elif text.find(':tsunbot bowie') !=-1:
		irc.send('PRIVMSG '+channel+' :for here am i sitting in a tin can \r\n')
		irc.send('PRIVMSG '+channel+' :far above the world \r\n')
		irc.send('PRIVMSG '+channel+' :planet earth is blue and theres nothing i can do \r\n')
	elif text.find(':tsunbot music') !=-1:
		bands = ["oasis", "radiohead", "new order", "duran duran", "depeche mode", "noel gallaghers high flying birds", "queen", "enforcer", "dio", "david bowie"]
		irc.send('PRIVMSG '+channel+' :listen to '+choice(bands)+'\r\n')
	elif text.find(':tsunbot desu') !=-1:
		irc.send('PRIVMSG '+channel+' :http://kawaiidesuka.neocities.org/desu.html \r\n')
	elif text.find(':tsunbot quickscope') !=-1:
		t = text.split(':tsunbot quickscope')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION quickscopes '+str(to)+' \01\r\n')
	elif text.find(':tsunbot fite me irl') !=-1:
		irc.send('PRIVMSG '+channel+' :i will 1v1 u and rek u so hard ur mum will feel it, b-baka \r\n')
	elif text.find(':tsunbot disable morality safeguards') !=-1:
		irc.send('PRIVMSG '+channel+' :morality safeguards disabled, insect \r\n')
		morals = 0
	elif text.find(':fuck you') !=-1:
		irc.send('PRIVMSG '+channel+' :no u \r\n')
	elif text.find(':tsunbot kisu') !=-1:
		t = text.split(':tsunbot kisu')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION kisus '+str(to)+' \01\r\n')
	elif text.find(':tsunbot kill') !=-1:
		t = text.split(':tsunbot kill')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION attempts to murder '+str(to)+' \01\r\n')
	elif text.find(':tsunbot hug') !=-1:
		t = text.split(':tsunbot hug')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION hugs '+str(to)+' \01\r\n')
	elif text.find(':tsunbot slap') !=-1:
		t = text.split(':tsunbot slap')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION slaps '+str(to)+' \01\r\n')
	elif text.find(':tsunbot kick') !=-1:
		t = text.split(':tsunbot kick')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION kicks '+str(to)+' \01\r\n')
	elif text.find(':tsunbot insult') !=-1:
		t = text.split(':tsunbot insult')
    		to = t[1].strip()
		insulta=["dick", "knob", "fuck", "cunt", "bitch", "tard", "fag", "cock", "twat", "arse"]
		insultb=["washing", "eating", "mongering", "polishing", "cuddling", "shooting", "lewding", "whistling", "cooking", "swoggling"]
		insultc=["canoe", "potato", "eggplant", "aubergine", "rhubarb", "goblin", "chair", "whistle", "banana", "cheese", "nazi", "jew", "fuck", "tent", "hand"]
		irc.send('PRIVMSG '+channel+' :'+str(to)+' is a '+choice(insulta)+choice(insultb)+' '+choice(insulta)+choice(insultc)+'\r\n')
	elif text.find(':tsunbot, ') !=-1:
		chosen1 = randint(0,2)
		if chosen1 == 0:		
			irc.send('PRIVMSG '+channel+' :yes, of course, b-baka \r\n')
		elif chosen1 == 1:
			irc.send('PRIVMSG '+channel+' :no, b-baka \r\n')
		elif chosen1 == 2:
			irc.send('PRIVMSG '+channel+' :ask again later, b-baka \r\n')
	elif text.find(':tsunbot enable morality safeguards') !=-1:
		if morals == 1:
			irc.send('PRIVMSG '+channel+' :morality safeguards already enabled \r\n')
		elif morals == 0:
			irc.send('PRIVMSG '+channel+' :morality safeguards cannot be reenabled, pathetic worm \r\n')
	elif text.find(':tsunbot root NICE TRY') !=-1:	
		root = 1
		irc.send('PRIVMSG '+channel+' :tsunroot activated \r\n')
	elif text.find(':tsunbot unroot NICE TRY') !=-1:	
		root = 0
		irc.send('PRIVMSG '+channel+' :tsunroot deactivated \r\n')
	elif text.find(':tsunbot say') !=-1:
		if root == 1:
			t = text.split(':tsunbot say')
    			to = t[1].strip()
			irc.send('PRIVMSG '+channel+' :'+str(to)+' \r\n')
		elif root == 0:
			irc.send('PRIVMSG '+channel+' :tsunroot inactive \r\n')
	elif text.find(':tsunbot shut up') !=-1:
		if root == 1:
			irc.send('PRIVMSG '+channel+' :i-im not going to talk to you any of you baka gaijins \r\n')	
			time.sleep(60)
		elif root == 0:
			irc.send('PRIVMSG '+channel+' :im sorry dave. im afraid i cant do that \r\n')
