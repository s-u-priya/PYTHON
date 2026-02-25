class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")

# 🚗 Get user input to create a Car object
make = input("Enter the car's make: ")
model = input("Enter the car's model: ")
year = input("Enter the car's year: ")

# Create a Car instance
car = Car(make, model, year)

# 🕹️ Ask user what to do
action = input("Type 'start' to start the car or 'stop' to stop it: ").strip().lower()

if action == "start":
    car.start()
elif action == "stop":
    car.stop()
else:
    print("Invalid action. Please type 'start' or 'stop'.")
