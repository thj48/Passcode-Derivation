#Programmed by Terry Holt
#Version 1.0.1
#February 26, 2015
#Keylogger Interpreter Program: problem 79, https://projecteuler.net/problem=79 

'''FileReader object that reads information from files'''
class FileReader:

    '''Reads from the file and sends it to the decryptor'''
    def readFile(self, fileName, decryptor):
        self.__file = open(fileName,"r")

        lines = self.__file.readlines()
        decryptor.setInfo(lines)

        self.__file.close()

#------------------------------------------------------

'''Decryptor class that finds password from the file'''
class Decryptor:

    __password = ""

    '''Sets the variables and calls decrypt'''
    def setInfo(self,lines):
        self.__lines = lines
        self.__decrypt()

    '''Returns the password'''
    def getPassword(self):
        return self.__password
    
    def __decrypt(self):
        count = 0;
        for line in self.__lines:
            count = count+1
            line = line.strip()
            self.__configurePassword(line)

    def __configurePassword(self, line):
        if self.__password == "" :
            self.__password = line
        else:
            self.__computeLine(line)

    def __computeLine(self, line):
        count = 0

        for number in line:
            
            if number in self.__password:
                count += line.index(number) + 2
                
        self.__insertLineToPassword(line, count)

    def __insertLineToPassword(self, line, count):
        firstNum = line[:1]
        secondNum = line [1:2]
        thirdNum = line [2:]

        if count == 0:
            self.__password += line
            
        elif count == 2:
            self.__setPassword(firstNum,line)

        elif count == 3:
            self.__setPassword(secondNum,line)
                
        elif count == 4:
            self.__setPassword(thirdNum,line)

        elif count == 5:
            self.__checkAndRearrangePosition(firstNum,secondNum)
            self.__password += thirdNum
            
        elif count == 6:
            self.__checkAndRearrangePosition(firstNum,thirdNum)
            self.__setPassword(firstNum, firstNum+secondNum)
            
        elif count == 7:
            self.__checkAndRearrangePosition(secondNum,thirdNum)
            self.__setPassword(secondNum, firstNum+secondNum)

        elif count == 9:
            self.__checkAndRearrangePosition(secondNum,thirdNum)
            self.__checkAndRearrangePosition(firstNum,secondNum)

    def __setPassword(self, original, new):
             self.__password = self.__password.replace(original, new)

    def __checkAndRearrangePosition(self, firstNum, secondNum):
        firstNumPosition = self.__password.index(firstNum)
        secondNumPosition = self.__password.index(secondNum)
        
        if firstNumPosition > secondNumPosition:
            self.__password = self.__password.replace(firstNum, "")
            self.__password = self.__password.replace(secondNum, firstNum+secondNum)

#--------------------------------------------------------------------

'''Main entrance/controller of the program''' 
def main():
    decryptor = Decryptor()
    fileReader = FileReader()
    fileReader.readFile("keylog.txt",decryptor)
    password = decryptor.getPassword()
    print ("Password: " + password)

main()
