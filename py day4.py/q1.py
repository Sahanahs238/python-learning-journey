Gym = ["Pushups", "Pullups", "Squats", "Lunges", "Plank"]
#print("My Gym Routine:", Gym)
Gym[-1]="Plank for 1 minute"
print(Gym)
Gym.append("Burpees")
Gym.remove("Pullups")
print(Gym)
print(len(Gym))
for workout in Gym:
    print(workout)

