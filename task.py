def display_user_info(name, surname, birth_year):
    def age(birth_year):
        current_year = 2024
        age = current_year - birth_year
        return age

    print(f"\nName: {name.title()}")
    print(f"Surname: {surname.title()}")
    print(f"Born year: {birth_year}")
    print(f"Age: {age(birth_year)}")


if __name__ == "__main__":
    print("if you wanna run this code, you have to move main.py !!!")
