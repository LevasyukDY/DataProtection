def encrypt(inp_mess, key, al):
    out_mess = ''
    for symbol in inp_mess:
        position = al.find(symbol)
        new_position = (position + key) % len(al)
        if symbol in al:
            out_mess = out_mess + al[new_position]
        else:
            out_mess = out_mess + symbol
    return out_mess

def decrypt(inp_mess, key, al):
    out_mess = ''
    for symbol in inp_mess:
        position = al.find(symbol)
        new_position = (position - key) % len(al)
        if symbol in al:
            out_mess = out_mess + al[new_position]
        else:
            out_mess = out_mess + symbol
    return out_mess

def hack(inp_mess, al):
    for key in range(len(al)):
        print(f'Возможный ключ #{key}: {decrypt(inp_mess, key, al)}')


al = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

choice = input('Выберите что нужно сделать (зашифровать/расшифровать/хакнуть): ').lower()
inp_mess = input('Введите сообщение: ').upper()

if choice == 'зашифровать':
    key = int(input('Введите ключ: '))
    print()
    print(encrypt(inp_mess, key, al))
elif choice == 'расшифровать':
    key = int(input('Введите ключ: '))
    print()
    print(decrypt(inp_mess, key, al))
elif choice == 'хакнуть':
    print()
    hack(inp_mess, al)
