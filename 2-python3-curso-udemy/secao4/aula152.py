"""
- Se quisermos fazer algo quando algum erro específico acontecer, 
usa o try except com a exceção específica!

- Quebrar funções: Uma função não deveria ter mais de uma responsabilidade, 
como dividir número e verificar se o divisor é zero
"""

def is_zero(input):
    if input == 0:
        raise ZeroDivisionError('Is not possible to divide by zero')
    
def is_int_or_float(input):
    input_type = type(input)
    if not isinstance(input, (int, float)):
        raise TypeError(
            'Inputs must be int or float\n'
            f'{input_type.__name__} sent!'
        )

def divide(n, d):
    is_zero(d)
    
    is_int_or_float(n)
    is_int_or_float(d)

    return n / d
    

print(divide(8,'2'))