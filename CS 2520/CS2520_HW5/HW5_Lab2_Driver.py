from HW5_Lab2_Main import *
'''
The polynomial p can be constructed as:
    p = newPolynomial(-10, 0)
    addTerm(p, -1, 1)
    addTerm(p, 9, 7)
    addTerm(p, 5, 10)
'''
def main():
    #creates the polynomial using: new_polynomial(coefficient,power) and add_term(polynomial,coefficient,power)
    p = new_polynomial(-10, 0)
    add_term(p, -1, 1)
    add_term(p, 9, 7)
    add_term(p, 5, 10)
    p.sort(key = lambda x: x[1], reverse=True)

    #outputs the full polynomial p(s) and p(x)*p(x)
    print(f"p(x) = {print_polynomial(p)}")
    print(f"p(x) * p(x) = {print_polynomial(multiply_polynomial(p, p))}")

main()