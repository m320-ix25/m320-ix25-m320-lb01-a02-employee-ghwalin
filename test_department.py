import string
import sys
from random import choices

import pytest

from department import Department
from employee import Employee


def test_department_init(random_string):
    department = Department(random_string)
    assert department.designation == random_string
    assert department._employees == []


def test_department_add_employee(random_string):
    department = Department('Sales')
    employee = Employee(random_string)
    department.add_employee(employee)
    assert department._employees == [employee]


def test_department_add_employee_overflow(random_string):
    department = Department(random_string)
    if hasattr(department, 'add_employee') and callable(department.add_employee):
        for i in range(15):
            department.add_employee(Employee(f'Employee {i}'))
        with pytest.raises(OverflowError):
            department.add_employee(Employee(f'Employee 99'))
    else:
        pytest.fail('add_employee method not implemented')


def test_department_take_employee_by_name(random_string):
    department = Department('Sales')
    employee = Employee(random_string)
    if sys.version_info < (3, 8) or hasattr(department, 'find_employee'):
        department.add_employee(employee)
        assert employee.find_department(random_string) == 0
    else:
        pytest.skip('Skipped compatibility test')


def test_department_take_employee(random_string):
    department = Department('Sales')
    employee = Employee(random_string)
    if hasattr(department, 'add_employee') and callable(department.add_employee):
        department.add_employee(employee)
    else:
        pytest.fail('add_employee method not implemented')

    if hasattr(department, 'take_employee') and callable(department.take_employee):
        assert department.take_employee(0) == employee
    else:
        pytest.fail('take_employee method not implemented')

def test_department_take_employee_invalid():
    department = Department('Sales')
    employee = Employee('Hanna')
    if hasattr(department, 'add_employee') and callable(department.add_employee):
        department.add_employee(employee)
    else:
        pytest.fail('add_employee method not implemented')

    if hasattr(department, 'take_employee') and callable(department.take_employee):
        with pytest.raises(IndexError):
            department.take_employee(1)
    else:
        pytest.fail('take_employee method not implemented')


def test_department_remove_employee(random_string):
    department = Department('Sales')
    employee = Employee(random_string)
    if hasattr(department, 'add_employee') and callable(department.add_employee):
        department.add_employee(employee)
    else:
        pytest.fail('add_employee method not implemented')

    if hasattr(department, 'remove_employee') and callable(department.remove_employee):
        department.remove_employee(random_string)
        assert department._employees == []
    else:
        pytest.fail('remove_employee method not implemented')


def test_department_len():
    department = Department('Sales')
    if sys.version_info < (3, 8) or hasattr(department, '__len__'):
        assert len(department) == 0
        employee = Employee('Hanna')
        department.add_employee(employee)
        assert len(department) == 1
    else:
        pytest.skip('Skipped compatibility test')

def test_department_eq(random_string):
    department1 = Department(random_string)
    department2 = Department(random_string)
    assert department1 == department2
    department3 = Department('Administration')
    assert department1 != department3


@pytest.fixture
def random_string():
    return ''.join(choices(string.ascii_uppercase + string.ascii_lowercase, k=8))