import math
import random

import pandas as pd
import numpy as np


class Terr:
    def __init__(self):
        num_pets = random.randrange(10, 20)
        type_of_pets = []
        for i in range(0, num_pets):
            type_of_pets.append(random.randrange(1, 5))
        num_human = random.randrange(5, 10)
        terren = self.create_space()
        position_of_pets, position_of_human = self.initalize_position(terren, num_human, num_pets, type_of_pets)
        # ============Static setup for test===============\
        position_of_pets, position_of_human = self.read_file_test("input/test/input_test.txt")
        # ================================================
        terren_populate = self.populate(terren, position_of_pets, position_of_human)
        round_score = int(round(self.calculate_score(terren_populate, position_of_human, position_of_pets), 0))

        print("e")

    def calculate_score(self, terrain, position_of_human, position_of_pets):
        s_i = []
        for human_pos in position_of_human:
            r_i = len(position_of_human)
            n_i = 0
            y_pos = human_pos[0]
            x_pos = human_pos[1]
            list_visited = []
            list_to_question = []
            while True:
                if y_pos - 1 >= 1:
                    if terrain.loc[y_pos - 1, x_pos] != 6 and terrain.loc[y_pos - 1, x_pos] != 8 and [y_pos - 1,
                                                                                                      x_pos] not in list_visited:
                        list_visited.append([y_pos - 1, x_pos])
                        if math.isnan(terrain.loc[y_pos - 1, x_pos]):
                            list_to_question.append([y_pos - 1, x_pos])
                            r_i += 1
                        else:
                            n_i += 1
                            r_i += 1

                if x_pos - 1 >= 1:
                    if terrain.loc[y_pos, x_pos - 1] != 6 and terrain.loc[y_pos, x_pos - 1] != 8 and [y_pos,
                                                                                                      x_pos - 1] not in list_visited:
                        list_visited.append([y_pos, x_pos - 1])
                        if math.isnan(terrain.loc[y_pos, x_pos - 1]):
                            list_to_question.append([y_pos, x_pos - 1])
                            r_i += 1
                        else:
                            n_i += 1
                            r_i += 1

                if y_pos + 1 <= 30:
                    if terrain.loc[y_pos + 1, x_pos] != 6 and terrain.loc[y_pos + 1, x_pos] != 8 and [y_pos + 1,
                                                                                                      x_pos] not in list_visited:
                        list_visited.append([y_pos + 1, x_pos])
                        if math.isnan(terrain.loc[y_pos + 1, x_pos]):
                            list_to_question.append([y_pos + 1, x_pos])
                            r_i += 1
                        else:
                            n_i += 1
                            r_i += 1

                if x_pos + 1 <= 30:
                    if terrain.loc[y_pos, x_pos + 1] != 6 and terrain.loc[y_pos, x_pos + 1] != 8 and [y_pos,
                                                                                                      x_pos + 1] not in list_visited:
                        list_visited.append([y_pos, x_pos + 1])
                        if math.isnan(terrain.loc[y_pos, x_pos + 1]):
                            list_to_question.append([y_pos, x_pos + 1])
                            r_i += 1
                        else:
                            n_i += 1
                            r_i += 1

                if list_to_question:
                    next_point = list_to_question[0]
                    list_to_question.remove(next_point)
                    y_pos = next_point[0]
                    x_pos = next_point[1]
                else:
                    break
            s_i.append((abs(r_i) / 900) * 2 ** (-n_i))
        round_score = ((10 ** 8) * ((1 / len(position_of_human)) * sum(s_i)))
        return round_score

    def create_space(self):
        terren = pd.DataFrame(index=np.arange(1, 31), columns=np.arange(1, 31))
        return terren

    def populate(self, terren, position_of_pets, position_of_human):
        for pets_element in position_of_pets:
            y_pos = pets_element[0]
            x_pos = pets_element[1]
            type = pets_element[2]
            terren.loc[y_pos, x_pos] = type

        for human_element in position_of_human:
            y_pos = human_element[0]
            x_pos = human_element[1]
            terren.loc[y_pos, x_pos] = 6

        return terren

    def initalize_position(self, terrein, num_human, num_pets, type_of_pets):
        f = open("input/input_random.txt", "w+")

        position_of_pets = []
        position_of_human = []

        f.writelines(str(num_pets) + "\n")
        for num_element in range(0, num_pets):
            x_pos = random.randrange(1, 30)
            y_pos = random.randrange(1, 30)
            if math.isnan(terrein.iloc[y_pos, x_pos]):
                position_of_pets.append([y_pos, x_pos, type_of_pets[num_element]])
                f.writelines(str(y_pos) + " " + str(x_pos) + " " + str(type_of_pets[num_element]) + "\n")
            else:
                if num_element != 0:
                    num_element -= 1

        f.writelines(str(num_human) + "\n")
        for num_element in range(0, num_human):
            x_pos = random.randrange(1, 30)
            y_pos = random.randrange(1, 30)
            if math.isnan(terrein.iloc[y_pos, x_pos]):
                position_of_human.append([y_pos, x_pos])
                f.writelines(str(y_pos) + " " + str(x_pos) + "\n")
            else:
                if num_element != 0:
                    num_element -= 1

        f.close()
        return position_of_pets, position_of_human

    def read_file_test(self, path):
        position_of_pets = []
        position_of_human = []

        file_test = open(path, 'r')

        num_pets = file_test.readline()
        try:
            num_pets = int(num_pets)
        except Exception as e:
            print(e)
            num_pets = 0

        for index_pets in range(1, num_pets + 1):
            positon_pets = file_test.readline()
            line_pets = []
            for element in positon_pets.split():
                try:
                    line_pets.append(int(element))
                except Exception as e:
                    print(e)
                    line_pets.append(0)
            position_of_pets.append(line_pets)

        num_human = file_test.readline()
        try:
            num_human = int(num_human)
        except Exception as e:
            print(e)
            num_human = 0

        for index_human in range(0, num_human):
            positon_human = file_test.readline()
            line_human = []
            for element in positon_human.split():
                try:
                    line_human.append(int(element))
                except Exception as e:
                    print(e)
                    line_human.append(0)
            position_of_human.append(line_human)

        return position_of_pets, position_of_human


Terr()
