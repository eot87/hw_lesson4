# Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

def printer(my_func):
    print(my_func.__name__, my_func.__code__.co_varnames)


def open_browser(arg0):
    pass


def go_to_companyname_homepage(arg1):
    pass


def find_registration_button_on_login_page(arg2):
    pass


def main():
    iteration_object = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
    for my_func in iteration_object:
        printer(my_func)


if __name__ == "__main__":
    main()
