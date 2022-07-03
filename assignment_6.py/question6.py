class student_data:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def student_id(self):
        print(f'name : {self.name} ||| branch : {self.branch}')


s = student_data('aniket', 'civil')
# function
s.student_id()

# arguments
print('--->', s.name)
print('--->', s.branch)










