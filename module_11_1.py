import requests
import matplotlib.pyplot as plt

#Использования requests для запроса данных с сайта и вывода их в консоль
response = requests.get('https://www.google.com')
print(response.text)

#Использованиt matplotlib для визуализации данных
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График функции')
plt.show()

