
class GameMode:
    def __init__(self):
        print("Game Mode Menu\n"
              "1 - Player vs Bot\n"
              "2 - Player vs Player")
        self.mode = input("[*] Choose game mode:")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
            if mode == '1':
                self._mode = "solo"
            elif mode == '2':
                self._mode = "pvp"
            else:
                raise ValueError("[*] There is not such an option")


class Board:
    def __init__(self):
        self.__fields = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def getfield(self, field):
        return self.__fields[field]

    def getfields(self):
        return self.__fields

    def setfield(self, field, sign):
        self.__fields.update({field : sign})

    def __str__(self):
        return(f" {self.getfield('1')} | {self.getfield('2')} | {self.getfield('3')}\n"
              "---|---|---\n"
              f" {self.getfield('4')} | {self.getfield('5')} | {self.getfield('6')}\n"
              "---|---|---\n"
              f" {self.getfield('7')} | {self.getfield('8')} | {self.getfield('9')}\n")


    def checkFields(self): #po każdej turze sprawdzane jest czy, któryś z graczy wygrał
        box = self.getfields()
        if box.get("1") != " " and (box.get("1") == box.get("2")) and (box.get("1") == box.get("3")):
            print(f"[*] Player {box.get('1')} win!!!")
            return True
        elif  box.get("4") != " " and (box.get("4") == box.get("5")) and (box.get("4") == box.get("6")):
            print(f"[*] Player {box.get('4')} win!!!")
            return True
        elif  box.get("7") != " " and (box.get("7") == box.get("8")) and (box.get("7") == box.get("9")):
            print(f"[*] Player {box.get('7')} win!!!")
            return True
        elif  box.get("1") != " " and (box.get("1") == box.get("4")) and (box.get("1") == box.get("7")):
            print(f"[*] Player {box.get('1')} win!!!")
            return True
        elif  box.get("2") != " " and (box.get("2") == box.get("5")) and (box.get("2") == box.get("8")):
            print(f"[*] Player {box.get('5')} win!!!")
            return True
        elif  box.get("3") != " " and (box.get("3") == box.get("6")) and (box.get("3") == box.get("9")):
            print(f"[*] Player {box.get('3')} win!!!")
            return True
        elif  box.get("3") != " " and (box.get("3") == box.get("5")) and (box.get("3") == box.get("7")):
            print(f"[*] Player {box.get('3')} win!!!")
            return True
        elif  box.get("1") != " " and (box.get("1") == box.get("5")) and (box.get("1") == box.get("9")):
            print(f"[*] Player {box.get('1')} win!!!")
            return True
        else:
            notempty = 0
            for x in box:
                if box.get(x) != " ":
                    notempty += 1
            if notempty == 9:
                print("[*] Draw!!!")
                return True
            else:
                return False


class Player:  # dorób kolory potem
    ID = 0
    def __init__(self, sign, nick):  # Znak/Nick
        self.sign = sign
        self.__nick = nick
        Player.ID += 1

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, sign):
        if len(sign) == 1:
            if Player.ID == 0:
                self._sign = f"\033[94m{sign}\033[0m"
            else:
                self._sign = f"\033[93m{sign}\033[0m"
        else:
            raise ValueError("[*] Sign must be 1 char!!!")

    def setnick(self, nick):
        self.__nick = nick

    def getnick(self):
        return self.__nick

    def getsign(self):
        return self.sign

    def setfield(self, board):  # metoda ustawia w wybranym polu znak gracza
        while True:
            key = input(f"[*] Insert field {self.getnick()}: ")
            if int(key) > 9 or int(key) < 1:
                print("[*] Field number must be in range 1-9")
            elif board.getfield(key) != " ":
                print("[*] Chosen field is busy")
            else:
                board.setfield(key, self.getsign())
                break



class Menu:
    def __init__(self):
        print("MENU\n"
              "1 - Play\n"
              "2 - Quit\n")
        self.option = input("Choose: ")

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self, option):
        if option == "1":
            self._option = GameMode()
        elif option == "2":
            exit()
        else:
            raise ValueError("[*] There is not such an option")

    def __str__(self):
        return "MENU\n" \
               "1 - Solo\n" \
               "2 - PvP\n" \
               "3 - Quit\n"


class Play:

    def __init__(self, board, menu):
        self.menu = menu
        self.board = board
        self.player1 = None
        self.player2 = None

        if menu.option.mode == "solo":
            from bot import Bot
            self.player1 = Player(input("Enter Player1 sign: "), input("Enter Player1 nickname: "))
            self.player2 = Bot(self.player1.getsign())
        elif menu.option.mode == "pvp":
            self.player1 = Player(input("Player1\nEnter sign: "), input("Enter nickname: "))
            self.player2 = Player(input("Player2\nEnter sign: "), input("Enter nickname: "))
            while self.player2.getnick() == self.player1.getnick():
                print("[*] Nicks cant be the same!!!")
                self.player2.setnick(input("Enter nickname: "))


    def switch(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def rond_pvp(self, player):
        print(self.board)
        while not self.board.checkFields():
            player.setfield(self.board)
            print("\n"*100)
            print(self.board)
            player = self.switch(player)

    def rond_solo(self, player):
        print(self.board)
        while not self.board.checkFields():
            player.setfield(self.board)
            print("\n"*100)
            print(self.board)
            player = self.switch(player)


    def start_rand(self):
        import random
        switch = random.randint(0,100)
        if switch % 2 == 0:
            self.rond_solo(self.player1)
        else:
            self.rond_solo(self.player2)


if __name__ == '__main__':

    game = Play(Board(), Menu())
    game.start_rand()

