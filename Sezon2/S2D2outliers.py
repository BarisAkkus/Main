data = [4,5,104,105,110,120,130,130,150,
        160,170,183,185,187,188,191,350,360]

# del data [0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# for index,value in enumerate(data):
#     if ( value < min_valid) or (value > max_valid):
#         del data[index]
# print(data) --- not safe çalışmadı 

#düşük değerler için
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

#yüksek değerler icin
start=0
for index in range(len(data) - 1,-1,-1):
    if data [index] <= max_valid:
        #We have the index of the last item to keep
        #Set 'start' to the position of the first
        #item to delete, which is 1 after 'index'.
        start = index + 1
        break
print(start)    
del data[start:]
print(data)