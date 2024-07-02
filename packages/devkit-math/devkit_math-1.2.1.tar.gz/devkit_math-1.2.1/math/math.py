def gcd(x, y):
    if type(x) != type(int()) or type(y) != type(int()):
        return 0
    return gcd(y, x % y) if y else x
def lcm(x, y):
    if type(x) != type(int()) or type(y) != type(int()):
        return 0
    return x * y / gcd(x, y)
def prime(x):
    if type(x) != type(int()):
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1
def prime_generator():
	i = 1
	while True:
		i += 1
		j = 2
		while j <= i / j:
			if i % j == 0:
				break
			j += 1
		else:
			yield i
