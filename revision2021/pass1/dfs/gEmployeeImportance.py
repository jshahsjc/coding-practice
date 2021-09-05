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

class Employee:
    def __init__(self, id, importance, subordinates = []):
        self.id = id
        self.importance =  importance
        self.subordinates = subordinates

def getImportance(employees, query_id):
    e_map =  { e.id: e for e in employees }

    def dfs(e_id):
        employee = e_map[e_id]
        return employee.importance + sum( dfs(s_id) for s_id in employee.subordinates )

    return dfs(query_id)


"""
Alternate solution:
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
"""

def employeeImportance(employees, q_id):
    keep = { e[0]: e for e in employees }
    def dfs(e_id):
        e = keep[e_id]
        e_imp = e[1]
        e_sub = e[2]
        if not e_sub:
            return e_imp
        for s_id in e_sub:
            e_imp += dfs(s_id)
        return e_imp
    return dfs(q_id)


def employeeImportance(employees, q_id):
    e_dict = { e[0]: e for e in employees }
    def dfs(e_id):
        emp = e_dict[e_id]
        importance = emp[1]
        subordinates = emp[2]
        for s in subordinates:
            importance += dfs(s)
        return importance
    return dfs(q_id)
