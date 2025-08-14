from tabulate import tabulate

print("\n\n--------Инструкция--------")

table_instruction = [
    ["*", "Все сезоны"],
    ["[Номер начало сезона]-[Номер конца сезона]", "К примеру 2-3. Скачаются второй и третий сезон"],
    ["[Номер]", "Или вы можете выбрать просто номер сезона"]
]

print(tabulate(table_instruction, headers=["Тип", "Пояснение к типу"], tablefmt="grid"))