import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, norm

# Заданные параметры для 6-го варианта
N = 1000
a, b = 1, 11       # Параметры равномерного распределения
lambda_param = 1   # Параметр экспоненциального распределения
mu, sigma = 0, 6   # Параметры нормального распределения

# Генерация выборок
uniform_sample = np.random.uniform(a, b, N)
exponential_sample = np.random.exponential(1 / lambda_param, N)
normal_sample = np.random.normal(mu, sigma, N)

# Функция для вычисления математического ожидания и дисперсии
def calculate_stats(sample):
    mean = np.mean(sample)
    variance = np.var(sample)
    return mean, variance

# Объемы выборок для оценки
sample_sizes = [10, 20, 50, 100, 1000]
uniform_stats = []
exponential_stats = []
normal_stats = []

for size in sample_sizes:
    uniform_stats.append(calculate_stats(uniform_sample[:size]))
    exponential_stats.append(calculate_stats(exponential_sample[:size]))
    normal_stats.append(calculate_stats(normal_sample[:size]))

# Построение графиков зависимости оценок от объема выборки
def plot_stats(sample_sizes, stats, title, param_mean, param_var):
    means = [s[0] for s in stats]
    variances = [s[1] for s in stats]
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sample_sizes, means, marker='o', label="Оценка мат. ожидания")
    plt.axhline(y=param_mean, color='r', linestyle='--', label="Теоретическое значение")
    plt.xlabel("Объем выборки")
    plt.ylabel("Математическое ожидание")
    plt.title(f"{title} - Математическое ожидание")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(sample_sizes, variances, marker='o', label="Оценка дисперсии")
    plt.axhline(y=param_var, color='r', linestyle='--', label="Теоретическое значение")
    plt.xlabel("Объем выборки")
    plt.ylabel("Дисперсия")
    plt.title(f"{title} - Дисперсия")
    plt.legend()
    plt.show()

# Построение графиков для каждого распределения
plot_stats(sample_sizes, uniform_stats, "Равномерное распределение", (a + b) / 2, ((b - a) ** 2) / 12)
plot_stats(sample_sizes, exponential_stats, "Экспоненциальное распределение", 1 / lambda_param, 1 / (lambda_param ** 2))
plot_stats(sample_sizes, normal_stats, "Нормальное распределение", mu, sigma ** 2)

# Построение гистограмм и теоретических функций плотности
def plot_histogram_and_theoretical(sample, theoretical_dist, params, title, bins=11):
    plt.hist(sample, bins=bins, density=True, alpha=0.5, color='g', label='Гистограмма')
    x = np.linspace(min(sample), max(sample), 1000)
    plt.plot(x, theoretical_dist.pdf(x, *params), 'r--', label='Теоретическая функция')
    plt.xlabel("Значения")
    plt.ylabel("Плотность вероятности")
    plt.title(title)
    plt.legend()
    plt.show()

# Гистограммы для каждого распределения
plot_histogram_and_theoretical(uniform_sample, uniform, (a, b - a), "Равномерное распределение")  # Используем uniform
plot_histogram_and_theoretical(exponential_sample, expon, (0, 1 / lambda_param), "Экспоненциальное распределение")
plot_histogram_and_theoretical(normal_sample, norm, (mu, sigma), "Нормальное распределение")
