from src.contacts_book import ContactsBook
from src.record import Record


class Assistant:
    # """Main assistant class that handles user interaction"""
    def __init__(self):
        self.contacts_book = ContactsBook()
        self.running = False

    def run(self):
    # """Run the main loop of the assistant"""
        self.running = True
        print("Welcome to the Personal Assistant!")
        self.show_help()

        while self.running:
            try:
                command = input("Enter a command: ").strip().lower()
                self.process_command(command)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                self.running = False

            except Exception as e:
                print(f"Error: {e}")


    def process_command(self, command):
        # """Process user command"""
        if command in ["exit", "quit", "q"]:
            print("Goodbye!")
            self.running = False
        elif command == "help":
            self.show_help()
        elif command == "add":
            self.add_contact()
        elif command == "show all":
            self.show_all_contacts()
        elif command.startswith("find "):
            name = command[5:].strip()
            self.find_contact(name)
        else:
            print("Unknown command. Type 'help' for available commands.")
    

    def show_help(self):
         """Show available commands"""
         print("\nAvailable commands:")
         print("  add - Add a new contact")
         print("  show all - Show all contacts")
         print("  find [name] - Find a contact by name")
         print("  help - Show this help message")
         print("  exit/quit/q - Exit the program\n")
    

    def add_contact(self):
         """Add a new contact"""
         try:
             name = input("Enter name: ").strip()
             if not name:
                 print("Name cannot be empty.")
                 return
             
             # Check if contact already exists
             if self.contacts_book.find(name):
                 print(f"Contact '{name}' already exists.")
                 return
             
             # Create a new contact record
             record = Record(name)
             
             # Add phone numbers
             while True:
                 phone = input("Enter phone number (leave empty to skip): ").strip()
                 if not phone:
                     break
                 try:
                     record.add_phone(phone)
                     add_another = input("Add another phone? (y/n): ").strip().lower()
                     if add_another != 'y':
                         break
                 except ValueError as e:
                     print(f"Error: {e}")
             
             # Add the record to the address book
             self.contacts_book.add_record(record)
             print(f"Contact '{name}' added successfully.")
             
         except ValueError as e:
             print(f"Error: {e}")


    def show_all_contacts(self):
         """Show all contacts"""
         if not self.contacts_book.data:
             print("No contacts found.")
             return
         
         print("\nAll contacts:")
         for record in self.contacts_book.data.values():
             print(record)


    def find_contact(self, name):
        # """Find a contact by name"""
        record = self.contacts_book.find(name)
        if record:
            print(f"\nFound contact:\n{record}")
        else:
            print(f"Contact '{name} not found.")
    



