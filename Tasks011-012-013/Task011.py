
class Homework:
    global glob_change

    def first_homework_metod(self, change_2: int = 5, change_3: int = 5) -> None:
        # enclosing
        encl_change: int = 10

        def first_homework_metod_in_menod() -> None:
            # local
            loc_change: int = 12
            print(f'sum = {glob_change + encl_change + loc_change}')

        first_homework_metod_in_menod()
        print(f'var2 + var3 = {change_2 + change_3}')


# global
glob_change: int = 1
sc = Homework()
sc.first_homework_metod()