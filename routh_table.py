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
	table.append(first_row)
	table.append(second_row)
	dimension_new_row = len(second_row) - 1
	while (dimension_new_row > 0 and is_table_defined(table)):
		new_row = []
		for i in range(dimension_new_row):
			rows_n = len(table)
			matrix = build_matrix(table, i, rows_n)
			element_i = (-1/table[rows_n - 1][0]) * det(matrix)
			new_row.append(element_i)
		table.append(new_row)
		dimension_new_row -= 1		
	return table


def build_matrix(table, index, rows_n):
	matrix = []
	first_row = []
	second_row = []
	a0 = table[rows_n-2][0]
	a1 = table[rows_n-2][index + 1]
	a2 = table[rows_n-1][0]
	a3 = table[rows_n-1][index + 1]
	first_row.extend([a0, a1])
	second_row.extend([a2, a3])
	matrix.extend([first_row, second_row])
	return matrix


def det(matrix):
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	return det
	
	

def is_system_stable(table):
	for row in table:
		if row[0] < 0:
			return False
	return True
	
	
def is_table_defined(table):
	for row in table:
		if row[0] == 0:
			return False
	return True	
	
	


def main():
	print("Routh table generator of P(y) = y^n + ay^(n-1) + by^(n-2) +....+ z")
	print("Type in the coefficients of P(y), from a to z, separated by whitespaces")
	expression = input()
	coefficients_list = expression.split()
	coefficients_list = [int(i) for i in coefficients_list]
	table = build_routh_table(coefficients_list)
	print("The Routh table is:")
	for row in table:
		for element in row:
			print("%.2f" % round(element,2), end = "    ")
		print("")
	if is_table_defined(table):
		if is_system_stable(table):
			print("The system is STABLE")
		else:
			print("The system is NOT STABLE")
	else:
		print("The table is NOT DEFINED")
			

			




if __name__ == "__main__":
	main()

