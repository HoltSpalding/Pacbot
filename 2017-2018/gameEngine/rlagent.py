import subprocess
import os, sys, logging
import robomodules as rm
from messages import *
from pacbot.variables import game_frequency, ticks_per_update
from pacbot import StateConverter, GameState


from gameEngine import GameEngine 

ADDRESS = os.environ.get("BIND_ADDRESS","localhost")
PORT = os.environ.get("BIND_PORT", 11297)

#open the server
bashCommand = 'screen -dmS "screen-name-1" ./server.py'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print(error)

class GE(GameEngine):
    def __init__(self, addr, port):
        # GameEngine.__init__(self, addr, port)
        self.subscriptions = [MsgType.PACMAN_LOCATION]
        super().__init__(addr, port, message_buffers, MsgType, FREQUENCY, self.subscriptions)
        self.game = GameState()
        self.loop.add_reader(self.game._should_die():, self.keypress)


    def check_game_state(self):
        return self.game._die()

        
    def main():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s',
                        datefmt="%I:%M:%S %p")
        engine = GameEngine(ADDRESS, PORT)
        print('Game is paused.')
        print('Controls:')
        print('    r - restart')
        print('    p - (un)pause')
        print('    q - quit')

        engine.run()


if __name__ == "__main__":
    GE.main()
