def generate_numbers():
    return list(range(10))
print("Привет, мир!")

from my_module import generate_numbers  # Предположим, что функция находится в модуле 'my_module'

numbers = generate_numbers()
print(numbers)