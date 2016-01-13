import socket
import sys
import time
from random import randint
from random import choice

server = "irc.freenode.net"
channel = "#CHANNEL"
botnick = "BOTNICK"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :desu\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("PRIVMSG nickserv :identify PASSWORD\n")
time.sleep(20)
morals = 1
irc.send("JOIN "+ channel +"\n")
irc.send('PRIVMSG '+channel+' :i-its not like ive been waiting to see you or anything, b-bakas \r\n')
while 1:
	text=irc.recv(2040)
	print text
	if text.find('PING') != -1:
		irc.send('PONG ' + text.split() [1] + '\r\n')
#action
	if text.find(':BOTNICK ACTION') !=-1:
		t = text.split(':BOTNICK ACTION')
    		to = t[1].strip()
		irc.send('PRIVMSG '+channel+' :\01ACTION ACTION '+str(to)+' \01\r\n')
	if text.find(':BOTNICK COMMAND') !=-1:
		irc.send('PRIVMSG '+channel+' :RESPONSE \r\n')