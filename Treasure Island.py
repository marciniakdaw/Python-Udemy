print(''''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction=input("Choose way you want to go: left, right or straight ahead?  ")

if direction.lower()=="l" or direction.lower()=="left":
  print("You are on the lake bank")
  lake_decision=input("What do you do? Are you swimming or wait?  ")
  if lake_decision.lower()== "w" or lake_decision.lower()=="wait":
    print("Some fishman brought you to island.")
    door_decision=input("You stand on front of 3 doors. Witch one do you choose: red, blue, green? ")
    if door_decision.lower()=="b" or door_decision.lower()=="blue":
      print("You winn! The treasure is your's :-)")
    elif door_decision.lower()=="r" or door_decision.lower()=="red":
      print('''
                (  .      )
            )           (              )
                  .  '   .   '  .  '  .
           (    , )       (.   )  (   ',    )
           .' ) ( . )    ,  ( ,     )   ( .
         ). , ( .   (  ) ( , ')  .' (  ,    )
      (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''')
      print("Burn in fire. Game over!")
    else:
      print('''
                         (    )
                         ((((()))
                      |o\ /o)|
                       ( (  _')
                      (._.  /\__
                       ,\___,/ '  ')
        '.,_,,       (  .- .   .    )
         \   \\     ( '        )(    )
           \   \\    \.  _.__ ____( .  |
          \  /\\   .(   .'  /\  '.  )
             \(  \\.-' ( /    \/    \)
             '  ()) _'.-|/\/\/\/\/\|
                      '\\ .( |\/\/\/\/\/|
                  '((  \    /\    /
                   ((((  '.__\/__.')
                    ((,) /   ((()   )
                    "..-,  (()("   /
                      _//.   ((() ."
               _____ //,/" ___ ((( ', ___
                               ((  )
                                 / /
                               _/,/'
                             /,/,"     
      ''')
      print("Eaten by beasts. Game over!")
  else:
        print('''
        
                              _.---._     .---.
                    __...---' .---. `---'-.   `.
          ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
        -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
          ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
            ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
            ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
                ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
                    ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                        ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                            ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
        

        ''')
        print("Met a crocodile. Game over!")
elif direction.lower()=="r" or direction.lower()=="right":
  print("You fall into whole. Game over!")
else:
  print('''
  
                 ,  ,, ,
           , ,; ; ;;  ; ;  ;
        , ; ';  ;  ;; .-''\ ; ;
     , ;  ;`  ; ,; . / /8b \ ; ;
     `; ; .;'         ;,\8 |  ;  ;
      ` ;/   / `_      ; ;;    ;  ; ;
         |/.'  /9)    ;  ; `    ;  ; ;
        ,/'          ; ; ;  ;   ; ; ; ;
       /_            ;    ;  `    ;  ;
      `?8P"  .      ;  ; ; ; ;     ;  ;;
      | ;  .:: `     ;; ; ;   `  ;  ;
      `' `--._      ;;  ;;  ; ;   ;   ;
       `-..__..--''   ; ;    ;;   ; ;   ;
                   ;    ; ; ;   ;     ;
  
  ''')
  print("You met the lion. Game over!")
  # print("Game over")
