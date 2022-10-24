import numpy as np


class Tetris:

    def __init__(self):
        self.figure = None
        borders = input("Enter border parameters (for example: 10 10): ").split()
        self.x = int(borders[0])
        self.y = int(borders[1])
        self.field = np.array(["-" for _ in range(self.x * self.y)])
        self.figures = {"O": [[4, 14, 15, 5]],
                        "I": [[4, 14, 24, 34], [3, 4, 5, 6]],
                        "S": [[5, 4, 14, 13], [4, 14, 15, 25]],
                        "Z": [[4, 5, 15, 16], [5, 15, 14, 24]],
                        "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
                        "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
                        "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}
        self.coord = None
        self.counter = 0
        self.print()

    def del_figure(self):
        for i in self.coord[self.counter]:
            self.field[i] = "-"

    def print_figure(self):
        for i in self.coord[self.counter]:
            self.field[i] = "0"
        self.print()

    def check_border(self):
        for i in self.coord[self.counter]:
            if self.x * (self.y - 1) <= i < self.x * self.y:
                return True
            if self.field[i + 10] == "0" and i + 10 not in self.coord[self.counter]:
                return True
        return False

    def check_rotate(self):
        right = False
        left = False
        for i in self.coord[self.counter]:
            if (i + 1) % self.x == 0:
                right = True
            if i % self.x == 0:
                left = True
        if left and right:
            return False
        return True

    def check_end(self):
        for i in range(self.x):
            column = [a for a in range(i, self.x * self.y, 10)]
            if all(self.field[col_pos] == "0" for col_pos in column):
                print("Game Over!")
                exit()

    def move_command(self):
        while True:
            command = input("Enter command (piece, break, right, left, down, rotate, exit): ")
            if command == "exit":
                exit()
            if command == "piece":
                self.counter = 0
                self.figure = input("Enter piece (O, I, S, Z, L, J, T): ")
                self.coord = self.figures[self.figure]
                self.print_figure()
                if not self.check_border():
                    self.del_figure()
            elif command == "break":
                counter = self.x
                for pos in range(self.y):
                    row = self.field[counter - self.x:counter]
                    check = False
                    for i in row:
                        if i == "-":
                            counter += self.x
                            check = True
                            break
                    if check:
                        continue
                    a = [i for i in range(counter - self.x, counter)]
                    help_field = np.delete(self.field, a)
                    new_field = np.insert(help_field, 0, ["-" for _ in range(self.x)])
                    self.field = new_field
                    counter += self.x
                self.print()
                continue
            elif not self.check_border():
                if command == "right":
                    num = 11
                    for i in self.coord[self.counter]:
                        if (i + 1) % self.x == 0:
                            num = 10
                            break
                elif command == "left":
                    num = 9
                    for i in self.coord[self.counter]:
                        if i % self.x == 0:
                            num = 10
                            break
                elif command == "down" or command == "rotate":
                    num = 10
                nums_array = []
                for nums in self.coord:
                    new_coord = []
                    for i in nums:
                        new_coord.append(i + num)
                    nums_array.append(new_coord)
                self.coord = nums_array
                if command == "rotate":
                    self.counter += 1
                    if self.counter == len(self.coord):
                        self.counter = 0
                    if not self.check_rotate():
                        if self.counter != 0:
                            self.counter -= 1
                self.print_figure()
                self.check_end()
            elif self.check_border():
                self.print()
                self.check_end()
            if not self.check_border():
                self.del_figure()

    def print(self):
        counter = self.x
        for _ in range(self.y):
            print(*self.field[counter - self.x:counter])
            counter += self.x
        print()


tetris = Tetris()
tetris.move_command()

