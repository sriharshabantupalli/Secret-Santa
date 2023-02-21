import random
import csv
import itertools


class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def select_receiver(self, receivers):
        mask = [receiver.name and receiver is not self
                for receiver in receivers]
        valid_receivers = list(itertools.compress(receivers, mask))
        if not valid_receivers:
            raise Exception('Failed to match pairs compatibily')
        receiver = random.choice(valid_receivers)
        return receiver

    def __str__(self):
        return self.name

    def __repr__(self):
        return self


class Pair:

    def __init__(self, giver, receiver):
        self.giver = giver
        self.receiver = receiver

    def __str__(self):
        return f"{self.giver.name}-{self.giver.email} - {self.receiver.name}-{self.receiver.email}"

    def __repr__(self):
        return self


class Group:

    def __init__(self,_):
        self.load_contact_data()
        self.generate_pairs()

    def load_contact_data(self):
        with open(r'C:\Users\harik\Desktop\santa\santaa.csv') as csvfile:
            self.people = []
            crew_data = csv.reader(csvfile)
            for row in crew_data:
                name, email = row[
                    0], row[1]
                self.people.append(
                    Person(name, email))

    def generate_pairs(self):
        self.pairs = []
        givers = self.people
        receivers = self.people
        for giver in givers:
            try:
                receiver = giver.select_receiver(receivers)
                receivers.remove(receiver)
                self.pairs.append(Pair(giver, receiver))
            except Exception:
                self.generate_pairs()


crew = Group(r'C:\Users\harik\Desktop\santa\santaa.csv')
print(crew)
list1=[]
for pair in crew.pairs:
    list1.append([pair.giver.name, pair.giver.email, pair.receiver.name, pair.receiver.email])


f = open('C:\\Users\\harik\\PycharmProjects\\santa\\random.csv', 'w',encoding='utf-8', newline="")
writer = csv.DictWriter(f, fieldnames=["name", "email","secretsanta name","secretsanta email"])
writer.writeheader()
w = csv.writer(f)
w.writerows(list1)


