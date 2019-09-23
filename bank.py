def bank(a, year):
	a = (a + ((a * 0.1)* year))
	print("итого в банке", a)
a = int(input("сумма в банк "))
year = int(input("на сколько лет "))
ba = bank(a, year)
ba