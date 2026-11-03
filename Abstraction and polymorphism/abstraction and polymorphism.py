class Student(User):
    def __init__(self, name, room_number, student_id):
        super().__init__(name, room_number)
        self.student_id = student_id

    def get_role(self):
        return "Student"


class HostelWarden(User):
    def __init__(self, name, room_number, staff_id):
        super().__init__(name, room_number)
        self.staff_id = staff_id

    def get_role(self):
        return "Hostel Warden"
    # Creating objects
student = Student("Grace", "B12", "S001")
warden = HostelWarden("Mr James", "Office 1", "W001")

# Demonstrating polymorphism
users = [student, warden]

for user in users:
    print(user.name, "is a", user.get_role())