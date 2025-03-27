from collections import UserDict


class ContactsBook(UserDict): 

    def add_record(self, record):
        self.data[record.name.value] = record
        return True


    def find(self, name):
        return self.data.get(name)
    

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False
    

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    


    