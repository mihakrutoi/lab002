total_seconds = int(input("Всего секунд: "))
remaining_hours = total_seconds // 3600
remaining_minutes = (total_seconds - (remaining_hours * 3600)) // 60
remaining_seconds = total_seconds - (remaining_hours * 3600) - (remaining_minutes * 60)
print(f"{remaining_hours} ч {remaining_minutes} мин {remaining_seconds} с")