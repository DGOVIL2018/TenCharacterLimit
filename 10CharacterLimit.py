#Dhruv Govil Period 2 March 5 2016
#Ten Character Limit Program

ifh = open("INPUT.txt", "r")
ofh = open("OUTPUT.txt", "w+")

#for each line in the file, until end of file is reached
for inLine in ifh:
    outLine = inLine[0 : 10] #assign the first 10 characters of inLine string to outLine string
    ofh.write(outLine) #write outLine string to the output file
    

ifh.close()
ofh.close()


