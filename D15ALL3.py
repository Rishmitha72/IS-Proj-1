import random
trials = 1000
count_sum_7 = 0
for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1
probability = count_sum_7 / trials
print(f"Experimental Probability of sum = 7: {probability:.4f}")


import random
trials = 100000
count_heads_and_six = 0
for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    if coin == "H" and die == 6:
        count_heads_and_six += 1
prob_independent = count_heads_and_six / trials
print(f"Experimental Probability (Heads AND 6): {prob_independent:.4f}")
count_two_red = 0
for _ in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)
    if first == "R" and second == "R":
        count_two_red += 1
prob_dependent = count_two_red / trials
print(f"Experimental Probability (Two Reds): {prob_dependent:.4f}")


P_spam = 0.1
P_ham = 0.9
P_free_given_spam = 0.9
P_free_given_ham = 0.05
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)
P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print(f"Probability that an email with 'Free' is Spam: {P_spam_given_free:.4f}")