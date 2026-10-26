import string
import sys
from random import choices

import pytest

from department import Department
from employee import Employee


def test_employee_init(random_string):
    employee = Employee(random_string)
    assert employee.name == random_string
    assert employee._departments == []


def test_employee_add_department(random_string):
    employee = Employee('Karliene')
    if hasattr(employee, 'add_department') and callable(employee.add_department):
        department = Department(random_string)
        employee.add_department(department)
        assert employee._departments == [department]
    else:
        pytest.fail('add_department methode not implemented')


def test_employee_add_department_overflow(random_string):
    employee = Employee(random_string)
    if hasattr(employee, 'add_department') and callable(employee.add_department):
        for i in range(5):
            employee.add_department(Department(f'department {i}'))
        with pytest.raises(OverflowError):
            employee.add_department(Department(f'department 999'))
    else:
        pytest.fail('add_department methode not implemented')


def test_employee_take_department_by_name(random_string):
    employee = Employee('Karl')
    department = Department(random_string)
    if sys.version_info < (3, 8) or hasattr(employee, 'find_department'):
        employee.add_department(department)
        assert employee.find_department(random_string) == 0
    else:
        pytest.skip('Skipped compatibility test')


def test_employee_take_department(random_string):
    employee = Employee('Lee')
    department = Department(random_string)
    if hasattr(employee, 'take_department') and callable(employee.take_department):
        employee.add_department(department)
        assert employee.take_department(0) == department
    else:
        pytest.fail('take_department methode not implemented')


def test_employee_take_department_invalid(random_string):
    employee = Employee('Bruce')
    department = Department(random_string)
    if hasattr(employee, 'take_department') and callable(employee.take_department):
        employee.add_department(department)
        with pytest.raises(IndexError):
            employee.take_department(1)
    else:
        pytest.fail('take_department methode not implemented')


def test_employee_remove_department(random_string):
    employee = Employee('Delphine')
    department = Department(random_string)
    if hasattr(employee, 'remove_department') and callable(employee.remove_department):
        employee.add_department(department)
        employee.remove_department(random_string)
        assert employee._departments == []
    else:
        pytest.fail('remove_department methode not implemented')


def test_employee_len():
    employee = Employee('Svenja')
    if sys.version_info < (3, 8) or hasattr(employee, '__len__'):
        assert len(employee) == 0
        department = Department('Sales')
        employee.add_department(department)
        assert len(employee) == 1
    else:
        pytest.skip('Skipped compatibility test')


def test_employee_eq():
    employee1 = Employee('Svenja')
    employee2 = Employee('Svenja')
    assert employee1 == employee2
    employee3 = Employee('Mustafa')
    assert employee1 != employee3


@pytest.fixture
def random_string():
    return ''.join(choices(string.ascii_uppercase + string.ascii_lowercase, k=8))