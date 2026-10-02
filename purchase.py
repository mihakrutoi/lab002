price = int(input("Цена в рублях: "))
count = int(input("Количество: "))
paid = int(input("Переданная сумма: "))

total_price = price * count
change = paid - total_price
print(f"Стоимость {total_price} сдача {change}")