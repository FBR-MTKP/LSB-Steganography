# Steganography
A simple Steganography program to embed and/or extract a message from a sound file (.WAV)
Created By: Ashour Dankha
Title of Program: Steganography
Language: JES (Jython Enviornment for Students)

Purposes: 
1. The ability to embed a message in a sound file.
2. The ability to extract a message from a sound file.

Approach:

For embedding a message to a sound file:
Iterate through each sound sample
Grab the amplitude of each sample and smoothe it.
Since an ASCII character is 0-127, we smoothe the last 7 bits.
We smoothe by using modulos operation.

For extracting a message from a sound file:
Traverse through each sound sample and take modulos 128 of the amplitude
to grab the last 7 bits. From here, we append to a string variable and finito!

# To Download JES (WINDOWS): 
https://github.com/gatech-csl/jes/releases/download/5.020/jes-5.020-windows.exe
# To Download JES (Mac OS):
https://github.com/gatech-csl/jes/releases/download/5.020/jes-5.020-macosx.zip
