"""
You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.

Example:
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.

"""

def empImp(employees, id):
    """
    employees: list of list or objects of class employees
    """
    e_dict = { e[0]: e for e in employees }
    def dfs(e_id):
        emp = e_dict[e_id]
        imp = emp[1]
        sub = emp[2]
        for s in sub:
            imp += dfs(s)
        return imp
    return dfs(id)
