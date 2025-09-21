class Product:
    def __init__(self, id, name, category, price, stock, description, brand, weight, color, rating):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.description = description
        self.brand = brand
        self.weight = weight
        self.color = color
        self.rating = rating


def add_stock(self): pass
def remove_stock(self): pass
def update_price(self): pass
def show_info(self): pass
def apply_discount(self): pass

class Category:
    def __init__(self, id, name, description, parent, created_at, updated_at, image, status, keywords, priority):
        self.id = id
        self.name = name
        self.description = description
        self.parent = parent
        self.created_at = created_at
        self.updated_at = updated_at
        self.image = image
        self.status = status
        self.keywords = keywords
        self.priority = priority


def add_product(self): pass
def remove_product(self): pass
def update_category(self): pass
def get_products(self): pass
def show_info(self): pass

class Customer:
    def __init__(self, id, name, email, phone, address, registration_date, loyalty_points, orders_count, status, password):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.registration_date = registration_date
        self.loyalty_points = loyalty_points
        self.orders_count = orders_count
        self.status = status
        self.password = password


def register(self): pass
def login(self): pass
def make_order(self): pass
def leave_review(self): pass
def update_profile(self): pass

class Order:
    def __init__(self, id, customer, date, status, items, total, discount, payment_method, delivery_address, tracking_number):
        self.id = id
        self.customer = customer
        self.date = date
        self.status = status
        self.items = items
        self.total = total
        self.discount = discount
        self.payment_method = payment_method
        self.delivery_address = delivery_address
        self.tracking_number = tracking_number


def add_item(self): pass
def remove_item(self): pass
def calculate_total(self): pass
def update_status(self): pass
def show_info(self): pass

class Cart:
    def __init__(self, id, customer, items, total, created_at, updated_at, discount, coupon, status, session_id):
        self.id = id
        self.customer = customer
        self.items = items
        self.total = total
        self.created_at = created_at
        self.updated_at = updated_at
        self.discount = discount
        self.coupon = coupon
        self.status = status
        self.session_id = session_id


def add_item(self): pass
def remove_item(self): pass
def clear_cart(self): pass
def calculate_total(self): pass
def apply_coupon(self): pass

class Payment:
def __init__(self, id, order, amount, method, status, date, transaction_id, customer, currency, description):
self.id = id
self.order = order
self.amount = amount
self.method = method
self.status = status
self.date = date
self.transaction_id = transaction_id
self.customer = customer
self.currency = currency
self.description = description


def process(self): pass
def refund(self): pass
def check_status(self): pass
def generate_receipt(self): pass
def show_info(self): pass

class Delivery:
def __init__(self, id, order, address, city, postal_code, country, status, courier, estimated_date, cost):
self.id = id
self.order = order
self.address = address
self.city = city
self.postal_code = postal_code
self.country = country
self.status = status
self.courier = courier
self.estimated_date = estimated_date
self.cost = cost


def update_status(self): pass
def calculate_cost(self): pass
def assign_courier(self): pass
def track_delivery(self): pass
def show_info(self): pass

class Supplier:
def __init__(self, id, name, contact, email, phone, address, products, rating, contract_date, status):
self.id = id
self.name = name
self.contact = contact
self.email = email
self.phone = phone
self.address = address
self.products = products
self.rating = rating
self.contract_date = contract_date
self.status = status


def add_product(self): pass
def remove_product(self): pass
def update_info(self): pass
def show_products(self): pass
def terminate_contract(self): pass

class Invoice:
def __init__(self, id, order, date, total, tax, customer, items, due_date, status, payment_status):
self.id = id
self.order = order
self.date = date
self.total = total
self.tax = tax
self.customer = customer
self.items = items
self.due_date = due_date
self.status = status
self.payment_status = payment_status


def generate(self): pass
def send(self): pass
def update_status(self): pass
def calculate_total(self): pass
def show_info(self): pass

class Review:
def __init__(self, id, product, customer, rating, comment, date, status, likes, dislikes, reply):
self.id = id
self.product = product
self.customer = customer
self.rating = rating
self.comment = comment
self.date = date
self.status = status
self.likes = likes
self.dislikes = dislikes
self.reply = reply


def add_like(self): pass
def add_dislike(self): pass
def edit(self): pass
def delete(self): pass
def show_info(self): pass

class Discount:
def __init__(self, id, code, percentage, start_date, end_date, status, min_order, max_uses, used_count, description):
self.id = id
self.code = code
self.percentage = percentage
self.start_date = start_date
self.end_date = end_date
self.status = status
self.min_order = min_order
self.max_uses = max_uses
self.used_count = used_count
self.description = description


def apply(self): pass
def deactivate(self): pass
def check_validity(self): pass
def update(self): pass
def show_info(self): pass

class Warehouse:
def __init__(self, id, name, location, capacity, stock, manager, contact, status, created_at, updated_at):
self.id = id
self.name = name
self.location = location
self.capacity = capacity
self.stock = stock
self.manager = manager
self.contact = contact
self.status = status
self.created_at = created_at
self.updated_at = updated_at


def add_stock(self): pass
def remove_stock(self): pass
def check_capacity(self): pass
def show_info(self): pass
def transfer_stock(self): pass

class Employee:
def __init__(self, id, name, email, phone, role, department, hire_date, salary, status, manager):
self.id = id
self.name = name
self.email = email
self.phone = phone
self.role = role
self.department = department
self.hire_date = hire_date
self.salary = salary
self.status = status
self.manager = manager


def assign_task(self): pass
def update_info(self): pass
def promote(self): pass
def terminate(self): pass
def show_info(self): pass

class Return:
def __init__(self, id, order, product, reason, status, date, customer, refund_amount, method, comment):
self.id = id
self.order = order
self.product = product
self.reason = reason
self.status = status
self.date = date
self.customer = customer
self.refund_amount = refund_amount
self.method = method
self.comment = comment


def request(self): pass
def approve(self): pass
def reject(self): pass
def refund(self): pass
def show_info(self): pass

class LoyaltyProgram:
def __init__(self, id, customer, points, level, discount, start_date, end_date, status, rewards, history):
self.id = id
self.customer = customer
self.points = points
self.level = level
self.discount = discount
self.start_date = start_date
self.end_date = end_date
self.status = status
self.rewards = rewards
self.history = history


def add_points(self): pass
def redeem_points(self): pass
def upgrade_level(self): pass
def deactivate(self): pass
def show_info(self): pass





