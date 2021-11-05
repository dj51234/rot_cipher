import string

letters = string.ascii_lowercase

class RotCipher:

    def __init__(self, rot_amount, a=letters):
        self.rot_amount = rot_amount 
        self.alpha = a
        self.rot_alphabet = []
        self.e = []
        self.d = []

    def create_rot_alphabet(self):
        for i in range(len(self.alpha)):
            if self.alpha.index(self.alpha[i]) < self.rot_amount and i + self.rot_amount <= len(self.alpha) - 1:
                new_letter = self.alpha[i + self.rot_amount]

            elif i + self.rot_amount > len(self.alpha) - 1:
                remainder = len(self.alpha) - self.alpha.index(self.alpha[i]) # q = 16, 25 - 16 = 9, 15-9 = correct letters index
                new_index = self.rot_amount - remainder
                new_letter = self.alpha[new_index]

            self.rot_alphabet.append(new_letter)

    def encrypt(self, text):
        self.create_rot_alphabet()
        for letter in text:
            self.e.append(self.rot_alphabet[self.alpha.index(letter)])

        self.encrypted = ''.join(self.e)
        return self.encrypted
    
    def decrypt(self, text):
        self.create_rot_alphabet()
        # self.text = text
        for letter in text:
            self.d.append(self.alpha[self.rot_alphabet.index(letter)])

        self.decrypted = ''.join(self.d)
        return self.decrypted
    
    def __str__(self):
        return f'Your word has been converted to {self.encrypted}'