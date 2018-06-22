
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Miyuki")
define y = Character("Yu")


# The game starts here.

label start:

    scene bg room

    show eileen happy

    m "You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
