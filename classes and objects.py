# ==========================================
# 7. DUCK TYPING
# ==========================================

class GuestStudent:
    
    ##This class does not inherit from User.
    #However, it has the attributes and method
    #required by display_user().
    
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Guest Student"


def display_user(user):
    
    ##Accepts any object that provides name and get_role().
    

    print(f"Name: {user.name}")
    print(f"Role: {user.get_role()}")


# ==========================================
# 8. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    # Create the hostel borrowing system.
    hostel_system = ShoeBorrowingSystem(
        "UCU Students' Hostel"
    )

    # Create students.
    grace = Student("Grace", "B12", "S001", 39)
    sarah = Student("Sarah", "B15", "S002", 39)
    brian = Student("Brian", "B18", "S003", 42)

    # Create hostel warden.
    warden = HostelWarden("Mr James", "Office 1", "W001")

    # Register shoes.
    shoe1 = Shoe("SH001", "Sports Shoes", 39, sarah)
    shoe2 = Shoe("SH002", "Formal Shoes", 42, brian)
    shoe3 = Shoe("SH003", "Sneakers", 40, grace)

    warden.register_shoe(hostel_system, shoe1)
    warden.register_shoe(hostel_system, shoe2)
    warden.register_shoe(hostel_system, shoe3)

    # Display available shoes.
    hostel_system.show_available_shoes()

    # Grace requests Sarah's sports shoes.
    print("\nTEST 1: VALID BORROWING REQUEST")

    grace.request_shoe(
        hostel_system, "SH001", 2, True
    )

    # Brian tries to borrow the same shoes.
    print("\nTEST 2: BORROWING AN UNAVAILABLE PAIR")

    brian.request_shoe(
        hostel_system, "SH001", 2, True
    )

    # Grace tries to borrow another pair before returning.
    print("\nTEST 3: ONE ACTIVE LOAN RULE")

    grace.request_shoe(
        hostel_system, "SH002", 2, True
    )

    # Grace returns Sarah's shoes.
    print("\nTEST 4: RETURNING SHOES")

    hostel_system.return_shoe(grace, "SH001")

    # Grace can now request another pair.
    print("\nTEST 5: REQUEST AFTER RETURN")

    grace.request_shoe(
        hostel_system, "SH002", 2, True
    )

    # Display updated inventory and records.
    hostel_system.show_available_shoes()
    hostel_system.show_borrowing_records()

