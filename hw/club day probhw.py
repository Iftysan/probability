all_students = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
chess = {1, 2, 3, 4}
robotics = {3, 4, 5, 6, 7}
drama = {8, 9, 10}

#Part 1 chess and robotics
chess | robotics
print(chess | robotics)
chess & robotics
print(chess & robotics)
p_chess = len(chess) / len(all_students)
p_robotics = len(robotics) / len(all_students)
p_both = len(chess & robotics) / len(all_students)

p_union = p_chess + p_robotics - p_both

print(p_union)

p_union2 = len(chess | robotics) / len(all_students)

print(p_union2)

print(p_union == p_union2)

#part 3 chess and drama
chess & drama
len(chess | drama) / len(all_students)

#part 4 winning and not winning
winning = 2
total = 5
probability = winning / total
print(winning / total, "independent")

probability = (winning - 1) / (total - 1)