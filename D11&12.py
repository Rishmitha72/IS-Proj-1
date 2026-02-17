import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months, revenue, marker='o', linestyle='-', color='b')
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")
plt.show()

import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours, scores, color='blue', marker='o')
plt.xlabel("Hours Spent Studying")
plt.ylabel("Exam Scores")
plt.title("Relationship Between Study Hours and Exam Scores")
plt.show()

import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
trend = [100, 150, 200, 250, 300]
plt.subplot(1, 2, 1)
plt.bar(categories, sales, color=['blue', 'green', 'orange'])
plt.title("Sales by Category")
plt.xlabel("Product Categories")
plt.ylabel("Sales")
plt.subplot(1, 2, 2)
plt.plot(months, trend, marker='o', linestyle='-', color='red')
plt.title("Sales Trend Over Months")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()