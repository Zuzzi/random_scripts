# Routh stability criterion

def build_routh_table(coefficients_list):
	table = []
	first_row = []
	second_row = []
	first_row.append(1)
	for index, c in enumerate(coefficients_list):
		if index % 2 == 0:
			second_row.append(c)
		else:
			first_row.append(c)
	print(first_row)
	print(second_row)
	table.append(first_row)
	table.append(second_row)
	dimension_new_row = len(second_row) - 1
	third_row = []
	for i in range(dimension_new_row):
		matrix = build_matrix(table, i)
		print(matrix)
		print(det(matrix))
		element_i = (-1/table[1][0]) * det(matrix)
		third_row.append(element_i)
	table.append(third_row)
	return table


def build_matrix(table, index):
	matrix = []
	first_row = []
	second_row = []
	a0 = table[0][0]
	a1 = table[0][index + 1]
	a2 = table[1][0]
	a3 = table[1][index + 1]
	first_row.extend([a0, a1])
	second_row.extend([a2, a3])
	matrix.extend([first_row, second_row])
	return matrix


def det(matrix):
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	return det


def main():
	print("Routh table generator of P(y) = y^n + ay^(n-1) + by^(n-2) +....+ z")
	print("Type in the coefficients of P(y), from z to a, separated by whitespace")
	expression = input()
	coefficients_list = expression.split()
	coefficients_list = [int(i) for i in coefficients_list]
	print(coefficients_list)
	table = build_routh_table(coefficients_list)
	print("The final table is:")
	print(table)

			




if __name__ == "__main__":
	main()

