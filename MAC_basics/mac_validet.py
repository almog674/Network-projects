class Mac_validetor:
    letters_bank = ['a', 'b', 'c', 'd', 'e', 'f', ':', 'A', 'B', 'C', 'D', 'E', 'F']
    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.check_validate()

    def check_seperations(self):
        split_address = self.mac_address.split(sep=':')
        if len(split_address) != 6:
            return 'invalid'
        else:
            return 'valid'

    def check_parts(self):
        split_address = self.mac_address.split(sep=':')
        for part in split_address:
            if len(part) != 2:
                return 'invalid'
        return 'valid'

    def check_length(self):
        if len(self.mac_address) != 17:
            return 'invalid'
        else:
            return 'valid'


    def check_digits(self):
        for digit in self.mac_address:
            if (digit.isdigit() == False) and digit not in self.letters_bank:
                return 'invalid'
        return 'valid'

    def check_type(self):
        split_address = self.mac_address.split(sep=':')
        first_byte = split_address[0]
        scale = 16
        result = bin(int(first_byte, scale)).zfill(8)
        important_bit = result[len(result) - 1]
        if important_bit == "1":
            return 'Multicast'
        else:
            return 'Unicast'

    def check_validate(self):
        ans1 = self.check_length()
        ans2 = self.check_seperations()
        ans3 = self.check_parts()
        ans4 = self.check_digits()
        if ans1 != 'valid':
            print('The length has to be 17 characters')
        elif ans2 != 'valid':
            print('The seperation needed to be ":"')
        elif ans3 != 'valid':
            print('The address needs to be sepereted to 6 parts')
        elif ans4 != 'valid':
            print('all of the characters have to be hexadecimal')
        else:
            print(self.mac_address + ' Is a valid address')
            type_of_address = self.check_type()
            print('The address type is: ' + type_of_address)

        



almog = Mac_validetor('12:22:33:44:55:66')
a = Mac_validetor('FF:FF:FF:FF:FF:FF')
s = Mac_validetor('AB:12:cd:34:31:21')
f = Mac_validetor('11:22:33:44:55:66:77')
b = Mac_validetor('66-55-44-33-22-11')
k = Mac_validetor('11:22:33:44:55')
p = Mac_validetor('H:22:33:44:55:661')


