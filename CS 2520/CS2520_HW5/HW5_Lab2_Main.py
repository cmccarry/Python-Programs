'''
Stores a polynomial such as --> p(x) = 5*x^10 + 9*x^7 - x - 10 as a list of terms. 
p(x) gets stored as --> (5,10),(9,7),(-1,1),(-10,0)
The polynomial p can be constructed as:
    p = newPolynomial(-10, 0)
    addTerm(p, -1, 1)
    addTerm(p, 9, 7)
    addTerm(p, 5, 10)
Computes p(x) * p(x)
'''

def new_polynomial(coefficient, power):
    return [(coefficient,power)]

def add_term(polynomial, coefficent, power):
    polynomial.append((coefficent, power))
    #polynomial.sort(key = lambda x: x[1],reverse=True)
    return polynomial

def multiply_polynomial(p1, p2):
    count = 0
    for coeff1, power1 in p1:
        for coeff2, power2 in p2:
            if count == 0:
                newP = new_polynomial(coeff1*coeff2,power1+power2)
                count += 1
            else:
                newP = add_term(newP,coeff1*coeff2,power1+power2)
    for element in newP:
        result = new_polynomial(element[0],element[1])
    for element in newP:
        if element not in result:
            if newP.count(element) > 1:
                newElement = (element[0]*2,element[1])
                if newElement not in result:
                    add_term(result, element[0]*2, element[1])
            else:
                add_term(result, element[0], element[1])
    result.sort(key = lambda x: x[1],reverse=True)
    return result


def print_polynomial(polynomial):
    fullPolynomial = ""
    for coeff, power in polynomial:
        sign = "+" if coeff >= 0 else "-"
        if power == 0:
            fullPolynomial += f" {sign} {abs(coeff)}"
        elif power == 1:
            if coeff == 1:
                fullPolynomial += f" {sign} x"
            else:
                fullPolynomial += f" {sign} {abs(coeff)}x"
        else:
            if coeff == 1:
                fullPolynomial += f" {sign} x^{power}"
            else:
                fullPolynomial += f" {sign} {abs(coeff)}x^{power}" 
    fullPolynomial = fullPolynomial.lstrip(" +")
    return fullPolynomial