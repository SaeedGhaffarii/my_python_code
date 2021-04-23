# region Calculate salary
# # Calculate employees salary
# class Employee:
#     def __init__(self, emp_id, first_name, last_name, hours_worked, wage):
#         self.emp_id = emp_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.hours_worked = hours_worked
#         self.wage = wage
#
#     def __str__(self):
#         return (f"Employee Info:\n\t"
#                 f"Employee ID: {self.emp_id}\n\t"
#                 f"First Name: {self.first_name}\n\t"
#                 f"Last Name: {self.last_name}\n\t"
#                 f"Hours Worked: {self.hours_worked} hrs\n\t"
#                 f"Wage: ${self.wage:.2f}\n\t"
#                 f"Salary: ${self.calculate_salary():.2f}\n")
#
#     def calculate_salary(self):
#         return self.hours_worked * self.wage
#
#
# emp1 = Employee(1, "John", "Smith", 39, 13.)
# emp2 = Employee(2, "Jane", "Doe", 150, 20.)
#
# print(emp1.calculate_salary())
# print(emp2.calculate_salary())
# print(emp1)
# print(emp2)
# endregion
