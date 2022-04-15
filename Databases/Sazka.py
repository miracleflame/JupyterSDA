from random import randint

class Sazka:

    def __init__(self, rows):
        self.rows = int(input("Zadej pocet tahu: "))
        n_numbers = int(input("Zadej pocet losovanych cisel: "))


    def play_sazka(rows, n_numbers):

        for i in range(rows):
            line = []
            for i in range(n_numbers):
                # random_number = randint(1, 49)
                # while random_number in line:
                #     random_number = randint(1, 49)
                random_number = random.sample(range(1, 51), 5)
                line.append(random_number)
            print(sorted(line))

    def euromiliony(self):

        list_of_first_rounds = []
        counter = 0
        while counter < 6:
            round_one = []
            for i in range(5):
                x = random.randint(1, 50)
                round_one.append(x)
                final_round_one = sorted(round_one)
            if len(set(final_round_one)) == len(final_round_one):
                list_of_first_rounds.append(final_round_one)
                counter += 1
            else:
                continue

play_sazka(10, 6)




# class Sazka:
#     """there could be documentation"""
#     def __init__(self, count_of_round):
#         self.count_of_round = count_of_round
#
#     def generate_numbers(self, count, range_start, range_stop):
#         tah = []
#         while len(tah) < count:
#             num = random.randint(range_start, range_stop)
#             if num in tah:
#                 continue
#             tah.append(num)
#         sorted_list = sorted(tah)
#         return sorted_list
#
#     def sportka(self):
#         whole_round = []
#         for _ in range(self.count_of_round):
#             one_round = self.generate_numbers(6, 1, 49)
#             whole_round.append(one_round)
#         return whole_round
#
#     def eurojackpot(self):
#         whole_round = []
#         for _ in range(self.count_of_round):
#             five_numbers = self.generate_numbers(5, 1, 50)
#             two_numbers = self.generate_numbers(2, 1, 10)
#             one_round = [five_numbers, two_numbers]
#             whole_round.append(one_round)
#         return whole_round
#
#     def extra_renta(self):
#         whole_round = []
#         for _ in range(self.count_of_round):
#             one_round = self.generate_numbers(7, 1, 33)
#             whole_round.append(one_round)
#         return whole_round
#
#
# ticket_sportka = Sazka(2).sportka()
# ticket_euromiliony = Sazka(3).eurojackpot()
# ticket_extra_renta = Sazka(4).extra_renta()
# print(ticket_sportka)
# print(ticket_euromiliony)
# print(ticket_extra_renta)