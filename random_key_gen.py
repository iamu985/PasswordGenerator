import random
import string

ALPHA = list(string.ascii_uppercase)
alpha = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list('!#$%&()*+,-./:;<=>?@[\]^_`{|}~.')
#just a joke | list_words = ['_zoinka', '_kamidesuka', '_frank', '_brano', '_gomes', '_kamisama']

head = ['A', 'a', 'n', 's']
dictionary = {
    'A' : ALPHA,
    'a' : alpha,
    'n' : numbers,
    's' : symbols,
    }




class RandomKeyGenerator():
    '''
A program that gives randomly generated password or key for any given length
    '''
    def __init__(self, password_length):
        '''Initialize the variables'''
        self.password_length = int(password_length)
        self.head = head
        self.dictionary = dictionary
        self.password_list = []

    def choose_head(self):
        '''
    Function to choose head
    '''
        random_head = random.choice(self.head)
        return random_head

    def choose_value(self, h_value):
        '''
    Function to choose random value to fill the password length
    '''

        if h_value == self.head[0]:
            value = random.choice(self.dictionary[h_value])
            return value

        if h_value == self.head[1]:
            value = random.choice(self.dictionary[h_value])
            return value

        if h_value == self.head[2]:
            value = random.choice(self.dictionary[h_value])
            return value

        if h_value == self.head[3]:
            value = random.choice(self.dictionary[h_value])
            return value

    def run(self):
        '''Prgram to run'''
        for length in range(self.password_length):
            call_head = RandomKeyGenerator(self.password_length).choose_head()
            place_value = RandomKeyGenerator(self.password_length).choose_value(call_head)
            self.password_list.append(place_value)

        password = ''.join(self.password_list)

        return password

if __name__ == '__main__':
    ask_len = int(input('Enter Password Length: '))
    generate = RandomKeyGenerator(ask_len)
    get_pass = generate.run()
    print(get_pass)
