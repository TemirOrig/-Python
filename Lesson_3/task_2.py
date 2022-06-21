def personal_info_record(**kwargs):
    for char, arg in kwargs.items():
        print(f"{char}: {arg}", end="}:) ")


name = input("Введите имя: ").capitalize()
surname = input("Введите фамилию: ").capitalize()
birth_year = input("Введите год рождения: ")
city = input("Введите город проживания: ").capitalize()
mail = input("Введите адрес электронной почты: ")
tel_number = input("Введите номер телефона: ")
personal_info_record(имя=name, фамилия=surname, год=birth_year, город=city, email=mail, номер=tel_number)
