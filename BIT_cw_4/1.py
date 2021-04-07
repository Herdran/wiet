from collections import deque
import shelve
import uuid


class Employee:
    def __init__(self, name, age, pesel, email, hours_worked):
        self._name = name
        self._age = age
        self._pesel = pesel
        self._email = email
        self._hours_worked = hours_worked
        self._access_level = 1
        self._hours_to_work = 140
        self.id = str(uuid.uuid4())

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def pesel(self):
        return self._pesel

    @property
    def email(self):
        return self._email

    @property
    def hours_worked(self):
        return self._hours_worked

    @property
    def access_level(self):
        return self._access_level

    def check_access(self, needed_level):
        return needed_level <= self._access_level

    def hours_left(self):
        return self._hours_to_work - self._hours_worked

    def send_email(self, receiver):
        if self.check_access(receiver.acces_level):
            print(f"{self._name} sent an email to {receiver.name}")
        else:
            print("Access level too low for this operation")

    def __str__(self):
        return f"{self._name} is {self._age} years old"



class ITSupport(Employee):
    def __init__(self, name, age, pesel, email, hours_worked):
        super().__init__(name, age, pesel, email, hours_worked)
        self._access_level = 2
        self._ticket_list = deque()

    def add_ticket(self, ticket):
        self._ticket_list.append(ticket)

    def get_oldest_ticket(self):
        return self._ticket_list[0]

    def delete_oldest_ticket(self):
        self._ticket_list.popleft()


class Manager(Employee):
    def __init__(self, name, age, pesel, email, hours_worked):
        super().__init__(name, age, pesel, email, hours_worked)
        self._access_level = 3
        self._hours_to_work = 120

    def send_email_to_any(self, receiver):
        print(f"{self._name} sent an email to {receiver.name}")


if __name__ == '__main__':
    myEmployee = Employee("Dude", 12, "1234567890", "123@gamil.com", 30)
    welder = Employee("Dudet", 43, "1234567890", "544326@gamil.com", 37)
    mySupport = ITSupport("Dudo", 82, "1234567890", "123@gamil.com", 95)
    chief = Employee("Deda", 24, "1234567890", "fdsfsd@gamil.com", 67)

    print(chief)
    with shelve.open("employees.db", writeback=True) as db:
        print(list(db.items()))
        # db[myEmployee.id] = myEmployee
        # db[welder.id] = welder
        # db[mySupport.id] = mySupport
        # db[chief.id] = chief
