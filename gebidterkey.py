import os
import random
import sys
import time
from time import sleep
os.system( 'clear' )
def mengetik(s):
   for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(random.random() * 0.4)
a ='\033[92m'
b ='\033[91m'
c ='\033[93m'
d ='\033[95m'
e ='\033[94m'
print (a+'Loading...')
sleep(0.1)
mengetik(c+' > > > > > > > > > > > | 100%')
os.system('clear')

print(a+'\t  Shorcut for help you')
print(b+'\t   GebidInfo')
print(c+'\t  IG : hallo_catur & zslam3')

print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+d+'\n\nThanks Have A Nice Day\n\n')
print(c+'Good Bye')
# ini cuma shortcut buat bantu para nub

