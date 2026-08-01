# Code assistance provided by OpenAI's ChatGPT

from datetime import datetime


# Define the Person class to represent each individual in the family tree
class Person:
    def __init__(self, name, birth_date, death_date=None):
        self.name = name  # Person's name
        self.birth_date = datetime.strptime(birth_date, '%d-%m-%Y')  # Birth date as a datetime object
        self.death_date = datetime.strptime(death_date, '%d-%m-%Y') if death_date else None  # Death date or None
        self.parents = []  # List of parent objects
        self.children = []  # List of child objects

    # Add a parent to the person and establish the relationship
    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)  # Add to parents list
            parent.children.append(self)  # Ensure the reverse relationship is set

    # Add a child to the person and establish the relationship
    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)  # Add to children list
            child.parents.append(self)  # Ensure the reverse relationship is set

    # Calculate the age of the person (at death or current age if alive)
    def calculate_age(self, on_date=None):
        end_date = self.death_date if self.death_date else (on_date or datetime.today())
        return (end_date - self.birth_date).days // 365  # Age in years

    # Get the number of children
    def get_children_count(self):
        return len(self.children)

    # Get the names of parents
    def get_parents(self):
        return [parent.name for parent in self.parents] if self.parents else 'No known parents.'

    # Get the names of grandparents
    def get_grandparents(self):
        grandparents = []
        for parent in self.parents:
            grandparents.extend([gp.name for gp in parent.parents])
        return grandparents if grandparents else 'No known grandparents.'

    # Get the names of grandchildren
    def get_grandchildren(self):
        grandchildren = []
        for child in self.children:
            grandchildren.extend([grandchild.name for grandchild in child.children])
        return grandchildren if grandchildren else 'No known grandchildren.'


# Define the FamilyTree class to manage all individuals and their relationships
class FamilyTree:
    def __init__(self):
        self.members = {}  # Dictionary to store family members by name

    # Add a person to the family tree (create if not already present)
    def add_person(self, name, birth_date, death_date=None):
        if name not in self.members:
            self.members[name] = Person(name, birth_date, death_date)  # Create a new Person object
        return self.members[name]

    # Find parents of a given person
    def find_parents(self, name):
        person = self.members.get(name)
        return person.get_parents() if person else 'Person not found.'

    # Find grandparents of a given person
    def find_grandparents(self, name):
        person = self.members.get(name)
        return person.get_grandparents() if person else 'Person not found.'

    # Find grandchildren of a given person
    def find_grandchildren(self, name):
        person = self.members.get(name)
        return person.get_grandchildren() if person else 'Person not found.'

    # Calculate the average age at death for deceased members
    def calculate_average_age_at_death(self):
        deceased = [person for person in self.members.values() if person.death_date]
        if not deceased:  # No deceased members
            return 0
        total_age = sum(person.calculate_age() for person in deceased)
        return total_age / len(deceased)

    # Calculate total and average number of children
    def calculate_children_statistics(self):
        children_counts = [person.get_children_count() for person in self.members.values()]
        total_children = sum(children_counts)
        average_children = total_children / len(children_counts) if children_counts else 0
        return total_children, average_children

    # List the number of children for each individual
    def list_children_for_individuals(self):
        return {person.name: person.get_children_count() for person in self.members.values()}

    # Merge another family tree into this one
    def merge_family_trees(self, other_tree):
        for name, person in other_tree.members.items():
            if name not in self.members:
                self.members[name] = person


# Function to display the menu and handle user options
def menu(tree):
    while True:
        # Display menu options
        print("\n=== Family Tree Menu ===")
        print("1. View Average Age at Death")
        print("2. View Number of Children for Each Individual")
        print("3. Add a New Person")
        print("4. View Total and Average Number of Children")
        print("5. Find Parents")
        print("6. Find Grandparents")
        print("7. Find Grandchildren")
        print("8. Exit")

        # Get user choice
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            # Calculate and display average age at death
            average_age_at_death = tree.calculate_average_age_at_death()
            print(f"\nAverage age at death: {average_age_at_death:.2f} years")
        elif choice == "2":
            # List number of children for each individual
            children_for_individuals = tree.list_children_for_individuals()
            print("\nNumber of children for each individual:")
            for name, count in children_for_individuals.items():
                print(f"{name}: {count} children")
        elif choice == "3":
            # Add a new person to the tree
            name = input("Enter the person's name: ").strip()
            birth_date = input("Enter the birth date (DD-MM-YYYY): ").strip()
            death_date = input("Enter the death date (DD-MM-YYYY, or leave blank if alive): ").strip() or None
            tree.add_person(name, birth_date, death_date)
            print(f"\n{name} has been added to the family tree.")
        elif choice == "4":
            # Display total and average number of children
            total_children, average_children = tree.calculate_children_statistics()
            print(f"\nTotal children in the family tree: {total_children}")
            print(f"Average number of children per person: {average_children:.2f}")
        elif choice == "5":
            # Find and display parents of a given person
            name = input("Enter the person's name to find their parents: ").strip()
            print("Parents of", name, ":", tree.find_parents(name))
        elif choice == "6":
            # Find and display grandparents of a given person
            name = input("Enter the person's name to find their grandparents: ").strip()
            print("Grandparents of", name, ":", tree.find_grandparents(name))
        elif choice == "7":
            # Find and display grandchildren of a given person
            name = input("Enter the person's name to find their grandchildren: ").strip()
            print("Grandchildren of", name, ":", tree.find_grandchildren(name))
        elif choice == "8":
            # Exit the program
            print("\nExiting the program. Goodbye!")
            break
        else:
            # Handle invalid input
            print("\nInvalid choice. Please try again.")


# Initialize the family tree
family_tree = FamilyTree()

# Add all family members
# Add members by name and date of birth, and link relationships
cornelia = family_tree.add_person("Cornelia Emmershon", "05-12-1990")
otto = family_tree.add_person("Otto Emmershon", "11-04-1988")
alex = family_tree.add_person("Alex Emmershon", "20-01-1965")
maria = family_tree.add_person("Maria Emmershon", "18-03-1968")
sagar = family_tree.add_person("Sagar Ali", "15-05-1970")
mysha = family_tree.add_person("Mysha Ali", "22-09-1973")
alfred = family_tree.add_person("Alfred Emmershon", "12-07-1930", "01-01-1999")
veronica = family_tree.add_person("Veronica Emmershon", "10-06-1933", "05-08-2005")
jacek = family_tree.add_person("Jacek Nowak", "15-04-1940")
sally = family_tree.add_person("Sally Nowak", "30-11-1945")
rishi = family_tree.add_person("Rishi Ali", "07-07-1940")
akshata = family_tree.add_person("Akshata Ali", "14-08-1944")
mohhamed = family_tree.add_person("Mohhamed Rahman", "18-02-1935", "12-12-2000")
shaviga = family_tree.add_person("Shaviga Rahman", "25-10-1937", "10-07-2002")

# Define family relationships
mohhamed.add_child(mysha)
shaviga.add_child(mysha)
akshata.add_child(sagar)
rishi.add_child(sagar)
sally.add_child(maria)
jacek.add_child(maria)
alfred.add_child(alex)
veronica.add_child(alex)
sagar.add_child(cornelia)
mysha.add_child(cornelia)
alex.add_child(otto)
maria.add_child(otto)

# Run the menu for user interaction
menu(family_tree)

# Code assistance provided by OpenAI's ChatGPT# Code assistance provided by OpenAI's ChatGPT