f = open('data.txt', 'r')
data = f.readlines()

data1 = 0
mean = 0
totalSum = 0
totalDouble = 0
vari = 0
i = 0
totalTwice = 1
totalList = []

for line in data:
    line = line.replace('\n', '')
    totalSum = totalSum + float(line)
    totalDouble = totalDouble + float(line)*float(line)
    totalTwice = totalTwice * float(line)
    totalList.append(float(line))
    i += 1

    # data1_str = data1_str.split('\n')
    # data1 = float(data1_str)
    # data2 = data1_str.split('\n')
    # data1 = int(data1_str)
f.close()

mean = totalSum / i
vari = totalDouble / i - mean**2
# 분산 = 제곱의평균 - 평균의제곱

# median
totalList.sort()
if len(totalList) % 2 == 1:
    median = totalList[int((len(totalList) - 1) / 2)]
else:
    median = totalList[len(totalList) / 2]



# Mean, variance, and standard deviation
print('---------------------')
print('totalSum:', totalSum)
print('totalDouble:', totalDouble)
print('totalTwice:', totalTwice)
print('mean:', mean)
print('variance(s^2):', vari)
print('std devi:', vari**(1/2))
print('geometric mean:', totalTwice**(1/i))
print("median = " + str(median))

# data2 = list(data1)
# print(data1.split('\n'))
# print(int(data2))
# print(data2)
# print(sum(data2))
# print(data1)
# print(type(line))


# def mean() :
#     sum(data1)

# print('mean:',sum(data1))












# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
