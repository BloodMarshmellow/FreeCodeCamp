import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for i in balls.keys():
            for x in range(0, balls[i]):
                self.contents.append(i)

    def draw(self, num_balls_drawn):
        drawing_content = []
        if len(self.contents) < num_balls_drawn:
            for y in range(len(self.contents)):
                drawing_content.append(self.contents[y])
            self.contents.clear()
            return drawing_content
        else:
            for y in range(num_balls_drawn):
                rand = random.randint(0,len(self.contents)-1)
                drawing_content.append(self.contents[rand])
                self.contents.pop(rand)
            return drawing_content


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_experiments = 0
    needed_balls = []
    cases = []
    for i in range (num_experiments):
        cases.append(copy.deepcopy(hat))
        needed_balls.append(copy.deepcopy(expected_balls))
        result = cases[i].draw(num_balls_drawn)
        for j in result:
            if (j in needed_balls[i]) and (needed_balls[i][j] != 0):
                needed_balls[i][j] = needed_balls[i][j] - 1
        if all(x == 0 for x in needed_balls[i].values()):
            success_experiments +=  1
    return success_experiments / num_experiments





