import sys

from shmup.game import Game

def main(args=None):
    app = Game()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())
