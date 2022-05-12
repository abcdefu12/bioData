a = 1
b = 2
c = 3.5
d = abs(a - b * c)
print('d =', d)

# 근의 공식
a = 2
b = 5
c = 1
x1 = (-b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
print('x1 =', x1)
print('x2 =', x2)

# max, min
a = [1, 20, 35, 0.4, 25, 109]
# a.sort()
# minValue = a[0]
# maxValue = a[-1]
# print(minValue)
# print(maxValue)
print('min of a:', min(a))
print('max of a:', max(a))

# 1부터 10까지 더하기
a = 0
sumVal = 0
while a < 10:
    a += 1
    sumVal += a
print('sum of 1 to 10:', sumVal)
