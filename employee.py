class Employee:
  def __init__(name , age , salary):
    self.name = name
    self.age = age
    self.salary = salary

   def display_info(self):
    print(F"{self.name} {self.age} {self.salary}")


class Developer(Employee):
 def ___init__(self, name, age, salary, programming_language):
    super().__init__(name, age, salary)
    self.programming_language = programming_language

    def work(self):
        print(f"{self.name} {self.age} {self.salary} has{self.programming_language}")


class Manager(Employee):
    def ___init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
        
        def work(self):
            print(f"{self.name} {self.team_size}")
        
        dev = Developer("Алекс", 30, 70000,"Python")
        man = Manager("Екатерина", 40, 90000, 10)
        
        dev.display_info()
        dev.work()

        print()

        man.display_info()
        man.work()



