import random

key = []
gen = []
gamma = []


def generate_key():
  for i in range(256):
    key.append(i)
  random.shuffle(key)
  for i in range(256):
    gen.append(key[i])


def generation_random_numbers():
  j = 0
  for i in range(256):
    j = (j + gen[i] + key[i]) % 256
    gen[j], gen[i] = gen[i], gen[j]
  return gen


def create_gamma(message, gen):
  temp = gen

  i, j = 0, 0
  for k in range(len(message)):
    i = (i + 1) % 256
    j = (j + temp[i]) % 256
    temp[i], temp[j] = temp[j], temp[i]
    t = (temp[i] + temp[j]) % 256
    gamma.append(temp[t])
  return gamma


def str2bin(message):
  list = []
  for i in range(len(message)):
    list.append(bin(ord(message[i]))[2:].zfill(16)[:8])
    list.append(bin(ord(message[i]))[2:].zfill(16)[8:])

  result = []

  for elem in list:
    num = 0
    str = elem[::-1]  # переворачиваем elem
    for i in range(len(str)):
      num += int(str[i]) * (2 ** i)
    result.append(num)
  return result


def bin2str(message):
  symbols = ""
  num = 0
  while num < len(message):
    bit1 = bin(message[num])[2:].zfill(8)
    bit2 = bin(message[num+1])[2:].zfill(8)

    number = bit1 + bit2
    number = number[::-1]
    bit = 0
    for i in range(len(number)):
      bit += int(number[i]) * (2 ** i)

    symbols += chr(bit)
    num += 2
  return symbols


def encrypt(message, gamm):
  bytes = []
  for i in range(len(message)):
    bytes.append(message[i] ^ gamm[i])
  return bytes


def decrypt(message, gamm):
  bytes = []
  for i in range(len(message)):
    bytes.append(message[i] ^ gamm[i])
  return bytes


def main():
  print("\n___________СТАРТ ПРОГРАММЫ____________\n")
  generate_key()

  print("Ключ:   ", key[:10])

  generation_random_numbers()
  print("Массив: ", gen[:10])

  print()
  print("Введите сообщение: ")
  message = input()

  print()
  print("Сообщение:", [ord(letter) for letter in message])

  print()
  split = str2bin(message)
  print("Пары байтов:\n", split)

  print()
  create_gamma(split, gen)
  print("Гамма:\n", gamma)

  print()
  enc = encrypt(split, gamma)
  print("Зашифрованное сообщение:\n", enc)

  print()
  symbols = bin2str(enc)
  print("Символы: ", symbols)

  print()
  unsplit = str2bin(symbols)
  print("Расшифрованные символы:\n", unsplit)

  print()
  decr = decrypt(unsplit, gamma)
  print("Расшифрованное сообщение:\n", decr)

  print()
  end = bin2str(decr)
  print("Итоговое сообщение:\n", end)

  print()


if __name__ == '__main__':
  main()