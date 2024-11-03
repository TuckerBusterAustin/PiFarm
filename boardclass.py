#pifarm boards:

class Boards:
    def __init__(self,name,board_type, specs):
            self.name = name
            self.board_type = board_type
            self.specs = specs # expand?
    def display_info(self):
          return f"{self.name}, {self.board_type}, {self.specs}"
    


pi_boards = {
    "pi4alpha": Boards(name="pi4alpha", board_type="Raspberry Pi 4", specs="4GB RAM, Quad-core"),
    "pi4bravo": Boards(name="pi4bravo", board_type="Raspberry Pi 4", specs="2GB RAM, Dual-core"),
    "pivpn": Boards(name="pivpn", board_type="Raspberry Pi 4 VPN", specs="8GB RAM, Quad-core"),
    "pi3alpha": Boards(name="pi3alpha", board_type="Raspberry Pi 3", specs="4GB RAM, Quad-core"),
    "pi3bravo": Boards(name="pi3bravo", board_type="Raspberry Pi 3", specs="4GB RAM, Quad-core"),
    "pi3charlie": Boards(name="pi3charlie", board_type="Raspberry Pi 3", specs="2GB RAM, Dual-core"),
    "pi3delta": Boards(name="pi3delta", board_type="Raspberry Pi 3", specs="8GB RAM, Quad-core"),
    "nanoalpha": Boards(name="nanoalpha", board_type="AI Nano Jetson", specs="4GB RAM, Quad-core"),
    "nanobeta": Boards(name="nanobeta", board_type="AI Nano Jetson", specs="4GB RAM, Quad-core"),
    "pi5alpha": Boards(name="Bpi5alphaeta", board_type="Raspberry Pi 5", specs="2GB RAM, Dual-core")
}

#print(pi_boards['pi4alpha'].display_info())

for key, piboard in pi_boards.items():
      print(f"{piboard.display_info()}")