# Assignment-7

# Create a class Employee with:
# - a public variable name,
# - a protected variable _salary,
# - a private variable __ssn.
# Access all three variables and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def get__ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary  # Protected variable updated
        else:
            print("Salary must be positive number")

    def display(self):
        print(f"Name: {self.name}")         # Public
        print(f"Salary: {self._salary}")    # Protected
        print(f"SSN: {self.__ssn}")         # Private

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Private SSN via method: {self.get__ssn()}")

m = Manager("Ibrahim", 12000, "234-2343-235", "Information Technology")

m.show_manager_info()

m.set_salary(40000)
print("Updated Salary (protected):", m._salary)

print("Private SSN via name mangling:", m._Employee__ssn)
