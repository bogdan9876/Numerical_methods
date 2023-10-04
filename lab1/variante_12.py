import numpy as np

numbers = np.array([[8.3, 2.86, 4.1, 1.9],
                    [3.92, 8.45, 7.54, 2.46],
                    [2.21, 3.41, 1.69, 6.69]])

# Отримання розмірності вхідної матриці
n, m = numbers.shape

# Створення "розширеної" матриці, додаючи до матриці `numbers` одиничну матрицю справа
augmented_matrix = np.hstack((numbers, np.identity(n)))

# Початок виконання методу Гауса з вибором головного елемента по всій матриці

# Цикл по рядках матриці
for i in range(n):
    # Знаходження найбільшого за модулем елемента у підматриці
    pivot_row, pivot_col = np.unravel_index(np.argmax(np.abs(augmented_matrix[i:, i:])), (n - i, n - i))
    
    # Збільшення індексів на `i` для відображення реальних позицій у великій матриці
    pivot_row += i
    pivot_col += i

    # Обмін рядків та стовпців, щоб півотальний елемент опинився на діагоналі
    augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]
    augmented_matrix[:, [i, pivot_col]] = augmented_matrix[:, [pivot_col, i]]
    
    # Нормалізація поточного рядка, робимо півотальний елемент рівним 1
    augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]

    # Виконання операцій над іншими рядками, щоб зробити всі інші елементи у стовпці рівними нулю
    for j in range(n):
        if j != i:
            augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]

# Отримання оберненої матриці з правої частини "розширеної" матриці
inverse_matrix = augmented_matrix[:, n:]

print("Inverse Matrix:")
print(inverse_matrix)

# Перевірка, чи є обернена матриця правильною інверсією вихідної матриці
# Множимо вихідну матрицю на обернену і порівнюємо з одиничною матрицею
identity_matrix = np.dot(numbers, inverse_matrix.T)  # Transpose the inverse_matrix

# Порівнюємо кожен елемент identity_matrix з відповідним елементом одиничної матриці
is_identity = np.allclose(identity_matrix, np.identity(n))

if is_identity:
    print("The inverse matrix is correct.")
else:
    print("The inverse matrix is incorrect.")