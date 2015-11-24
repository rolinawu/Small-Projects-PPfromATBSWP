""" This Function censors the desired text file"""
def main():

    error_message ="""
***************************************************************
Sorry, something went wrong.
Here are some commmon error:
- Inccorect file name entered for desired file to be censored
- File extensions were not included
Please check if you made any of these errors and try again.
***************************************************************
"""

    try:
        print("This is a program that will help you censor the words that you want")
        fName = input("Please enter the file name: ")
        outfName = input("What is the new file name?: ")
        censor = input("What is the word you want to censor?: ")
        inf = open(fName, 'r') #only read the desired file
        outf = open(outfName, 'w') #write the new file
    
        for line in inf:
            new = ""
            myList = line.split()
            for i in range(len(myList)):
                x = myList[i]
                if x == censor:
                    myList[i] = "*" * len(x)
                new = new + myList[i]+" "
                
            print(new, file = outf) #print new to file outfile

        inf.close()
        outf.close()
    except:
        print(error_message)

main()