inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final updated inventory:", inventory)

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First reading:", temperatures[0])
print("Last reading:", temperatures[-1])
afternoon_peak = temperatures[3:6]
print("Afternoon Peak readings:", afternoon_peak)
last_three_hours = temperatures[-3:]
print("Last 3 Hours readings:", last_three_hours)

screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")
#screen_res[0] = 1280
print("Tuples cannot be modified!")