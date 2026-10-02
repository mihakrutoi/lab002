total = int(input("Введите количество единиц: "))
capacity = int(input("Введите количество в одной упаковке: "))

full = total // capacity
remain = total % capacity
packs = (total + capacity - 1) // capacity

print(f"Полных: {full}, остаток: {remain}, всего: {packs}")