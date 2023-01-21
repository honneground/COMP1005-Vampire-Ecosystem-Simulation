import random

class Entities():
    states = ["remaining","perish"]

    def __init__(self, classification, XMAX, YMAX):
        self.state = self.states[0]
        self.position = [random.randint(0, XMAX),random.randint(0, YMAX)]
        self.classification = classification

    def getSize(self):
        sizsmap = {"water":15,"human":5,"vampire":5}
        size = sizsmap.get(self.classification, 5)
        return size
    def getColor(self):
        colormap = {"human":"g" ,"vampire":"r" ,"food":"tab:brown" ,"water":"b" ,"garlic":"tab:gray"}
        color = colormap.get(self.classification)
        return color

    def getShape(self):
        shapemap = {"Creatures":"o" ,"Ingestibles":"s"}
        shape = shapemap[type(self).__name__] if self.classification != "garlic" else "^"
        return shape

class Ingestibles(Entities):
    def __init__(self, classification, XMAX, YMAX):
        super().__init__(classification, XMAX, YMAX)
        nutrition_map = {"food":30 ,"water":50 ,"garlic":100}
        identifier_map = {"food":11 ,"water":12 ,"garlic":13}
        self.nutrition = nutrition_map[self.classification]
        self.identifier = identifier_map[self.classification]

class Creatures(Entities):
    def __init__(self, classification, XMAX, YMAX, exact_or_upto_steps):
        super().__init__(classification, XMAX, YMAX)
        self.health = 100
        self.age = random.randint(10,50)
        self.limit = [XMAX, YMAX]
        self.exact_or_upto_steps = exact_or_upto_steps

    def step_change(self, exact_or_upto_steps):
        if self.state == "remaining":
            steps = 4 if self.classification == "human" else 8
            movement = random.choice([(movx, movy) for movx in range(-steps, steps+1) for movy in range(-steps, steps+1) if abs(movx) + abs(movy) == steps and 0 <= movx+self.position[0] <= self.limit[0] and 0 <= movy+self.position[1] <= self.limit[1]]) if exact_or_upto_steps == True else random.choice([(movx, movy) for movx in range(-steps, steps+1) for movy in range(-steps, steps+1) if abs(movx) + abs(movy) <= steps and 0 <= movx+self.position[0] <= self.limit[0] and 0 <= movy+self.position[1] <= self.limit[1]])
            # How to motifly steps to move
            # if abs(movx) + abs(movy) <= steps #move up to n steps
            # if abs(movx) + abs(movy) == steps #move excat n steps
            self.position[0] += movement[0]
            self.position[1] += movement[1]
            self.age += 1
            if self.classification == "human":
                self.health -= 1
                if self.health < 1 or self.age == 70:
                    self.state = "perish"
                    return 1
        return 0

    def interact(self, object):
        if self.classification == "human":
            if type(object).__name__ == "Ingestibles":
                object.state = "perish"
                self.health += object.nutrition
                return object.identifier
                # print(f"A human just {object.verb} {object.classification}")
            if object.classification== "human":
                if random.random() <= 0.4:
                    self.health += 20
                    object.health -= 20
                    if object.health <1:
                        object.state = "perish"
                        return 3
                    else:
                        return 2
                else:
                    self.health += 10
                    object.health += 10
                    return 4
        if self.classification == "vampire":
            if object.classification== "human":
                if random.random() <= 0.7:
                    object.classification = "vampire"
                    return 5
                else:
                    self.state = "perish"
                    return 6
            if object.classification== "vampire":
                object.health -= 20
                self.health -= 20
                counter = 7
                if self.health < 0:
                    self.state = "perish"
                    counter += 1
                if object.health < 0:
                    object.state = "perish"
                    counter += 1
                return counter
        return 0