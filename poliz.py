def main():
	print('Введите выражение: ')
	string = input()

	ans = ''
	steck = []

	for word in string:
		if word == ' ':
			continue
		else:
			if (word >= '0' and word <= '9') or (word >= 'a' and word <='z') or (word >= 'A' and word <= 'A') or (word >= 'а' and word <='я') or (word >= 'А' and word <='Я'):
				ans += word
			elif word == '(':
				steck.append(word)
			elif word == ')':
				if len(steck):
					while steck[-1] != '(':
						ans += steck.pop()
						if not(len(steck)):
							print('В выражении было введено неверное количество скобок...')
							return 0
					steck.pop()
			elif word == '^':
				if len(steck):
					while steck[-1] == '^':
						ans += steck.pop()
				steck.append(word)
			elif word == '+' or word == '-':
				if len(steck):
					while steck[-1] == '*' or steck[-1] == '/' or steck[-1] == '+' or steck[-1] == '-':
						ans += steck.pop()
				steck.append(word)
			elif word == '*' or word == '/':
				if len(steck):
					while steck[-1] == '*' or steck[-1] == '/':
						ans += steck.pop()
				steck.append(word)
			else:
				print('Неизвестная операция ' + word)
				return 0
	while len(steck):
		if steck[-1] != '(':
			ans += steck.pop()
		else:
			print('В выражении было введено неверное количество скобок...')
			return 0
	print(ans)


if __name__ == '__main__':
	main()



