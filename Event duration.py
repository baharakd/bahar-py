import math

data = [50.3, 338.4, 626.5, 959.4, 1317.9,
        1716.7, 2134.3, 2565.5, 3085.6,3626.7]
new_item = 0
duration = []
for i in range(len(data)-1) :
    new_item = round(data[i+1]- data[i] , 2)
    duration.append(new_item)
print(duration)