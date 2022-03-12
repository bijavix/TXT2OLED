# bijavix Q1 2022 - Text to arduino OLED array

maxLenght = 21 # Maximum number of characters that the display can hold in a single line 
columnLenght = 3 # How many number of columns to generate before next line (only affects on how the code looks)

#The chunk of data YOU want to convert. You can put it directly here or read it from a text file:
dataRaw = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""
#dataRaw = open("info.txt", "r").read() # Uncomment this line if you are going to read the text from a file

#Remove non-ASCII characters (Ex: á ñ ü) as these can't be correctly displayed by default on the OLED and replace newlines with nothing.
dataRaw = dataRaw.encode("ascii", errors="ignore").decode().replace('\n', '') 

#Open/Create the file where YOU want to save the output. (FILE WILL BE OVERWRITED!)
f = open("oledReady.txt", "w") #Examples: ("C:\\Users\\Me\\Documents\\myFile.txt") or ("myFile.txt")

f.write('char *OledText[] = { \n') # Start the array
clmChk = 0

#Separate all the text into chunks of the needed lenght and write to the file.
for data in range(0, len(dataRaw), maxLenght):
    dt = dataRaw[data:data+maxLenght] # Select the text that's going to get in

    if (clmChk < columnLenght - 1): # Write the text to the file
        f.writelines(['"' + dt + '"' + ', '])
        clmChk += 1
    else: # Write but with new line
        f.writelines(['"' + dt + '"' + ', ' + '\n'])
        clmChk = 0

f.write('"EOF"};') # End the array
f.close # Close the file
