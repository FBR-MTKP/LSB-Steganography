# Name: Ashour Dankha
# Title of Program: Steganography
# Language: JES (Jython Enviornment for Students)
#
# Purposes: 
# 1. The ability to embed a message in a sound file.
# 2. The ability to extract a message from a sound file.
#
# Approach:
#
# For embedding a message to a sound file:
# Iterate through each sound sample
# Grab the amplitude of each sample and smoothe it.
# Since an ASCII character is 0-127, we smoothe the last 7 bits.
# We smoothe by using modulos operation.
#
# For extracting a message from a sound file:
# Traverse through each sound sample and take modulos 128 of the amplitude
# to grab the last 7 bits. From here, we append to a string variable and finito!


# The following function is a helper function to help smoothe the soundObject samples.
# Since we are working with text, we know that a character can range from 0-127 (128)
# 128 is 7 bits (2^7)
# Since we know this fact, we know that a character cannot exceed this number.
# If we grab each amplitude value use the modulos operator with 128
# We will esentially hold the value to use for our subtraction to smoothe
# Example: 8018 mod 128 = 82
# our new amp value will then be 8018 - 82 = 7936
# If we convert 7936 in binary, we get: 0b1111100000000
# Notice that the last 7 bits are zeroes.
# We set them to 0's so that we can use them to 'insert' our character (ranging from 0-127)
def smootheSamples(samples, sLength):
   
  for i in range(sLength):
    ampValue = getSampleValue(samples[i])
    lsValue = ampValue % 128
    modAmpValue = ampValue - lsValue
    setSampleValue(samples[i], modAmpValue)


# The following function encodes our message.
# First it feeds the samples to our helper function smootheSamples()
# After it has smoothed the amp values, it traverses through the string
# and places the string in the samples
# Note: Remember, since we smoothed our amp values, it will add to our 7 bits.
# Once we added our characters / msg to our soundObject, we can then save it
# We now have a sound with a message embedded in it!! 
def encodeMessage(soundObject, msg):

  explore(soundObject)
  
  samplesList = getSamples(soundObject)
  
  # Hold the lengths of what we iterate through
  sLength = getLength(soundObject)
  msgLength = len(msg)
  
  # Smoothe the samples of the sound object
  smootheSamples(samplesList, sLength)
  
  # Traverse through the message and insert into samples list
  for i in range(msgLength):
    ampValue = getSampleValue(samplesList[i])
    finalAmpValue =  ampValue + ord(msg[i])
    setSampleValue(samplesList[i], finalAmpValue)
    
  explore(soundObject)
  f = pickAFile()
  writeSoundTo(soundObject, f)


# The following function extracts a message.
# This function ismply traverses through the sound object
# uses the modulos operator with 128 on the amplitude to get the 7 bits (in decimal)
# then converts the decimal to a character and appends to an empty string.
def extractMessage(soundObject):

  samplesList = getSamples(soundObject)
  sLength = getLength(soundObject)
  extractedMessage = ''
  
  for i in range(sLength):
    ampValue = getSampleValue(samplesList[i])
    charAscii = ampValue % 128
    # if charAscii is 0, then we've reached a smoothed value so our message is complete.
    if charAscii == 0:
      break
    letter = chr(charAscii)
    extractedMessage += letter
    
  showInformation(extractedMessage)


# Main driver program to prompt user for embedding or extracting a message to/from a sound file
def main():

  userInput = requestIntegerInRange('Enter 1 for embedding or 2 for extracting', 1, 2)
  f = pickAFile()
  s = makeSound(f)
  if userInput == 1:
    userMessage = requestString('Enter the string you want to encode:')
    encodeMessage(s, userMessage)  
  else:
    extractMessage(s)

main()
