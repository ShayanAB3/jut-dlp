from tabulate import tabulate

class SelectSeason:
    def show_table(anime_name:str, table:list[list[int,str]]) -> str:
        print(f"\n--------{anime_name}--------")

        print(tabulate(table, headers=["Номер", "Название сезона"], tablefmt="grid"))

        season = input("Какой сезон вы хотите скачать?: ")
        return season