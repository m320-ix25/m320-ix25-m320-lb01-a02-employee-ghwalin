""" provides the employee-class """
class Employee:
    """
    An employee working in a department

    Attributes
    ----------
    name: str
        the unique name of the employee
    departments: list(Department)
        a list of all departments this employee works in
    """

    def __init__(self, name):
        self._name = name
        self._departments = []

    def __str__(self):
        output = f'{self.name} arbeitet in:'
        for department in self._departments:
            output += f'\n  - {department.designation}'
        return output + '\n------'

    def __eq__(self, other):
        if not isinstance(other, Employee):
            raise TypeError('not an object of class Employee')
        return self.name == other.name

    def add_department(self, department):
        if not department in self._departments:
            if len(self._departments) >= 5:
                raise OverflowError('too many entries')
            else:
                self._departments.append(department)
                department.add_employee(self)

    def take_department(self, index):
        if len(self._departments) < index:
            raise IndexError('not found')
        return self._departments[index]

    def remove_department(self, designation):
        for department in self._departments:
            if department.designation == designation:
                self._departments.remove(department)
                department.remove_employee(self.name)


    @property
    def name(self):
        """ returns the name """
        return self._name