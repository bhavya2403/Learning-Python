arr = [['march 6', 300], ['march 7', 320], ['march 8', 340], ['march 9', 360]]
# insertion/deletion/search by value === O(n)
# whereas for dictionaries it is order of O(1)

d = {}
for i in arr:
    d[i[0]] = i[1]

print(d)

# this class is already defined in python


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, str):
        h = 0
        for char in str:
            h += ord(char)

        return h % self.MAX  # let''s say we have 10 entries

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


t = HashTable()

t['march 7'] = 320
t['march 6'] = 300
t['march 24'] = 400
t['march 17'] = 380

print(t.arr)

print(t['march 32'])


class Exercise(HashTable):
    def average_temp(self):
        sum = 0
        for i in range(len(self.arr)):
            for element in self.arr[i]:
                if element[0] == 'jan 1' or element[0] == 'jan 2' or element[0] == 'jan 3' or element[0] == 'jan 4' or 'jan 5' == \
                        element[0] or element[0] == 'jan 6' or element[0] == 'jan 7':
                    sum += element[1]

        return int(round(sum / 7))

    def max_temp(self):
        max = 0
        for i in range(len(self.arr)):
            for element in self.arr[i]:
                if element[1] > max:
                    max = element[1]

        return max


t1 = Exercise()
t1['jan 1'] = 27
t1['jan 2'] = 31
t1['jan 3'] = 23
t1['jan 4'] = 34
t1['jan 5'] = 37
t1['jan 6'] = 38
t1['jan 7'] = 29
t1['jan 8'] = 30
t1['jan 9'] = 35
t1['jan 10'] = 30

print(t1.arr)
print(t1.average_temp())
print(t1.max_temp())
print(t1['jan 9'])


class LinearProbing(HashTable):
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        while True:
            try:
                if len(self.arr[h]) == 0:
                    self.arr[h].append((key, value))
                    break
                h += 1
            except:
                h = 0


t2 = LinearProbing()
t2['jan 1'] = 27
t2['jan 2'] = 31
t2['jan 3'] = 23
t2['jan 4'] = 34
t2['jan 5'] = 37
t2['jan 6'] = 38
t2['jan 7'] = 29
t2['jan 8'] = 30
t2['jan 9'] = 35
t2['jan 10'] = 30
print(t2.arr)
