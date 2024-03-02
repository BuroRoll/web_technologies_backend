class Employee:
    def __init__(self, id: int, name: str, salary: int, department: str):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        self.__hours_salary__ = self.salary / 50

    def calculate_emp_salary(self, work_hours: int) -> float:
        if work_hours > 50:
            overtime: int = work_hours - 50
            overtime_amount: float = overtime * self.__hours_salary__
            return self.salary + overtime_amount
        return work_hours * self.__hours_salary__

    def assign_department(self, new_department: str) -> str:
        self.department = new_department
        return self.department

    def print_employee_details(self):
        print(f'Инофрмация о сотруднике:\n'
              f'{self.id} {self.name}\n'
              f'Департамент: {self.department}\n'
              f'Зарплата: {self.salary}₽')


if __name__ == '__main__':
    employee: Employee = Employee(1, 'Danil', 100_000, 'Отдел разработки')
    employee.assign_department('Отдел интеграции систем')
    employee.print_employee_details()
    work_hours: int = 100
    print(f'Зарплата за {work_hours} часов = {employee.calculate_emp_salary(work_hours)}₽')
