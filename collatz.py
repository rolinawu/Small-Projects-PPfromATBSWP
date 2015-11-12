## (collatz num)takes number: num.
## if number is even, then collatz() print num//2
## else print 3*num +
## keep going till num = 1

def collatz(num):
	print num
	while (num > 1):
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3 * num + 1
		print num 
	return num

def main():
	entry = int(raw_input("Number?"))
	collatz(entry)


if __name__ == '__main__':
	main()