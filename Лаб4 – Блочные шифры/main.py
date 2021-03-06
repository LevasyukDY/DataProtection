import random


list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

message = "VL"
byteList = []
table31 = []
table15 = []

tableP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


def encrypt(list, text):
  print()
  print('========== Шифрование ==========')
  bytes = getBin32(list, text)
  print("32 байта:\n", bytes)
  print()

  pblock = PBlock(bytes)
  print("Зашифрованная p-блоком битовая форма:\n", pblock)
  print()

  sblock = SBlock(pblock)
  print("Зашифрованная батареей s-блоков битовая форма:\n", sblock)
  # print(decSBlock(convert))
  print()

  result = PBlock(sblock)
  print("Зашифрованная p-блоком битовая форма:\n", result)

  print()
  mess = getStrFromBin(result)
  print("Зашифрованное сообщение:", mess)
  return result


def decrypt(text):
  print()
  print('========= Расшифрование =========')
  decrypted = decPBlock(text)
  print("Расшифрованная p-блоком битовая форма:\n", decrypted)

  print()
  decS = decSBlock(decrypted)
  print("Расшифрованная батареей s-блоков битовая форма:\n", decS)

  print()
  res = decPBlock(decS)
  print("Расшифрованная p-блоком битовая форма:\n", res)

  print()
  mess = getStrFromBin(res)
  print("Расшифрованное сообщение:", mess)
  print()
  return res
  

def randTable():
  random.shuffle(list2)
  random.shuffle(list1)

  count = 0
  while count <= 31:
    table31.append(list2[count])
    count += 1
  count = 0
  while count <= 15:
    table15.append(list1[count])
    count += 1


def toBin(list, text):
  for c in range(len(text)):
    list.append(str(bin(ord(text[c])))[2:].rjust(16, '0'))


def getBin32(list, text):
  toBin(list, text)
  result = ""
  for item in list:
    result += str(item)
  return result


def PBlock(text):
  result = ""
  for num in table31:
    result += text[num]
  return result


def SBlock(bytes):
  convert = ""
  num = 0
  while num < len(bytes):
    result = ""
    result += bytes[num:num + 4]
    convert += encrypt4byte(result)
    num += 4
  return convert


def decPBlock(text):
  result = ""
  num = 0
  for num in tableP:
    for i in range(len(table31)):
      if table31[i] == num:
        index = i
        result += text[index]
  return result


def decSBlock(convert):
  decrypted = ""
  num = 0
  while num < len(convert):
    result = ""
    result += convert[num:num + 4]
    decrypted += decrypt4byte(result)
    num += 4
  return decrypted


def encrypt4byte(text):
  decimal = int(text, 2)
  encrypted_decimal = str(bin(list1[decimal]))[2:]
  return encrypted_decimal.rjust(4, "0")


def decrypt4byte(text):
  decimal = int(text, 2)
  for num in range(len(list1)):
    if decimal == list1[num]:
      result = str(bin(num))[2:].rjust(4, '0')
      return result


def getStrFromBin(string):
  result = ""
  num = 0
  while num < len(string):
    result += chr(int(string[num:num + 8], 2))
    num += 8
  return result



def main():
  print("\n___________СТАРТ ПРОГРАММЫ____________\n")
  print("Введите сообщение для зашифровки (2 символа): ")
  message = input()
  print()

  print("Сообщение: ", message)
  randTable()

  a = encrypt(byteList, message)
  decrypt(a)


if __name__ == '__main__':
  main()