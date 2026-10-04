import random

group = ["A", "B", "C", "D", "E", "F"]
split_number = [3, 2]
choices = random.choice(split_number)
others = len(group)-choices

random.shuffle(group)
group_a = group[0:choices]
group_b = group[choices:]

print(f'グループA：{sorted(group_a)}')
print(f'グループB：{sorted(group_b)}')
