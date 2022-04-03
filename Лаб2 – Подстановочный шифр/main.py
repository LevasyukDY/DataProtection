import numpy as np
import math
import itertools


# Получаем нужную перестановку по индексу из файла sets.txt
def get_alphabet(number):

  f = open('sets.txt', 'r')
  for line in f:
    alphabet_lst = line.split(' ')
    alphabet = alphabet_lst[1].replace('\n', '')
    if alphabet_lst[0] == f'{number}':
      # print(f'Перестановка #{alphabet_lst[0]}: {alphabet}\n')
      return alphabet


# Генерирует все перестановки заданного алфавита в файл sets.txt
def gen_permutations(alphabet):
  
  f = open('sets.txt', 'w')

  amount = math.factorial(len(alphabet))
  
  lst = [''.join(p) for p in itertools.permutations(alphabet)]

  for index in range(amount):
    f.write(f'{index + 1} {lst[index]}\n')

  f.close()


# Шифр Хилла (полиграммный шифр)
def encrypting(alphabet, input_string, M, matrix, vector):

  N = len(alphabet)
  print('N =', N)

  print('Матрица:')
  print(matrix)
  print()

  print('Обратная матрица:')
  inv_matrix = np.linalg.inv(matrix)
  # Приводим обратную матрицу к положительным значениям
  i, j = 0, 0
  for i in range(M):
    for j in range(M):
      while inv_matrix[i][j] < 0:
        inv_matrix[i][j] += N
  print(inv_matrix)
  print()

  print('Произведение матриц:')
  mul_matrix = np.dot(matrix, inv_matrix)
  print(mul_matrix)
  print()

  print('Деление с остатком на N:')
  mod_matrix = mul_matrix % N
  print(mod_matrix)
  print()

  print('Вектор B:')
  print(vector)
  print()

  if len(input_string) % M != 0:
    input_string += '_'

  print('Алфавит:', alphabet)
  print()

  result_string = ''
  j = 0
  step = 0
  for i in range(0, len(input_string), M):
    step += (j + 1)
    print(f'Шаг #{step}:')
    pair = input_string[i] + input_string[i+1]
    print('  Пара:', pair)

    indexes_of_pair = np.array(
        [alphabet.find(pair[0]), alphabet.find(pair[1])]
    )
    print('  Индексы пары:', indexes_of_pair)

    Y = ((np.dot(indexes_of_pair, matrix)) + vector) % N
    print('  Новые индексы:', Y)  

    new_pair = alphabet[Y[0]] + alphabet[Y[1]]
    print('  Новая пара:', new_pair)

    print()
    result_string += new_pair

  print('Исходная строка:      ', input_string)
  print('Зашифрованная строка: ', result_string)

  print('\n')
  return result_string


# Расшифровка сообщения (обратный ход)
def decrypting(alphabet, encrypt_string, M, matrix, vector, is_print=False):

  N = len(alphabet)
  if is_print: print('N =', N)

  if is_print: print('Обратная матрица:')
  inv_matrix = np.linalg.inv(matrix)
  # Приводим обратную матрицу к положительным значениям
  i, j = 0, 0
  for i in range(M):
    for j in range(M):
      while inv_matrix[i][j] < 0:
        inv_matrix[i][j] += N
  if is_print: print(inv_matrix)
  if is_print: print()

  if len(encrypt_string) % M != 0:
    encrypt_string += '_'

  if is_print: print('Алфавит:', alphabet)
  if is_print: print()

  decrypt_string = ''
  j = 0
  step = 0
  for i in range(0, len(encrypt_string), M):
    step += (j + 1)
    if is_print: print(f'Шаг #{step}:')
    pair = encrypt_string[i] + encrypt_string[i+1]
    if is_print: print('  Пара:', pair)

    indexes_of_pair = np.array(
      [alphabet.find(pair[0]), alphabet.find(pair[1])]
    )
    if is_print: print('  Индексы пары:', indexes_of_pair)

    Y_minus_B = indexes_of_pair - vector
    # Приводим массив к положительным значениям
    # k = 0
    # for k in range(M):
    #   while Y_minus_B[k] < 0:
    #     Y_minus_B[k] += N
    Y_minus_B_mul_invA = np.dot(Y_minus_B, inv_matrix)
    X = Y_minus_B_mul_invA % N
    if is_print: print('  Новые индексы:', X)  

    np_n1 = np.around(X[0])
    np_n2 = np.around(X[1])

    int_n1 = int(np_n1)
    int_n2 = int(np_n2)

    new_pair_n1 = alphabet[int_n1]
    new_pair_n2 = alphabet[int_n2]

    new_pair = new_pair_n1 + new_pair_n2
    if is_print: print('  Новая пара:', new_pair)

    if is_print: print()
    decrypt_string += new_pair

  if is_print: print('Зашифрованная строка:  ', encrypt_string)
  if is_print: print('Расшифрованная строка: ', decrypt_string)

  if is_print: print('\n')

  return decrypt_string


# Атака полным перебором
def hack(encrypt_string, M, matrix, vector):
  
  count = count_lines('sets.txt')

  alphabet = ''

  f = open('keys.txt', 'w')

  for key in range(1, count + 1):
    alphabet = get_alphabet(key)
    f.write(f'Возможный ключ {key}: {decrypting(alphabet, encrypt_string, M, matrix, vector)}\n')

  f.close()


# Подсчёт количества строк в файле
def count_lines(filename, chunk_size=1<<13):
  with open(filename) as file:
    return sum(chunk.count('\n')
      for chunk in iter(lambda: file.read(chunk_size), ''))



def main():
  print('\n__________СТАРТ ПРОГРАММЫ__________\n')
  
  alphabet = '_АОУНТК'
  input_string = 'А_КОТ_ТУТ_КАК_ТУТ'

  # alphabet = '_АТИНЯ'
  # input_string = 'НАТА_И_ТАНЯ'

  # Размерность матрицы
  M = 2
  print('M =', M)

  # Генерируем все возможные перестановки исходного алфавита
  gen_permutations(alphabet)

  # Получаем нужную перестановку по индексу из файла sets.txt
  alphabet = get_alphabet('100')

  # matrix = np.random.randint(0, len(alphabet), (M, M))
  # vector = np.random.randint(0, len(alphabet), M)

  # print(matrix)
  # print(vector)

  # Произвольная матрица А, имеющая обратную матрицу
  matrix = np.array(
    [
      [5, 1], 
      [1, 0]
    ]
  )

  # Произвольный вектор B
  vector = np.array(
      [2, 4]
  )

  # Определитель матрицы А
  print('det =', np.linalg.det(matrix))
  print()

  encrypt_string = encrypting(alphabet, input_string, M, matrix, vector)
  decrypt_string = decrypting(alphabet, encrypt_string, M, matrix, vector, True)

  hack(encrypt_string, M, matrix, vector)


if __name__ == '__main__':
  main()