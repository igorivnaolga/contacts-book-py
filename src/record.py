from src.field import Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                return self.phones.pop(i)
            

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
            return False
        

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"