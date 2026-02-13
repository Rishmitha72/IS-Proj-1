import pandas as pd
products = pd.Series(
    [700, 150, 300], 
    index=['Laptop', 'Mouse', 'Keyboard']
)
print("Full Series:")
print(products)
print("\nPrice of Laptop:")
print("\nFirst two products:")
print(products[:2])

import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print("Missing values (True = missing):")
print(grades.isnull())
filled_grades = grades.fillna(0)
print("\nFilled Series (missing replaced with 0):")
print(filled_grades)
filtered_grades = filled_grades[filled_grades > 60]
print("\nFiltered results (scores > 60):")
print(filtered_grades)

import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned = usernames.str.strip()
cleaned = cleaned.str.lower()
contains_a = cleaned.str.contains('a')
print("Cleaned Series:")
print(cleaned)
print("\nNames containing 'a':")
print(contains_a)