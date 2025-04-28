import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)

def cyclic123_array(n):
    """2. Генерирует numpy массив длины 3n, заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1,2,3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    arr = np.zeros((n,n), dtype=int)
    arr[0,:] = 1
    arr[-1,:] = 1
    arr[:,0] = 1
    arr[:,-1] = 1
    return arr

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    m = np.zeros((n, n))
    m[::2, ::2] = 1
    m[1::2, 1::2] = 1
    return m

def matrix_with_sum_index(n):
    """6. Создаёт n x n матрицу с (i,j)-элементами равным i+j."""
    i = np.arange(n).reshape(-1, 1)
    j = np.arange(n).reshape(1, -1)
    return i + j

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    cosx = np.cos(np.arange(a, b, dx))
    sinx = np.sin(np.arange(a, b, dx))
    return np.array([cosx, sinx])

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    return np.mean(A), np.sum(A, axis=0), np.sum(A, axis=1)

def sort_array_by_column(A, j):
    """9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[A[:, j].argsort()]

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a,b] с шагом dx 3-я методами: прямоугольника, трапеций и Симпсона."""
    x = np.arange(a, b+dx, dx)
    y = f(x)
    
    if method == 'rectangular':
        # метод прямоугольника (левая точка)
        return np.sum(y[:-1]) * dx
    elif method == 'trapezoidal':
        # метод трапеций
        return (dx/2) * np.sum(y[:-1] + y[1:])
    elif method == 'simpson':
        # метод Симпсона - n должно быть четным
        n = len(x) - 1
        if n % 2 == 1:
            n -= 1  # убираем последний, если нечётный
        h = dx
        I = y[0] + y[n]
        I += 4 * np.sum(y[1:n:2])
        I += 2 * np.sum(y[2:n-1:2])
        return (h/3) * I
    else:
        raise ValueError("Метод должен быть 'rectangular', 'trapezoidal' или 'simpson'")
