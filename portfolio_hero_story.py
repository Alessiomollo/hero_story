print("The Princess of the Earth has been kidnapped, our hero has started his journey to rescue the princess")
hero = input("What is the name of our hero?\n")
print(f"{hero} arrives at the entrance of the cursed forest...")

forest = input ("if you wish to enter the forest type Yes \n if you want to go back type No \n")
forest_lower = forest.lower()

if forest_lower == "yes":
  print(" \n")
  goblin = input(f'{hero} enter the forest and he finds a group of Goblins waiting for him. \n Do you want to fight the Goblins with the "Bow" or with the "Sword"? \n')
  goblin_lower = goblin.lower()
  print(" \n")
  if goblin_lower == "bow":
      print("You take 3 arrows and shooting them at the same time and you manage to kill the group of Goblins")
      boat = input(f'After defeating the goblins {hero} find himself at the shore of a lake\n Do you want to "Swim" or do you want to look for a "Boat" \n')
      boat_lower = boat.lower()
      if boat_lower == "boat":
        print(" \n")
        print(f"{hero} builds a boat and manage to cross the river where Python is holding the princess hostage")
        kill = input ( 'As soon you seen the princess you decide to attack Python! \n Which weapon do you use? "Bow", "Knife", or "Sword"? \n')
        kill_lower = kill.lower()
        print(" \n")
        if kill_lower == "sword":
            print(f"Python run towards you, but you are able to dodge his attack and to use your sword to kill him! Python is dead and the Princess is safe! \n {hero} you are a true hero!")
            print('''          /__`.
                              / \ `\\
                             /   \  `\
                            /     \   \
                           /_______\  /\
                           (((( ))))
                          (((' . ')))
                          (((\_-_/)))
                          (((_) (_)))
                         /((( \ / )))\
                        / (((  ^  ))) \
                       / / ((  ^  )) \ \
                      ( (   \  ^  /   ) ) 
                       \ \   )www(   / /
                        `\\ /     \ //'
                          /'       `\
                         /           \
                        /             \
                       /               \
                      /                 \
                     /                   \
                    /                     \
                   /                       \
                  /                         \
                 /                           \ jgs
                |                             |
                `-----......_____......-----'
                ''')
        else:
            print("Python is immune to it and he kills you. \n You Die.")
            print('''.     |\___/|
                          /       \
                        |    /\__/|
                        ||\  <.><.>
                        | _     > )
                        \   /----
                           |   -\/
                        /     \  ''')
 
      else:
        print("You decide to swin, but the lake if full of alligator. They eat you! \n You Die.")
        print('''                  
                              .-._   _ _ _ _ _ _ _ _
                   .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
                   '.___ '    .   .--_'-' '-' '-' _'-' '._
                     V: V 'vv-'   '_   '.       .'  _..' '.'.
                       '=.____.=_.--'   :_.__.__:_   '.   : :
                               (((____.-'        '-.  /   : :
                                                  (((-'\ .' /
                                               _____..'  .'
                                               '-._____.-'



''')
    
  else:
      print("The Goblins jump on you and kill you. You Die!")
      print('''
                       ,      ,
                      /(.-""-.)\
                  |\  \/      \/  /|
                  | \ / =.  .= \ / |
                  \( \   o\/o   / )/
                   \_, '-/  \-' ,_/
                     /   \__/   \
                     \ \__/\__/ /
                   ___\ \|--|/ /___
                 /`    \      /    `\
                        '----'       \                          ''')

else:
  print("The people of the Earth thinks you are a coward and they hang you. \n You Die!")
  print(''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .''')



