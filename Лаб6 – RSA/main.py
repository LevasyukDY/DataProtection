import math
import random


def inverse(a, n):
  if (a % n) != 0:
    result = 1
    while True:
      if ((result * a) % n) == 1:
        return result
      else:
        result += 1
  else:
    return None


def encrypt(message, keys):
  pk = keys[0]
  e = pk[0]
  n = pk[1]
  result = (message ** e) % n
  return int(result)


def decrypt(message, keys):
  sk = keys[1]
  n = sk[1]
  d = sk[0]
  result = (message ** d) % n
  return int(result)


def main():

  print("\n___________СТАРТ ПРОГРАММЫ____________\n")

  p = 13
  q = 17

  n = p * q
  eiler = (q - 1) * (p - 1)
  e = random.randint(3, n - 1)

  gcd = math.gcd(e, eiler)

  while gcd != 1:
    e = random.randint(3, n - 1)
    gcd = math.gcd(e, eiler)

  d = inverse(e, eiler)
  if d is None:
    return print("ОШИБКА!")

  pk = (e, n)
  sk = (d, n)
  keys = pk, sk
  print("Ключи:       ", keys)

  message = 14
  print("Сообщение:   ", message)

  # print(pk[0], sk)
  enc = encrypt(message, keys)
  print("Зашифровка:  ", enc)

  dec = decrypt(enc, keys)
  print("Расшифровка: ", dec)

  print()


if __name__ == '__main__':
  main()