
class Bot:
    def __init__(self, enemy_sign):
        self.__sign = "\033[91mB\033[0m"
        self.__nick = "BOT"
        self.__enemy_sign = enemy_sign

    def getenemy_sign(self):
        return self.__enemy_sign

    def getsign(self):
        return self.__sign

    def set(self, field, board):
        board.setfield(field, self.getsign())

    def setfield(self, board):
        box = board.getfields()

        if box.get("1") == self.getsign() and box.get("2") == self.getsign() and box.get("3") == " ":
            self.set("3", board)
                                                                                                                         # +++
        elif box.get("1") == self.getsign() and box.get("3") == self.getsign() and box.get("2") == " ":                  # ---
            self.set("2", board)                                                                                         # ---

        elif box.get("2") == self.getsign() and box.get("3") == self.getsign() and box.get("1") == " ":
            self.set("1", board)


        elif box.get("4") == self.getsign() and box.get("5") == self.getsign() and box.get("6") == " ":
            self.set("6", board)
                                                                                                                        # ---
        elif box.get("4") == self.getsign() and box.get("6") == self.getsign() and box.get("5") == " ":                 # +++
            self.set("5", board)                                                                                        # ---

        elif box.get("5") == self.getsign() and box.get("6") == self.getsign() and box.get("4") == " ":
            self.set("4", board)


        elif box.get("7") == self.getsign() and box.get("8") == self.getsign() and box.get("9") == " ":
            self.set("9", board)
                                                                                                                        # ---
        elif box.get("7") == self.getsign() and box.get("9") == self.getsign() and box.get("8") == " ":                 # ---
            self.set("8", board)                                                                                        # +++

        elif box.get("8") == self.getsign() and box.get("9") == self.getsign() and box.get("7") == " ":
            self.set("7", board)


        elif box.get("1") == self.getsign() and box.get("4") == self.getsign() and box.get("7") == " ":
            self.set("7", board)
                                                                                                                        # +--
        elif box.get("1") == self.getsign() and box.get("7") == self.getsign() and box.get("4") == " ":                 # +--
            self.set("4", board)                                                                                        # +--

        elif box.get("4") == self.getsign() and box.get("7") == self.getsign() and box.get("1") == " ":
            self.set("1", board)


        elif box.get("2") == self.getsign() and box.get("5") == self.getsign() and box.get("8") == " ":
            self.set("8", board)
                                                                                                                        # -+-
        elif box.get("2") == self.getsign() and box.get("8") == self.getsign() and box.get("5") == " ":                 # -+-
            self.set("5", board)                                                                                        # -+-

        elif box.get("5") == self.getsign() and box.get("8") == self.getsign() and box.get("2") == " ":
            self.set("2", board)


        elif box.get("3") == self.getsign() and box.get("6") == self.getsign() and box.get("9") == " ":
            self.set("9", board)

        elif box.get("3") == self.getsign() and box.get("9") == self.getsign() and box.get("6") == " ":                 # --+
            self.set("6", board)                                                                                        # --+
                                                                                                                        # --+
        elif box.get("6") == self.getsign() and box.get("9") == self.getsign() and box.get("3") == " ":
            self.set("3", board)


        elif box.get("3") == self.getsign() and box.get("5") == self.getsign() and box.get("7") == " ":
            self.set("7", board)
                                                                                                                        # --+
        elif box.get("3") == self.getsign() and box.get("7") == self.getsign() and box.get("5") == " ":                 # -+-
            self.set("5", board)                                                                                        # +--

        elif box.get("5") == self.getsign() and box.get("7") == self.getenemy_sign() and box.get("3") == " ":
            self.set("3", board)


        elif box.get("1") == self.getsign() and box.get("5") == self.getsign() and box.get("9") == " ":
            self.set("9", board)
                                                                                                                        # +--
        elif box.get("1") == self.getsign() and box.get("9") == self.getsign() and box.get("5") == " ":                 # -+-
            self.set("5", board)                                                                                        # --+

        elif box.get("5") == self.getsign() and box.get("9") == self.getsign() and box.get("1") == " ":
            self.set("1", board)



        elif box.get("1") == self.getenemy_sign() and box.get("2") == self.getenemy_sign() and box.get("3") == " ":
            self.set("3", board)
                                                                                                                        #+++
        elif box.get("1") == self.getenemy_sign() and box.get("3") == self.getenemy_sign() and box.get("2") == " ":     #---
            self.set("2", board)                                                                                        #---

        elif box.get("2") == self.getenemy_sign() and box.get("3") == self.getenemy_sign() and box.get("1") == " ":
            self.set("1", board)


        elif box.get("4") == self.getenemy_sign() and box.get("5") == self.getenemy_sign() and box.get("6") == " ":
            self.set("6", board)
                                                                                                                        #---
        elif box.get("4") == self.getenemy_sign() and box.get("6") == self.getenemy_sign() and box.get("5") == " ":     #+++
            self.set("5", board)                                                                                        #---

        elif box.get("5") == self.getenemy_sign() and box.get("6") == self.getenemy_sign() and box.get("4") == " ":
            self.set("4", board)


        elif box.get("7") == self.getenemy_sign() and box.get("8") == self.getenemy_sign() and box.get("9") == " ":
            self.set("9", board)
                                                                                                                        #---
        elif box.get("7") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("8") == " ":     #---
            self.set("8", board)                                                                                        #+++

        elif box.get("8") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("7") == " ":
            self.set("7", board)


        elif box.get("1") == self.getenemy_sign() and box.get("4") == self.getenemy_sign() and box.get("7") == " ":
            self.set("7", board)
                                                                                                                        #+--
        elif box.get("1") == self.getenemy_sign() and box.get("7") == self.getenemy_sign() and box.get("4") == " ":     #+--
            self.set("4", board)                                                                                        #+--

        elif box.get("4") == self.getenemy_sign() and box.get("7") == self.getenemy_sign() and box.get("1") == " ":
            self.set("1", board)


        elif box.get("2") == self.getenemy_sign() and box.get("5") == self.getenemy_sign() and box.get("8") == " ":
            self.set("8", board)
                                                                                                                        #-+-
        elif box.get("2") == self.getenemy_sign() and box.get("8") == self.getenemy_sign() and box.get("5") == " ":     #-+-
            self.set("5", board)                                                                                        #-+-

        elif box.get("5") == self.getenemy_sign() and box.get("8") == self.getenemy_sign() and box.get("2") == " ":
            self.set("2", board)


        elif box.get("3") == self.getenemy_sign() and box.get("6") == self.getenemy_sign() and box.get("9") == " ":
            self.set("9", board)

        elif box.get("3") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("6") == " ":     #--+
            self.set("6", board)                                                                                        #--+
                                                                                                                        #--+
        elif box.get("6") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("3") == " ":
            self.set("3", board)


        elif box.get("3") == self.getenemy_sign() and box.get("5") == self.getenemy_sign() and box.get("7") == " ":
            self.set("7", board)
                                                                                                                        #--+
        elif box.get("3") == self.getenemy_sign() and box.get("7") == self.getenemy_sign() and box.get("5") == " ":     #-+-
            self.set("5", board)                                                                                        #+--

        elif box.get("5") == self.getenemy_sign() and box.get("7") == self.getenemy_sign() and box.get("3") == " ":
            self.set("3", board)


        elif box.get("1") == self.getenemy_sign() and box.get("5") == self.getenemy_sign() and box.get("9") == " ":
            self.set("9", board)
                                                                                                                        #+--
        elif box.get("1") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("5") == " ":     #-+-
            self.set("5", board)                                                                                        #--+

        elif box.get("5") == self.getenemy_sign() and box.get("9") == self.getenemy_sign() and box.get("1") == " ":
            self.set("1", board)

        else:
            import random
            if box.get("5") == self.getenemy_sign():
                field = ["1", "3", "7", "9"]
                x = random.choice(field)
                while box.get(x) != " ":
                    x = random.choice(field)
                self.set(x, board)
            else:
                field = random.randint(1,10)
                while box.get(str(field)) != " ":
                    field = random.randint(1, 10)
                self.set(str(field), board)

if __name__ == '__main__':
    import Game
    board = {"1": "X", "2": "X", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}








