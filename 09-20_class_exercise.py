class Grade_Dictionary:
    
    def __init__(self,student_number):
        self.my_d = {}
        self.student_number = student_number
        
        for i in range(self.student_number):
            name = input('Student name:')
            grade = int(input('Grade:'))
            self.my_d[name] = grade
        print(self.my_d)

    def search(self,name):
        user_input = input('If you want search?')
        if name not in self.my_d:
            raise Exception("Sorry, your name does not exist")
        if user_input != 'Y' and user_input != 'N':
            raise Exception("Sorry, your input can just be 'Y' or 'N'")
        if user_input == 'Y':
            print(self.my_d[name])
            
    def add_or_update(self,name, grade):
        user_input = input('If you want add or update?')
        if user_input != 'Y' and user_input != 'N':
            raise Exception("Sorry, your input can just be 'Y' or 'N'")
        if user_input == 'Y':
            self.my_d[name] = grade
            
    def delete(self,name):
        user_input = input('If you want delete?')
        if name not in self.my_d:
            raise Exception("Sorry, your name does not exist")
        if user_input != 'Y' and user_input != 'N':
            raise Exception("Sorry, your input can just be 'Y' or 'N'")
        if user_input == 'Y':
            self.my_d.pop(name)
        
new_grade_d = Grade_Dictionary(2)

new_grade_d.search('Wang')
new_grade_d.add_or_update('Li', 100)
print(new_grade_d.my_d)
new_grade_d.add_or_update('Zhang', 90)
print(new_grade_d.my_d)
new_grade_d.delete('Zhang')
print(new_grade_d.my_d)