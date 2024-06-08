from task import display_user_info


def get_brith_year():
    birth = int(input("Enter your birth year: "))
    return birth


def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    brith_year = get_brith_year()
    display_user_info(name, surname, brith_year)


if __name__ == "__main__":
    main()
