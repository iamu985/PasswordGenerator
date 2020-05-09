import random

class PasswordGenerator():
    '''Randomly generates a password,
    password consists of lower and uppercase letters, numbers and symbols'''

    def variables():
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        lower = [letters for letters in alpha]
        upper = [letters.upper() for letters in alpha]
        number = [i for i in range(10)]
        char = '!@#$%^&*_;:|\,.?/'
        symbols = [sym for sym in char]

        choices = {
            'u' : upper,
            'l' : lower,
            'n' : number,
            's' : symbols,
            }
        return choices

    def __init__(self, passlen=8, var = variables()):
        self.passlen = passlen
        self.var = var
        self.password = []

class Checks(PasswordGenerator):

    def __init__(self, passlen=8, var = PasswordGenerator.variables()):
        super().__init__ (passlen=8, var = PasswordGenerator.variables())
        

    def checkUpper(self):
        '''Checks if there is the desired number of upper cases in the password'''
        '''Example if the password has more than 2 uppercases for 8 char length
            this code removes terminates the condition before it happens'''
        upperTrue = [items for items in self.password if items in self.var['u']]
        unwanted = []
        count = upperTrue.count()
        return count

    def checkLower(self):
        lowerTrue = [items for items in self.password if items in self.var['l']]
        unwanted = []
        count = lowerTrue.count()
        return count

    def checkNumbers(self):
        numbTrue = [items for items in self.password if items in self.var['n']]
        unwanted = []
        count = numbTrue.count()
        return count

    def checkSymbols(self):
        charTrue = [items for items in self.password if items in self.var['s']]
        unwanted = []
        count = charTrue.count()
        return count

class Fills(PasswordGenerator):

    def __init__ (self, passlen=8, var = PasswordGenerator.variables()):
        super().__init__(passlen=8, var = PasswordGenerator.variables())

    def fillUpper(self):
        '''fills an empty password field with upper cases'''
        upper = random.choice(self.var['u'])
        self.password.append(upper)
        return self.password

    def fillLower(self):
        '''fills the password field with lower cases'''
        lower = random.choice(self.var['l'])
        self.password.append(lower)
        return self.password()

    def fillNumb(self):
        '''fills the password field with numbers'''
        numb = random.choice(self.var['n'])
        self.password.append(numb)
        return self.password

    def fillChar(self):
        '''fills the password field with chars'''
        char = random.choice(self.var['s'])
        self.password.append(char)
        return self.password



    def generate(self):
        while len(self.password) < self.passlen:
            #for algo ulns
            Fills.fillUpper()
            upperCheck = Checks.checkUpper()
            if upperCheck < 2:
                Fills.fillUpper()
            lowerCheck = Checks.checkLower()
            if lowerCheck < 2:
                Fills.fillLower()
            numbChk = Checks.checkNumbers()
            if numbChk < 2:
                Fills.fillNumb()
            charCheck = Checks.checkSymbols()
            if charCheck < 2:
                Fills.fillChar()

        return self.password
            
        



if __name__ == '__main__':
    call = PasswordGenerator()
    print(call)
