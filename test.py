def greet():
	name = input("Enter your name: ")
	print(f"Hello, {name}!")


def add_two_numbers():
	try:
		a = float(input("First number: "))
		b = float(input("Second number: "))
		print(f"Sum: {a + b}")
	except ValueError:
		print("Invalid number entered.")


def main():
	print("Simple Python demo")
	print("1) Greet")
	print("2) Add two numbers")
	choice = input("Choose an option (1/2): ")
	if choice == "1":
		greet()
	elif choice == "2":
		add_two_numbers()
	else:
		print("Goodbye")


if __name__ == "__main__":
	main()

