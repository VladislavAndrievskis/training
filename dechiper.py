from dataclasses import replace


class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in original_text:
            position = self.alphabet.find(letter.lower())
            if position == -1:
                result.append(letter)
            else:
                result.append(self.alphabet[(position + shift) % len(self.alphabet)])
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            position = self.alphabet.find(letter.lower())
            if position == -1:
                result.append(letter)
            else:
                result.append(self.alphabet[(position - shift) % len(self.alphabet)])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))