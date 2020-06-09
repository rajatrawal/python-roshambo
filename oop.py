# Spec: write a program that holds product and department information about a store. User should be able to enter a department number and get a list of products in that department.

# Product info it:
# * quantity, int
# * price
# * dept
# * name, string

# You will get a product list later

# Department info: 
# * number, int
# * name, string

# Questions:

# How many products? Under 1,000,000
# How to present the data? Standard output.
# How many customer? Under 100 requests per second.

class Store:
  def __init__(self, name, depts): # Constructor
    self.name = name # "has-a" relationship
    self.depts = depts

  def __str__(self):
    s = f"Store: {self.name}\nDepartments:\n"

    for d in self.depts:
      s += f"     {d.name} {d.num}\n"

    return s

  def __repr__(self):
    return f'Store({repr(self.name)}. {repr(self.depts)})'
  
  def find_dept(self, dept_num):
    for d in self.depts:
      if d.num == dept_num:
        return d

    return None


class Dept:
  def __init__(self, name, num): # Constructor
    self.name = name
    self.num = num

  def __str__(self):
    return f"{self.name} {self.num}"

  def __repr__(self):
    return f'Dept({repr(self.name)}, {repr(self.num)})'

depts = [
  Dept("Department:", 11),
  Dept("Department:", 22),
  Dept("Department:", 33),
]

my_store = Store("Durb's Store", depts) # Create a new Store object
print(my_store)

dept_num = input("Enter a department number: ")

dept_num = int(dept_num)

dept = my_store.find_dept(dept_num)

print(dept)