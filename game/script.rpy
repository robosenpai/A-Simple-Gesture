##### CHANGELOG #####
#6/21/18 RS - just started the structure and put in a bunch of placeholders









# The script of the game goes in this file.



### Placeholder for all of the images ###
### bg should be jpg and characters should be png
#image bg street = 'street.jpg'
#image bg bedroom = 'bedroom.jpg'
#image bg bathroom = 'bathroom.jpg'
#image bg bathroomMask = 'bathroomMask.jpg'
#image bg bathroomMaskCracked = 'bathroomMaskCracked.jpg'
#image yu apathetic ='yuApathetic.png'
#image yu
#image letter
#

# Character Declarations
define m = Character("Miyuki")  #Childhood Friend
define y = Character("Yu")      #MC
define s = Character("stranger")#Player

default smile = False
# The game starts here.

label start:



    scene bg street

    show yu apathetic

    "[[PLACEHOLDER]"

menu:
    "I see a boy walking past me...."

    "and I smile at him":
        $ smile = True;
        jump letter

    "and I quickly walk past":
        jump letter



label letter:

    scene letter

    "[[LETTER PLACEHOLDER]"
    # This ends the game.

    return
