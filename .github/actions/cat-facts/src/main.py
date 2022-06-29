import requests
import random
import sys

# Create an empty list to store individual facts in
# This will make it easy to select a random one later
fact_list = [
'lol 1',
'lol 2',
'lol 3',
]

# Add the "text" of every object into the fact_list list
for fact in r_obj_list:
    fact_list.append(fact["text"])

# Select a random fact from the fact_list and return it
# into a variable named random_fact so we can use it
def select_random_fact(fact_arr):
    return fact_arr[random.randint(0, len(fact_list)+1)]

random_fact = select_random_fact(fact_list)

# Print the individual randomly returned cat-fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
