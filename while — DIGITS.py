#DIGITS
n = 3545767
maximum = 0
minimum = 9
product = 1
count_even = 0
s=0
while n > 0:
    last = n % 10
    product = product * last
    if last > maximum :
        maximum = last
    if last < minimum :
        minimum = last
    if last % 2 == 0:
        count_even = count_even + 1
        s += last
    n = n//10
print(f"Самая большая цифра = {maximum}")
print(f"Самая маленькая цифра = {minimum}")
print(f"Произведение всех цифр = {product}")
print(f"Количество четных цифр = {count_even}")
print(f"Сумма всех цифр = {s}")

number = 1234567890
count = 0
while number > 0:
    last_digit = number % 10
    if last_digit < 3:
        count = count + 1

    number = number // 10
    #print(last_digit)
    #print(number)
print(count)

number = 73408457689456878678695656757696789678956776786586796958546784567857897967956745745745678579678979
m = 0
s = 0
while number > 0:
    last_digit = number % 10
    s = s + last_digit
    if last_digit > m:
        m = last_digit
    number = number // 10
    #print(s, m)
print(s + m)

number = 73408
print(*reversed(str(number)), sep='\n')

number = '34'

from time import process_time, sleep
start = process_time() ## точка отсчета времени
n = int(number)
s=0
while n > 0:
    last = n % 10
    if last == 7:
        s += 1
    n = n//10
print(s)
end = process_time() ## собственно время работы программы
print(end-start) ## вывод времени

start = process_time() ## точка отсчета времени
n = list(number)
count = 0
while '7' in n:
    n.remove('7')
    count += 1
print(count)
end = process_time() ## собственно время работы программы
print(end-start) ## вывод времени

start = process_time() ## точка отсчета времени
print(number.count('7'))
end = process_time()## собственно время работы программы
print(end-start) ## вывод времени

#in binary
n = (int(number))
while n > 0:
    last = n % 2
    print(last,end='')
    n = n//2
print('\n---------------\n')
start = process_time()  ## точка отсчета времени
n = (int(number))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i+=1
end = process_time() ## собственно время работы программы
print(end-start) ## вывод времени

print('---------------\n')

start = process_time() ## точка отсчета времени
n = (int(number))
i = 1
while i <= n//2:
    if n % i == 0:
        print(i, end=' ')
    i+=1
print(n)
end = process_time() ## собственно время работы программы
print(end-start) ## вывод времени
print('---------------\n')

start = process_time() ## точка отсчета времени
k = 1
r = []
while k <= n:
  if n % k == 0:
    r.append(k)
  k += 1
print(*r, sum(r))

end = process_time() ## собственно время работы программы
print(end-start) ## вывод времени
a1=a = 14
b1=b = 21

start = process_time() ## точка отсчета времени

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'Нод={a}')
end = process_time() - start ## собственно время работы программы
print(end) ## вывод времени

a = a1
b = b1
start = process_time() ## точка отсчета времени
c = a * b
while b > 0:
    a, b = b, a % b

print(f'Нод={a}')
print(f'Нок={int(c / a)}')
end = process_time() - start ## собственно время работы программы
print(end) ## вывод времени