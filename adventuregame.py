#I have spent a LOT of time on this haha. My extra things I have added is an extra question, I have 4 instead of 3. My question with at least 3 choices is on the second question 
#of each choice after question1. I also included a loop to have the game start over if you chose an option that cuts the game short for you. However, for some reason the loop always
#repeats itself if you chose choice B after question 1. I have spent so much time but can't figure it out. Let me know if you can help! Hopefully I won't get docked points since 
#this is part of my extra creativity part of the assignment, I just need some help. Thank you!

while True:
    question1 = input('You are a young slave living on the planet Tatooine. Your master asks you to run an errand for him, you need to buy supplies from the Jawas. As you are making a deal with them for some scraps, you notice two strange boxes that seem to be calling to you. Choose A) Left Box or B) Right Box? ')

    print()
    
    if question1.upper() == 'A':
        print('You grab the left box, and return to your master, hiding the box under your cloak. After finishing your work, you run into your room to see what is inside. You open the box and see a glowing red stone, a kyber crystal.')
        question1a = input('Do you A) Become scared of what it is, you take it to a market and sell it, B) Take it to your master to ask what it is, or C) Keep it hidden, and study it when you can? ')

        print()

        if question1a.upper() == 'A':
            print('You made enough money to free yourself from slavery, congrats!')
            question1ab = input('Do you A) Use the money to buy a ship, or B) Use the money to buy a small house and start a shady bar where you provide a meeting spot for bounty hunters and criminals across the galaxy? ')

            print()

            if question1ab.upper() == 'A':
                print('You bought a ship! You make plans to explore the galaxy. The questions you have about that glowing object still linger, maybe you"ll go somewhere to find answers.')
            elif question1ab.upper() == 'B':
                print('Your black market bar is thriving! Until you get caught. Jedi find you, you get arrested for running spice operations through Republic space.')

            print()

        elif question1a.upper() == 'B':
            print('He steals it from you and sells it, you are still stuck as a slave.')
            tryagain = input('Would you like to try again? A) yes or B) No: ')
            if tryagain.upper() == 'B':
                print('Game Over.')
                break
        elif question1a.upper() == 'C':
            print('After studying the krystal for a few weeks, you begin to have dreams. You see a man, with a dark mask over his mouth and gray stripes over his head. Flashes of red and darkness flash across your mind. You see a place, it is familiar. You have been there before, searching for scraps for your master.')
            question2a = input('Do you A) Ignore the dream, it must be the effects of all the spice you have been taking, or B) Go to the place you see in your dreams? ')

            print()

            if question2a.upper() == 'A':
                print('You keep the crystal, but hide it away. You also chill out on all the spice.')
            elif question2a.upper() == 'B':
                print('After finishing your duties the next day, you sneak out in the night to go to the place you have been dreaming of. You see a dark cave on the side of a desert mountain,')
                question3a = input('Do you A) Enter the cave, you feel something calling you there, or B) Run away, something feels dark. You choose to push away the darkness. ')

                print()

                if question3a.upper() == 'A':
                    print('You enter the cave, and see the shadow of the man you saw in your dreams. He steps into a streak of light entering from a hole in the wall of the cave. His face is pale, his eyes are yellow. He looks at you, and says in a low voice, “I am Darth Malak, but now you will call me Master”')
                elif question3a.upper() == 'B':
                    print('As you run from the cave, a ship flies down landing in front of you. The door opens, and see a woman step out, wielding a blue lightsaber. “Get behind me!” She yells. As you run towards the ship, you look behind you and see the man from your dreams running towards you, red lightsaber in hand.')

                print()

                print('To be continued...')
                break

    elif question1.upper() == 'B':
        print('You grab the right box, and return to your master, hiding the box under your cloak. After finishing your work, you run into your room to see what is inside. You open the box and see a glowing blue stone, a kyber crystal.')
        question1b = input('Do you A) Become scared of what it is, you take it to a market and sell it, B) Take it to your master to ask what it is, or C) Keep it hidden, and study it when you can? ')

        print()

        if question1b.upper() == 'A':
            print('You made enough money to free yourself from slavery, congrats!')
            question1ba = input('Do you A) Use the money to buy a ship, or B) Use the money to buy a small house and start a shady bar where you provide a meeting spot for bounty hunters and criminals across the galaxy? ')

            print()

            if question1ba.upper() == 'A':
                print('You bought a ship! You make plans to explore the galaxy. The questions you have about that glowing object still linger, maybe you"ll go somewhere to find answers.')
            elif question1ba.upper() == 'B':
                print('Your black market bar is thriving! Until you get caught. Jedi find you, you get arrested for running spice operations through Republic space.')

            print()

        elif question1b.upper() == 'B':
            print('He steals it from you and sells it, you are still stuck as a slave.')
            tryagain = input('Would you like to try again? A) yes or B) No: ')
            if tryagain == 'B':
                print('Game Over.')
                break
        elif question1b.upper() == 'C':
            print('After studying the krystal for a few weeks, you begin to have dreams. You see a woman, with dark hair wielding a double-bladed blue lightsaber. She calls your name. You see a place, it is familiar. You have been there before, searching for scraps for your master.')
            question2b = input('Do you A) Ignore the dream, it must be the effects of all the spice you have been taking, or B) Go to the place you see in your dreams? ')

            print()

            if question2b.upper() == 'A':
                print('You keep the crystal, but hide it away. You also chill out on all the spice.')
            elif question2b.upper() == 'B':
                print('After finishing your duties the next day, you sneak out in the night to go to the place you have been dreaming of. You see a dark cave on the side of a desert mountain,')
                question3b = input('Do you A) Run away, something feels dark. You choose to push away the darkness, or B) Enter the cave, there is a strong pull as though it is telling you to enter. There is a darkness to it, but you can feel its power as you enter. ')

                print()

                if question3b.upper() == 'A':
                    print('You enter the cave, and see the shadow of the man you saw in your dreams. He steps into a streak of light entering in from a hole in the wall of the cave. His face is pale, his eyes are yellow. He looks at you, and says in a low voice, “I am Darth Malak, but now you will call me Master”')
                elif question3b.upper() == 'B':
                    print('As you run from the cave, a ship flies down landing in front of you. The door opens, and see a woman step out, weilding a blue lightsaber. “Get behind me!” She yells. As you run towards the ship, you look behind you and see the man from your dreams running towards you, red lightsaber in hand.')
            
                    print()

                    print('To be continued...')

    elif question1.upper() == 'B':
        print('You grab the right box, and return to your master, hiding the box under your cloak. After finishing your work, you run into your room to see what is inside. You open the box and see a glowing blue stone, a kyber crystal.')
        question1b = input('Do you A) Become scared of what it is, you take it to a market and sell it, B) Take it to your master to ask what it is, or C) Keep it hidden, and study it when you can?')

        print()

        if question1b.upper() == 'A':
            print('You made enough money to free yourself from slavery, congrats!')
            question1ba = input('Do you A) Use the money to buy a ship, or B) Use the money to buy a small house and start a shady bar where you provide a meeting spot for bounty hunters and criminals across the galaxy?')

            print()

            if question1ba.upper() == 'A':
                print('You bought a ship! You make plans to explore the galaxy. The questions you have about that glowing object still linger, maybe you"ll go somewhere to find answers.')
            elif question1ba.upper() == 'B':
                print('Your black markeet bar is thriving! Until you get caught. Jedi find you, you get arrested for running spice operations through Republic space.')


    elif question1b.upper() == 'B':
        print('He steals it from you and sells it, you are still stuck as a slave.')
        tryagain = input('Would you like to try again? A) yes or B) No: ')
        if tryagain.upper() == 'B':
            print('Game Over.')
            break

        print() 

    elif question1b.upper() == 'C':
        print('After studying the krystal for a few weeks, you begin to have dreams. You see a woman, with dark hair weilding a double bladed blue lightsaber. She calls your name. You see a place, it is familiar. You have been there before, searching for scraps for your master.')
        question2b = input('Do you A) Ignore the dream, it must be the effects of all the spice you have been taking, or B) Go to the place you see in your dreams?')

        print()

        if question2b.upper() == 'A':
            print('You keep the crystal, but hide it away. You also chill out on all the spice.')
        elif question2b.upper() == 'B':
            print('After finishing your duties the next day, you sneak out in the night to go to the place you have been dreaming of. You see a dark cave on the side of a desert mountain,')
            question3b = input('Do you A) Run away, something feels dark. You choose to push away the darkness, or B) Enter the cave, there is a strong pull as though it is telling you to enter. There is a darkness to it, but you can feel its power as you enter.')

            print()

            if question3b.upper() == 'A':
                print('As you run from the cave, a ship flies down landing in front of you. The door opens, and see a woman step out, weilding a blue lightsaber. It is the same woman you have seen in your dreams! “Get behind me!” She yells. As you run towards the ship, you look behind you and see a man running towards you, red lightsaber in hand.')
            elif question3b.upper() == 'B':
                print('You enter the cave, and see the shadow of a man.. He steps into a streak of light entering in from a hole in the wall of the cave. His face is pale, his eyes are yellow, a dark mask over his mouth and gray stripes over his head. He looks at you, and says in a low voice, “I am Darth Malak, but now you will call me Master”.')

            print()

            print('To be continued...')
        break