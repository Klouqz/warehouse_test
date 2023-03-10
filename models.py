class Warehouse:
    def __init__(self, name, description, address, created_at):
        self.name = name
        self.description = description
        self.address = address
        self.created_at = created_at

class Product:
    def __init__(self, name, description, category, price, supplier, created_at):
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.supplier = supplier
        self.created_at = created_at

