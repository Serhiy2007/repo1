# clothing_store.py

class ClothingItem:
    def __init__(self, name, size, color, price, brand, gender, material, style, stock, season):
        self.name = name
        self.size = size
        self.color = color
        self.price = price
        self.brand = brand
        self.gender = gender
        self.material = material
        self.style = style
        self.stock = stock
        self.season = season

    def add_stock(self, quantity):
        self.stock += quantity
        print(f"{quantity} одиниць додано до {self.name}. Загальний склад: {self.stock}")

    def sell_item(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity} одиниць {self.name} продано. Залишилось: {self.stock}")
        else:
            print(f"Недостатньо товару {self.name} на складі.")

    def change_price(self, new_price):
        self.price = new_price
        print(f"Ціна на {self.name} змінена на {self.price} грн")

    def display_info(self):
        print(f"\n📦 Назва: {self.name}, Розмір: {self.size}, Колір: {self.color}, Ціна: {self.price} грн")
        print(f"🏷️ Бренд: {self.brand}, Стать: {self.gender}, Матеріал: {self.material}, Стиль: {self.style}")
        print(f"📦 На складі: {self.stock}, Сезон: {self.season}")

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount
        print(f"Знижка {percent}% застосована до {self.name}. Нова ціна: {self.price} грн")


# Людина 1 — Верхній одяг
class TShirt(ClothingItem):
    def is_sport_style(self):
        return self.style.lower() == "спорт"

class Hoodie(ClothingItem):
    def has_hood(self):
        return True

class Sweater(ClothingItem):
    def is_winter_ready(self):
        return self.material.lower() in ["вовна", "фліс"]

class Jacket(ClothingItem):
    def weather_type(self):
        return "Холодна погода"

class Coat(ClothingItem):
    def is_long(self):
        return True


# Людина 2 — Нижній одяг
class Jeans(ClothingItem):
    def is_denim(self):
        return self.material.lower() == "денім"

class Shorts(ClothingItem):
    def is_summer_item(self):
        return self.season.lower() == "літо"

class Skirt(ClothingItem):
    def is_formal(self):
        return self.style.lower() == "офіційний"

class Suit(ClothingItem):
    def get_total_price(self, shirt_price):
        return self.price + shirt_price

class Tracksuit(ClothingItem):
    def is_unisex(self):
        return self.gender.lower() == "унісекс"


# Людина 3 — Аксесуари, взуття, інше
class Dress(ClothingItem):
    def is_evening_dress(self):
        return self.style.lower() == "вечірній"

class Blouse(ClothingItem):
    def is_office_ready(self):
        return self.style.lower() == "офісний"

class Socks(ClothingItem):
    def pack_of_pairs(self, pairs):
        return f"Упаковано {pairs} пар носків"

class Hat(ClothingItem):
    def is_winter_hat(self):
        return self.season.lower() == "зима"

class Shoes(ClothingItem):
    def shoe_type(self):
        if self.style.lower() == "спортивний":
            return "Кросівки"
        elif self.style.lower() == "офіційний":
            return "Туфлі"
        else:
            return "Інше"


# Приклад використання
if __name__ == "__main__":
    jacket = Jacket("Куртка зимова", "L", "Синя", 1500, "Adidas", "Чоловіча", "Поліестер", "Кежуал", 12, "Зима")
    jeans = Jeans("Джинси класичні", "M", "Сині", 900, "Levis", "Унісекс", "Денім", "Офіційний", 20, "Осінь")
    hat = Hat("Шапка в'язана", "Універсальний", "Сіра", 250, "H&M", "Унісекс", "Акрил", "Кежуал", 30, "Зима")

    for item in [jacket, jeans, hat]:
        item.display_info()
        item.add_stock(5)
        item.sell_item(3)
        item.apply_discount(10)
        print()
