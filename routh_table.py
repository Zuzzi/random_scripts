# Routh stability criterion



def get_first_exponent(expression):
	exponent = ""
	found_exp = False
	for char in expression:
		if char.isdigit() or char == "-":
			exponent += char
			found_exp = True
		elif found_exp:
			break
	return int(exponent)



def get_coefficients (expression):
	# find the first exponent (dimension of the polynomial)
	dimension = get_first_exponent(expression)
	print("Dimension = ", dimension)
	# find the coefficients
	for index, char in enumerate(expression):
		if char == "+" or char == "-": # coefficient spot starts here!
			exponent = get_first_exponent(expression[index + 1:])
			print("Exponent = ", exponent)
			
			

	
	
			
			
			
	
	









def main():
    print("Routh table generator")
    print("Type in the polynomial P(y) = y^n + ay^(n-1) + by^(n-2) +....+ z")
    expression = input()
    #coefficients_list = get_coefficients(expression)
    get_coefficients(expression)
    



















if __name__ == "__main__":
    main()

