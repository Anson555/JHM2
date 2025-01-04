import random
class GhostLeg:
    def __init__(self, lines, connectors):
        self.lines = lines
        self.connectors = connectors
        self.leg = self.create_leg()

    def create_leg(self):
        leg = [[0] * (self.lines - 1) for _ in range(self.connectors)]
        for i in range(self.connectors):
            line = random.randint(0, self.lines - 2)
            leg[i][line] = 1
        return leg

    def display_leg(self):
        for i in range(self.connectors):
            for j in range(self.lines - 1):
                if self.leg[i][j] == 1:
                    print("|---", end="")
                else:
                    print("|   ", end="")
            print("|")
def follow_path(leg, start):
    position = start
    for i in range(len(leg)):
        if position > 0 and leg[i][position - 1] == 1:
            position -= 1
        elif position < len(leg[0]) and leg[i][position] == 1:
            position += 1
    return position
def main():
    lines = 5
    connectors = 10

    ghost_leg = GhostLeg(lines, connectors)
    ghost_leg.display_leg()

    for i in range(lines):
        result = follow_path(ghost_leg.leg, i)
        print(f"Start at line {i + 1} ends at line {result + 1}")

if __name__ == "__main__":
    main()
