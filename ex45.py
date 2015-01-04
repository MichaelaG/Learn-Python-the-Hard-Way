# Example 45

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured.  Subclass it and implement"
        "enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter

class DiningCommons(Scene):

    def enter(self):
        print "Welcome to the wonderfully pink castle!!"
        print "Do you want to take a load off or wonder about the castle?"

        action = raw_input("> ")

        if action == "sit down":
            print "Guess you are not interested in taking a tour"
            print "That is okay... I only just cleaned for the past week..."
            return 'finished'

        elif action == "take a tour":
            print "YAY!! Follow me!!"
            return 'bedroom'

        else:
            print "My you are indecisive.  I'll decide for you! Follow me!"
            return 'bedroom'

class Bedroom(Scene):

    def enter(self):
        print "This is where I like to sleep at night!"
        print "Isn't it cool how huge it is?? Some say this room is the size"
        print "of many of the commoners' entire homes!  Not to mention, I have"
        print "a large walk-in closet located in the back! It can hold everything"
        print "So, what do you think?"

        action = raw_input("> ")

        if action == "you're crazy":
            print "I don't like you either... please leave now.  The tour is over"
            return 'finished'

        elif action == "you are the best!":
            print "I am glad you think so!! This way to the next room!"
            return 'bathing_room'

        else:
            print "Hmmm I guess no words are better than hurtful ones!"
            print "On to the next room!"
            return 'bathing_room'

class BathingRoom(Scene):

    def enter(self):
        print "Here is the bathing room!! Why don't we call it the bathroom you ask?"
        print "Well, we have lots more than just a bathtub of course!"
        print "we have a shower with 360 degree faucets and the tub is practically"
        print "a spa, with jets that gently massage your body!"
        print "The floor is also made of golden tiles!  Look how it sparkles!"
        print "Ain't it pretty??"

        action = raw_input("> ")

        if action == "nah":
            print "You have upset the princess... Beware her wrath!"
            print "She walks right up to you, looks you right in the eyes,"
            print "and BOOM! Breaks your neck.  Guess you shouldn't have talked"
            print "bad about the awesome jacuzzi!"
            return 'finished'

        elif action == "I love it!":
            print "Yay!!! I knew you would like it!! We should continue the tour"
            print "This way to more beauties!!"
            return 'moat'

        elif action == "I COULD STAY HERE ALL DAY":
            print "Oh me too!  Go ahead, get comfortable!"
            return 'finished'

        else:
            print "HOW DARE YOU!"
            print "Guess we are done here..."
            return 'finished'

class Moat(Scene):

    def enter(self):
        print "As we look outside, take a look around at the clear sky and"
        print "snowy mountains in the distance.  As well as the man-eating"
        print "aligators swimming around below in the moat!  Muahahahahahaha..."
        print "I mean, beware!  Don't walk too close to the edge of the bridge."
        print "But man, look how that water sparkles when the sun hits it."
        print "Dontcha like it??"

        action = raw_input("> ")

        if action == "I'm scared...":
            print "Scared??? Why are you scared?? Poor baby..."
            print "I'LL GIVE YOU SOMETHING TO BE SCARED ABOUT!"
            print "And she pushes you into the moat and you get to see the "
            print "aligators... up close and personal!  Before it eats you whole!"
            return 'finished'

        elif action == "My the water does sparkle!":
            print "I know right!! It is beautiful!  Almost as pretty as me! And not"
            print "quite as sparkly as my gorgeous crown. But nobody ever notices that..."
            print "everyone always likes to look at the water more than me..."
            print "And as a small tear falls off her face, you reach out and brush it "
            print "off, she looks right at you and smiles.  "
            print "We should go to the last room to finish this off..."
            return 'dungeon'

        else:
            print "Wow... if you are that speechless, then you should just leave"
            print "We are already outside, so just go ahead and cross the bridge"
            print "and leave"
            return 'finished'

class Dungeon(Scene):

    def enter(self):
        print "Here's the last room of the castle!  This is where we keep all the"
        print "bad boys and girls, the traitors and the criminals.  We don't keep"
        print "it nice down here, we want those you have done bad deeds to suffer"
        print "just a bit.  Wanna see any of the stalls?"

        action = raw_input("> ")

        if action == "Sure":
            print "Well here is the number one cell.  Nobody is being held here, so"
            print "it allows me to show it off to anybody interested.  We have state of "
            print "the art concrete walls and concrete floors that match perfectly."
            print "Some even have a tiny barred window up towards the ceiling to allow"
            print "in the smallest bit of sunlight.  It is like the perfect box for the"
            print "perfect criminal."
            print "But now our tour is over!  Thank for being a good sport!"
            return 'finished'

        elif action == "not really...":
            print "Good!  We could use somebody to fill one of our empty stalls."
            print "Now she is throwing you in the stall."
            return 'finished'

        elif action == "Of course!":
            print "oooo I like your excitement!  Eh lets forget the dungeon, it is not"
            print "THAT cool.  Why don't we start the tour over??  Maybe we can "
            print "discuss which room is your favorite!"
            return 'dining_commons'

        else:
            print "Well if you are not gonna say anything... then I guess we are done here"
            print "Lets go back up to the dining commons and maybe see if you can find your"
            print "words up there... I hate silent people..."
            return 'dining_commons'

class Finished(Scene):

    def enter(self):
        print "Guess we are done!  You left, whether that be to heaven or just leaving"
        print "the conversation to take in the room, or just straight up crossing the"
        print "bridge and going on your merry way"
    #    return 'finished'
        exit(1)

class Map(object):

    scenes = {
        'dining_commons': DiningCommons(),
        'bedroom': Bedroom(),
        'moat': Moat(),
        'bathing_room': BathingRoom(),
        'dungeon': Dungeon(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

map = Map('dining_commons')
game = Engine(map)
game.play()
