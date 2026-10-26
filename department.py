""" provides the department-class """
class Department:
    """
    A department with its employees

    Attributes
    ----------
    designation: str
        the unique designation of the department
    employees: list(Employee)
        a list of all employees working for this department
    """

    def __init__(self, designation):
        self._designation = designation
        self._employees = []

    def __str__(self):
        output = f'Mitarbeiter von {self.designation}:'
        for employee in self._employees:
            output += f'\n  - {employee.name}'
        return output + '\n------'

    def __eq__(self, other):
        if not isinstance(other, Department):
            raise TypeError('not an object of class Employee')
        return self.designation == other.designation

    def add_employee(self, employee):
        if not employee in self._employees:
            if len(self._employees) >= 15:
                raise OverflowError('too many entries')
            else:
                self._employees.append(employee)
                employee.add_department(self)

    def take_employee(self, index):
        if len(self._employees) < index:
            raise IndexError('not found')
        return self._employees[index]

    def remove_employee(self, name):
        for employee in self._employees:
            if employee.name == name:
                self._employees.remove(employee)
                employee.remove_department(self.designation)


    @property
    def designation(self):
        """ returns the designation """
        return self._designation