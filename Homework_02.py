"""Try except function homework, assuming non-progresivity for the tax rate"""

try:
    gross_salary = input("What is your gross salary? ")
    number_children = input("How many children do you have? ")
    gross_salary = int(gross_salary)
    number_children = int(number_children)

    initial_tax_rate = 0

    if gross_salary < 1000:
        initial_tax_rate = 0.10
    elif gross_salary < 2000:
        initial_tax_rate = 0.12
    elif gross_salary < 4000:
        initial_tax_rate = 0.14
    else:
        initial_tax_rate = 0.18

    tax_cut = 0

    if gross_salary < 2000:
        tax_cut = tax_cut + number_children * 0.01
    if gross_salary > 2000:
        tax_cut = tax_cut + number_children * 0.005

    intitial_tax_rate = initial_tax_rate - tax_cut

    if initial_tax_rate < 0:
        intitial_tax_rate = 0

    final_net_salary = gross_salary * (1 - initial_tax_rate)

    print("Your net salary based on your inputs is: ", round(final_net_salary, 2))

except ValueError:
    print("The input is invalid, please ensure that al
