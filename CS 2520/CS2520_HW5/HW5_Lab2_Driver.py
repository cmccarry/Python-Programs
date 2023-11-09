from HW5_Lab2_Main import *

def main():
    p = new_polynomial(-10, 0)
    add_term(p, -1, 1)
    add_term(p, 9, 7)
    add_term(p, 5, 10)
    p.sort(key = lambda x: x[1], reverse=True)
    print(f"p(x) = {print_polynomial(p)}")
    print(f"p(x) * p(x) = {print_polynomial(multiply_polynomial(p, p))}")

main()