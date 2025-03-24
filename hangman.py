word_list = ["algorithms", "functions", "structures", "input", "output", "programming", "project", "colors", "animals", "food",
    "water", "mcdonalds", "pizza", "snickers", "card", "watch", "doctors", "medicine", "machine", "cars",
    "university", "tools", "messages", "preview", "music", "netflix", "mail", "settings", "calendar", "september",
    "weather", "files", "history", "classes", "view", "representation", "dictionary", "narrow", "simplify", "element",
    "language", "feedback", "design", "number", "script", "speaker", "success", "hosting", "computer", "engine", "tires", "brakes", 
    "headlights", "steering", "gearbox", "accelerator", "clutch", "chassis", "suspension",
    "exhaust", "fuel", "battery", "dashboard", "odometer", "speedometer", "radiator", "transmission", "carburetor",
    "turbocharger", "alloy wheels", "spoiler", "hood", "trunk", "windshield", "mirrors", "seatbelt", "airbags",
    "ignition", "cylinders", "horsepower", "torque", "drivetrain", "axle", "muffler", "catalytic converter", "ABS",
    "traction control", "cruise control", "lane assist", "GPS", "bluetooth", "headlights", "taillights", "turn signals",
    "motorcycle", "handlebars", "kickstand", "helmet", "gears", "throttle", "chain", "sprocket", "fork", "shock absorber",
    "fairing", "footpegs", "fuel tank", "exhaust pipe", "rims", "tire pressure", "oil filter", "air filter", "coolant",
    "spark plugs", "piston", "camshaft", "crankshaft", "valves", "clutch lever", "brake pads", "disc brakes", "drum brakes",]

import random
class TriadHangman:
    def _init_(player, word_list, guessed_letters, total_attempts=6):
        player.word = random.choice(word_list)
        player.guessed_letters = set()
        player.total_attempts = total_attempts
        player.attempts_left = total_attempts
        player.current_state = ['_'] * len(player.word)
