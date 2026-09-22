import random

def pick_ball_experiment():
    balls = ['Blue', 'Red', 'Green']

    result = random.choice(balls)
    pro = balls.count('Red')/len(balls)
    print("Probability of picking a Red Ball is:", pro)

    if result == 'Red':
        return 'Red ball was picked'
    else:
        return 'Better luck next time'

res = pick_ball_experiment()
print(res)