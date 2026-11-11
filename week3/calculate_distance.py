#This program calculates the distance travelled given the following information
# x = v * t, where v = 80 mph and t = 2 hours

velocity = input("Enter velocity here: ")
time = input("Enter time here: ")

distance = float(velocity) * float(time)

print(f"The distance travlled for this example is: {distance} miles.")