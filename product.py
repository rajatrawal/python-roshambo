class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.discount = 0

  def __str__(self):
    return f'{self.name}: ${self.price}'


class Sneaker(Product):
  def __init__(self, name, price, show_size, brand)
    super().__init__(name, price)
    self.shoe_size = shoe_size
    self.brand = brand

nike_free = Sneaker("Nike Free", "100", "10", "Nike")

print(nike_free.price)
print(nike_free.discount)

class SoccerBall(Product):
  def __init__(self, name, price, material):
    super().__init__(name, price)
    self.material = material

soccer1 = Soccerball("Wilsone", "20", "Rubber")

print(soccer1.price)
print(soccer1.discount)