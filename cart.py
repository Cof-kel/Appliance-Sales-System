class Cart:
    def __init__(self):
        self.items = []

    def add(self, product_name, quantity, total):
        self.items.append((product_name, quantity, total))

    def get_total(self):
        return sum(item[2] for item in self.items)

    def clear(self):
        self.items = []
