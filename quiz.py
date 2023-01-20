# user enter yes to play game or no quit
# if user input is 1 say snake gam eand box game and bounce gmae
# if user input 1 say SNAK BITE YOU
# if 2 say YOU ARE BOXED
# if 3 say LET'S BOUNCE
# type 1 to roll or 2 to quit
# if 1 say you've rolled GOODBYE

user_plays = input('\nEnter \'-yes\' to play Or \'-no\' to quit: ').lower()
if user_plays == "yes":
	user_choice = int(input("Enter \n1- Snake game\n2-Box game\n3-Bounce game\n:"))
	if user_choice == 1:
		print("\nYOU ARE BITTEN BY PYTHON")
	elif user_choice == 2:
		print("\nSORRY! YOU ARE BOXED")
	else:
		print("\nLET'S BOUNCE")
		user_roll = input("\nType\n1- To ROLL\nQUIT- TO QUIT\n:").lower()
		if user_roll == "1":
			print("\nYOU'VE ROLLED")
		else:
			print("\nYOU QUIT")
else:
	print("\nTHANK YOU FOR COMING")






































#if user_plays == "yes":
#    userChoice = int(input("""
#    		Choose a game
#   		 1- Snake game
#  		 2- Box game
#   		 3- Bounce game
#    """))
#        if userChoice == 1:
#            print("SNAKE BITE YOU")
#        elif userChoice == 2:
#            print("YOU ARE BOXED")
#        else:
#            print("LET'S BOUNCE")
#            userBounce = int(input("""
#            Type:
#            1- to Roll
#            2- to quit
#            """))
#            if userBounce == 1:
#                print("YOU'VE BOUNCED")
#            else:
#                print("YOU QUIT")
#else:
#    print("Thanks for coming! GOODBYE")