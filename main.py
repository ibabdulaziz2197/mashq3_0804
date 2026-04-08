# 1
a = [1, 2, 3, 4]
roy = list(map(lambda el: el ** 2, a))
print(roy)

# 2
a = ["salom", "dunyo"]
roy = list(map(lambda x: x.upper(), a))
print(roy)

# 3
roy = ['apple', 'banana', 'chery']
a = list(map(lambda el: el.upper(), roy))
print(a)

# 4
roy = ['salom', 'dunyo', 'python']
a = list(map(lambda el: len(roy), roy))
print(a)

# 5
roy = [3, 6, 9, 12]
a = list(map(lambda el: el ** 2, roy))
print(a)

# 6
roy = ["Ali", "Vali", "Hasan"]

a = list(map(lambda el: "Mr. " + el, roy))

print(a)

# 7
roy = [100, 200, 300]

a = list(map(str, roy))

print(a)

# 8
roy = ["1", "2", "3", "4"]

a = list(map(int, roy))

print(a)

# 9
roy = [5, 10, 15, 20]

a = list(map(lambda x: x / 3, roy))

print(a)

# 10
roy = ["hello", "world"]

a = list(map(lambda el: '!' + el, roy))

print(a)
