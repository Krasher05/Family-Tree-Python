# Code assistance provided by OpenAI's ChatGPT

# Define the Person class with relationships
class Person:
    def __init__(self, name):
        self.name = name   # The persons name
        self.parents = []  # Stores the person's parents
        self.children = []  # Stores the person's children

    def add_parent(self, parent):
        self.parents.append(parent)  # Add the person to the list
        parent.children.append(self)  # Automatically add this person as a child to the parent

    def add_child(self, child):
        self.children.append(child) # add the person the children list
        child.parents.append(self)  # Automatically add this person as a parent to the child

    def get_parents(self):
        return [parent.name for parent in self.parents] if self.parents else 'No known parents.'

    def get_grandparents(self):
        #create an empty list to store the names of grandparents
        grandparents = []
        #go through each parent looking at their parents and names to the list
        for parent in self.parents:
            grandparents.extend([gp.name for gp in parent.parents])
            # return the list of grandparents if not a message if none are found
        return grandparents if grandparents else 'No known grandparents.'

    def get_grandchildren(self):
        #create an empty list to store the names of grand children(same thing as grandparents)
        grandchildren = []
        #for each child look at their children and their names to the list
        for child in self.children:
            grandchildren.extend([grandchild.name for grandchild in child.children])
            #return the list of grandchildren if not a message if none are found
        return grandchildren if grandchildren else 'No known grandchildren.'


# Define the FamilyTree class to store family members and their relationships
class FamilyTree:
    def __init__(self):
        self.members = {} # a dictionary to store all family members by name

    def add_person(self, name):
        # check if the person already exists in the family tree
        if name not in self.members:
            # if not, a new person object and store it in dictionary needs to be created
            self.members[name] = Person(name)
            # return the Person object
        return self.members[name]

    def find_parents(self, name):
        # collect the Person object from the members dictionary
        person = self.members.get(name)
        #if the person exists use their grandparents() method otherwise jut=st return an error message
        return person.get_parents() if person else 'Person not found.'

    def find_grandparents(self, name):
        # Retrieve the Person object from the members dictionary
        person = self.members.get(name)
        # #if the person exists use their grandparents() method otherwise just return an error message
        return person.get_grandparents() if person else 'Person not found.'

    def find_grandchildren(self, name):
        # Retrieve the Person object from the members dictionary
        person = self.members.get(name)
        # #if the person exists use their grandparents() method otherwise jut=st return an error message
        return person.get_grandchildren() if person else 'Person not found.'


# Initialize family tree
family_tree = FamilyTree()

# Create and add family members to the family tree
cornelia = family_tree.add_person('Cornelia Emmershon')
otto = family_tree.add_person('Otto Emmershon')

alex = family_tree.add_person('Alex Emmershon')
maria = family_tree.add_person('Maria Emmershon')

sagar = family_tree.add_person('Sagar Ali')
mysha = family_tree.add_person('Mysha Ali')

alfred = family_tree.add_person('Alfred Emmershon')
veronica = family_tree.add_person('Veronica Emmershon')

jacek = family_tree.add_person('Jacek Nowak')
sally = family_tree.add_person('Sally Nowak')

rishi = family_tree.add_person('Rishi Ali')
akshata = family_tree.add_person('Akshata Ali')

mohhamed = family_tree.add_person('Mohhamed Rahman')
shaviga = family_tree.add_person('Shaviga Rahman')

# Define family relationships in the tree
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


# Interactive functionality to search family relationships
def interactive_family_search():
    while True: # Loop until the user chooses to exit
        # Display the menu options
        print("\nFamily Tree Query Options:")
        print("1. Find parents")
        print("2. Find grandparents")
        print("3. Find grandchildren")
        print("4. Exit")
# prompt the user to select an option
        choice = input("Select an option (1, 2, 3, or 4): ")
# handle each menu option
        if choice == "1":
            # find parents
            name = input("Enter the person's name to find their parents: ")
            # call the find_parents method and display the result1
            print("Parents of", name, ":", family_tree.find_parents(name))

        elif choice == "2":
            # find grandparents
            name = input("Enter the person's name to find their grandparents: ")
            # Call the find_grandparents method and display the result
            print("Grandparents of", name, ":", family_tree.find_grandparents(name))

        elif choice == "3":
            # Find grandchildren
            name = input("Enter the person's name to find their grandchildren: ")
            # call the find_granchildren method and display the result
            print("Grandchildren of", name, ":", family_tree.find_grandchildren(name))

        elif choice == "4":
            #exit the program
            print("Exiting the program.")
            # exit the while loop
            break

        else:
            # handle invalid input
            print("Invalid choice. Please select a valid option.")


# Run the interactive family search
interactive_family_search()

# Code assistance provided by OpenAI's ChatGPT