#!/bin/bash
# -*- coding: utf-8 -*-
# Program to upload HEX files to PIC18F452
# By Chris Leaver, Aug 2010

# Requires the USPP library downloadable from
# * http://ibarona.googlepages.com/uspp
# * http://www.telefonica.net/web/babur

import time
from uspp import *

port = "/dev/ttyUSB0"

#======================================
# Misc Functions
#======================================#
def txerror(value):
  print "Transmitted data not correctly acknowledged",
  print value
  exit()
  

def hex2dec(s):
  return int(s, 16)
  
def progline(a):
# Now to start sending the actual HEX file...
# Read first line but change : to Z 
# and remove \n\r characters 0x0d and 0x0a (10 and 13)
# The chr() instruction converts an ascii value to a byte characters
    print
    print
    a = a.replace (':' , 'Z')
# replace ';' with 'Z'
    print a,
    mlength = len(a)
    print "length = " ,
    print mlength
    print a[0] # Z?
    tty.write(a[0])
    counter = 1
    
    while mlength > 3:
	b = a[counter] + a[(counter+1)]
	c = int(b,16)
	counter = counter + 2
	print b
	x = chr(c)
	tty.write(x)
	mlength = mlength - 2
	
    while (tty.inWaiting()==0):
	time.sleep(0.01)
  
    a = tty.read(1)
    if a != chr(0x66):
	print "a = ", 
	print a
	txerror(5)
    else:
        print '.'
#=========== MAIN PROGRAM =============



print "PIC 18F452 BOOTLOADER, PC END RUNNING"
print "Input File = main.hex"
hexfilename = "main.hex"
try: datastream = open(hexfilename, 'r') 
except: 
  print "Check you have copied the main.hex file into this directory\n\r"
  exit()

print "Opening Serial Port..."
print port , " @ 19200 Baud, 8-bits, 1 stop, 0 parity"
try: 
  tty=SerialPort(port, 100, 19200)
except:
  print"Error; Check Serial Port Settings And All Wiring Connections\n\r"
  exit()

print "Flushing Cache...\n\r"
tty.flush()
print "Turn ON the target circuit board"
print "Awaiting BOOT message from PIC"
while (tty.inWaiting() < 4):
  time.sleep(0.1)

mystring = tty.read(4)
print mystring
if mystring == 'BOOT':
  print "OK"
else:
  print "Incorrect BOOT message"
  exit()

  
# Send preamble bytes and await replies
time.sleep(0.5)
tty.write('X')
while (tty.inWaiting()==0):
  # no stuff here
  time.sleep(0.01)
a = tty.read(1)
if a != 'x':
  txerror(1)
  
tty.write('P')
while (tty.inWaiting()==0):
  time.sleep(0.01)
a = tty.read(1)
if a != 'p':
  txerror(2)
  
tty.write('B')
while (tty.inWaiting()==0):
  time.sleep(0.01)
a = tty.read(1)
if a != 'b':
  txerror(3)
  
  

tty.write(chr(0x53))
time.sleep(0.01)

tty.write(chr(0x00))
time.sleep(0.01)

tty.write(chr(0x70))
time.sleep(0.01)

tty.write(chr(0x8f))

while (tty.inWaiting()==0):
  time.sleep(0.01)
  
a = tty.read(1)
if a != chr(0x66):
  print "a = ", 
  print a
  txerror(4)

# End of preamble
#------------------------------------

eof = 0
while 1:
    d = datastream.readline()
    if len(d) != 0:
      progline(d)
    else:
      quit()
    
tty.write(chr(0x46))







  
datastream.close()  
print "END...\n\n\r"