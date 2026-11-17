import pandas as pd
import matplotlib.pyplot as plt

# Пример: конверсия воронки
funnel = pd.DataFrame({
    'Этап': ['Просмотр', 'Корзина', 'Покупка'], 'Пользователи': [1000, 300, 150]
})

print("Конверсия воронки:")
print(funnel)

# Визуализация
plt.figure(figsize=(8, 5))
plt.bar(funnel['Этап'], funnel['Пользователи'], color='skyblue')
plt.title('Воронка конверсии')
plt.ylabel('Количество пользователей')
plt.tight_layout()
plt.savefig('funnel.png')
print("\nГрафик сохранён: funnel.png")
