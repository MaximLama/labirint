import game


# MAIN
def main():
    game_instance = game.Game()
    game_instance.initialize()
    game_instance.update()
    return 0


if __name__ == "__main__":
    main()
