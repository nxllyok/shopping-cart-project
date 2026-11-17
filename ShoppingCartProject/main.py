class Product:
    def __init__(self, product_id, name, category, price, weight, description):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight
        self.description = description

    def show_info(self):
        print(
            f"ID: {self.product_id} | "
            f"Название: {self.name} | "
            f"Категория: {self.category} | "
            f"Цена: {self.price} руб. | "
            f"Вес: {self.weight} кг | "
            f"Описание: {self.description}"
        )


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Товар успешно добавлен в каталог.")

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def edit_product(self, product_id, name, category, price, weight, description):
        product = self.find_product(product_id)

        if product is None:
            print("Товар не найден.")
            return

        product.name = name
        product.category = category
        product.price = price
        product.weight = weight
        product.description = description

        print("Информация о товаре обновлена.")

    def delete_product(self, product_id):
        product = self.find_product(product_id)

        if product is None:
            print("Товар не найден.")
            return

        self.products.remove(product)
        print("Товар удалён из каталога.")

    def show_products(self):
        if not self.products:
            print("Каталог пуст.")
            return

        print("\n--- КАТАЛОГ ТОВАРОВ ---")
        for product in self.products:
            product.show_info()


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product is None:
            print("Товар не найден.")
            return

        self.items.append(product)
        print(f"Товар '{product.name}' добавлен в корзину.")

    def remove_product(self, product_id):
        for product in self.items:
            if product.product_id == product_id:
                self.items.remove(product)
                print(f"Товар '{product.name}' удалён из корзины.")
                return

        print("Такого товара нет в корзине.")

    def show_cart(self):
        if not self.items:
            print("Корзина пуста.")
            return

        print("\n--- ВАША КОРЗИНА ---")

        for product in self.items:
            product.show_info()

        print("Общий вес:", round(self.get_total_weight(), 2), "кг")
        print("Общая стоимость:", round(self.get_total_price(), 2), "руб.")

    def get_total_price(self):
        return sum(product.price for product in self.items)

    def get_total_weight(self):
        return sum(product.weight for product in self.items)

    def apply_discount(self, discount):
        if discount < 0 or discount > 100:
            print("Скидка должна быть от 0 до 100 процентов.")
            return

        total = self.get_total_price()
        discounted_total = total * (1 - discount / 100)

        print(f"Стоимость до скидки: {total:.2f} руб.")
        print(f"Скидка: {discount}%")
        print(f"Стоимость после скидки: {discounted_total:.2f} руб.")


def bubble_sort(items, key, reverse=False):
    result = items[:]
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            first = key(result[j])
            second = key(result[j + 1])

            if (first > second and not reverse) or \
               (first < second and reverse):
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def insertion_sort(items, key, reverse=False):
    result = items[:]

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0:
            if (key(result[j]) > key(current) and not reverse) or \
               (key(result[j]) < key(current) and reverse):
                result[j + 1] = result[j]
                j -= 1
            else:
                break

        result[j + 1] = current

    return result


def quick_sort(items, key, reverse=False):
    if len(items) <= 1:
        return items[:]

    pivot = items[len(items) // 2]

    if not reverse:
        smaller = [x for x in items if key(x) < key(pivot)]
        equal = [x for x in items if key(x) == key(pivot)]
        larger = [x for x in items if key(x) > key(pivot)]
    else:
        smaller = [x for x in items if key(x) > key(pivot)]
        equal = [x for x in items if key(x) == key(pivot)]
        larger = [x for x in items if key(x) < key(pivot)]

    return (
        quick_sort(smaller, key, reverse)
        + equal
        + quick_sort(larger, key, reverse)
    )


def merge_sort(items, key, reverse=False):
    if len(items) <= 1:
        return items[:]

    middle = len(items) // 2

    left = merge_sort(items[:middle], key, reverse)
    right = merge_sort(items[middle:], key, reverse)

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if (key(left[i]) <= key(right[j]) and not reverse) or \
           (key(left[i]) >= key(right[j]) and reverse):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort_cart(cart, algorithm, criterion, reverse=False):
    sort_functions = {
        "1": bubble_sort,
        "2": insertion_sort,
        "3": quick_sort,
        "4": merge_sort
    }

    sort_keys = {
        "1": lambda product: product.price,
        "2": lambda product: product.weight,
        "3": lambda product: product.category.lower()
    }

    if algorithm not in sort_functions:
        print("Неверный алгоритм сортировки.")
        return

    if criterion not in sort_keys:
        print("Неверный критерий сортировки.")
        return

    key = sort_keys[criterion]
    sorting_function = sort_functions[algorithm]

    cart.items = sorting_function(cart.items, key, reverse)

    print("\nКорзина успешно отсортирована!")
    cart.show_cart()

catalog = ProductCatalog()
cart = Cart()

catalog.add_product(Product(1, "Ноутбук", "Электроника", 65000, 2.1, "Портативный компьютер"))
catalog.add_product(Product(2, "Наушники", "Электроника", 3500, 0.3, "Беспроводные наушники"))
catalog.add_product(Product(3, "Книга", "Книги", 800, 0.5, "Учебная книга"))
catalog.add_product(Product(4, "Рюкзак", "Аксессуары", 2500, 0.9, "Городской рюкзак"))
catalog.add_product(Product(5, "Мышь", "Электроника", 1200, 0.2, "Компьютерная мышь"))


def show_menu():
    print("\n========== ВИРТУАЛЬНЫЙ МАГАЗИН ==========")
    print("1. Показать каталог товаров")
    print("2. Добавить товар в каталог")
    print("3. Редактировать товар")
    print("4. Удалить товар из каталога")
    print("5. Добавить товар в корзину")
    print("6. Удалить товар из корзины")
    print("7. Показать корзину")
    print("8. Сортировать корзину")
    print("9. Подсчитать итоговую стоимость")
    print("10. Применить скидку")
    print("0. Выход")
    print("=========================================")


while True:
    show_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        catalog.show_products()

    elif choice == "2":
        try:
            product_id = int(input("Введите ID товара: "))
            name = input("Введите название: ")
            category = input("Введите категорию: ")
            price = float(input("Введите цену: "))
            weight = float(input("Введите вес: "))
            description = input("Введите описание: ")

            if price < 0 or weight < 0:
                print("Цена и вес не могут быть отрицательными.")
            elif catalog.find_product(product_id) is not None:
                print("Товар с таким ID уже существует.")
            else:
                catalog.add_product(
                    Product(product_id, name, category, price, weight, description)
                )
        except ValueError:
            print("Ошибка: введите корректные числовые значения.")

    elif choice == "3":
        try:
            product_id = int(input("Введите ID товара для редактирования: "))
            name = input("Новое название: ")
            category = input("Новая категория: ")
            price = float(input("Новая цена: "))
            weight = float(input("Новый вес: "))
            description = input("Новое описание: ")

            if price < 0 or weight < 0:
                print("Цена и вес не могут быть отрицательными.")
            else:
                catalog.edit_product(
                    product_id, name, category, price, weight, description
                )
        except ValueError:
            print("Ошибка: введите корректные числовые значения.")

    elif choice == "4":
        try:
            product_id = int(input("Введите ID товара для удаления: "))
            catalog.delete_product(product_id)
        except ValueError:
            print("ID должен быть числом.")

    elif choice == "5":
        try:
            product_id = int(input("Введите ID товара: "))
            product = catalog.find_product(product_id)
            cart.add_product(product)
        except ValueError:
            print("ID должен быть числом.")

    elif choice == "6":
        try:
            product_id = int(input("Введите ID товара для удаления из корзины: "))
            cart.remove_product(product_id)
        except ValueError:
            print("ID должен быть числом.")

    elif choice == "7":
        cart.show_cart()

    elif choice == "8":
        if not cart.items:
            print("Корзина пуста. Сначала добавьте товары.")
            continue

        print("\nВыберите алгоритм сортировки:")
        print("1. Bubble Sort — пузырьковая сортировка")
        print("2. Insertion Sort — сортировка вставками")
        print("3. Quick Sort — быстрая сортировка")
        print("4. Merge Sort — сортировка слиянием")

        algorithm = input("Ваш выбор: ")

        print("\nВыберите критерий:")
        print("1. Цена")
        print("2. Вес")
        print("3. Категория")

        criterion = input("Ваш выбор: ")

        print("\nВыберите порядок:")
        print("1. По возрастанию")
        print("2. По убыванию")

        order = input("Ваш выбор: ")

        if order not in ("1", "2"):
            print("Неверный порядок сортировки.")
        else:
            sort_cart(
                cart,
                algorithm,
                criterion,
                reverse=(order == "2")
            )

    elif choice == "9":
        print(
            "Итоговая стоимость:",
            f"{cart.get_total_price():.2f} руб."
        )

    elif choice == "10":
        try:
            discount = float(input("Введите размер скидки в процентах: "))
            cart.apply_discount(discount)
        except ValueError:
            print("Введите число.")

    elif choice == "0":
        print("Спасибо за использование виртуального магазина!")
        break

    else:
        print("Неверная команда. Попробуйте ещё раз.")