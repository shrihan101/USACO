"""
ID: shrihan4
LANG: PYTHON3
TASK: gift1
"""

# open the file and get the data
f = open('gift1.in')
l = f.readlines()
f.close()

# get how many people there are
NP = int(l.pop(0))

people = { }

# removing the '\n' from the text
for i in range(len(l)):
    l[i] = l[i].strip()

# add people to the dict
for i in range(NP):
    people[str(l.pop(0))] = 0

# calculate the gifts
for i in range(NP):
    giver = l.pop(0)
    money_giving = int(l[0].split(' ')[0])
    num_of_people = int(l.pop(0).split(' ')[1])
    people[giver] -= money_giving

    if num_of_people != 0:
        wasted = money_giving % num_of_people
        people[giver] += wasted
        per_person = (money_giving-wasted) / num_of_people
        for j in range(num_of_people):
            person = l.pop(0)
            print(person)
            people[person] += per_person
            print(f'{person} got {per_person}')


f = open('gift1.out', 'w')

formatted = ""
for key in people:
    formatted += f'{key} {str(int(people[key]))}\n'

f.write(formatted)