# Steganography
A simple Steganography program to embed and/or extract a hidden message to/from a sound file (.WAV)

###### Language: 
JES (Jython Enviornment for Students)

## Purposes: 
1. To embed a message in a sound file.
2. To extract a message from a sound file.

## Approach:

###### For embedding a message to a sound file:
Iterate through each sound sample
Grab the amplitude of each sample and smoothe it.
Since an ASCII character is 0-127, we smoothe the last 7 bits.
We smoothe by using modulos operation.

###### Before embedding a message:
![alt text](https://i.imgur.com/1oSwT3B.png)

###### For extracting a message from a sound file:
Traverse through each sound sample and take modulos 128 of the amplitude
to grab the last 7 bits. From here, we append to a string variable and finito!

###### After extracting a message:
![alt text](https://i.imgur.com/ZJ687Ol.png)

## To Download JES (WINDOWS): 
https://github.com/gatech-csl/jes/releases/download/5.020/jes-5.020-windows.exe
## To Download JES (Mac OS):
https://github.com/gatech-csl/jes/releases/download/5.020/jes-5.020-macosx.zip


###### Disclaimer:
You must download JES and use the IDE in order for this .py file to work.
