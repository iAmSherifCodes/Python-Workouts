# user enter yes to play game or no quit
# if user input is 1 say snake gam eand box game and bounce gmae
# if user input 1 say SNAK BITE YOU
# if 2 say YOU ARE BOXED
# if 3 say LET'S BOUNCE
# type 1 to roll or 2 to quit
# if 1 say you've rolled GOODBYE

user_plays = input('\nEnter \'-yes\' to play Or \'-no\' to quit: ').lower()
score = 0
plays = 0
while plays != 20:
	if user_plays == "yes":
		user_choice = int(input("Enter \n1- Snake game\n2-Box game\n3-Bounce game\n:"))
		if user_choice == 1:
			ans = int(input(" 1 + 1 is ?"))
			if ans == 2:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 2:
			ans = int(input(" 1 + 2 is ?"))
			if ans == 3:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 3:
			ans = int(input(" 1 + 3 is ?"))
			if ans == 4:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 4:
			ans = int(input(" 1 + 4 is ?"))
			if ans == 5:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 5:
			ans = int(input(" 1 + 5 is ?"))
			if ans == 6:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 6:
			ans = int(input(" 1 + 6 is ?"))
			if ans == 7:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 7:
			ans = int(input(" 1 + 7 is ?"))
			if ans == 8:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 8:
			ans = int(input(" 1 + 8 is ?"))
			if ans == 9:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 9:
			ans = int(input(" 1 + 9 is ?"))
			if ans == 10:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 10:
			ans = int(input(" 1 + 10 is ?"))
			if ans == 11:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 11:
			ans = int(input(" 1 + 11 is ?"))
			if ans == 12:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 12:
			ans = int(input(" 1 + 12 is ?"))
			if ans == 13:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 13:
			ans = int(input(" 1 + 13 is ?"))
			if ans == 14:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 14:
			ans = int(input(" 1 + 14 is ?"))
			if ans == 15:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 15:
			ans = int(input(" 1 + 15 is ?"))
			if ans == 16:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 16:
			ans = int(input(" 1 + 16 is ?"))
			if ans == 17:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 17:
			ans = int(input(" 1 + 17 is ?"))
			if ans == 18:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 18:
			ans = int(input(" 1 + 18 is ?"))
			if ans == 19:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		elif user_choice == 19:
			ans = int(input(" 1 + 19 is ?"))
			if ans == 20:
				print("Correct!")
				score +=1
			else:
				print("Failed")
			plays += 1
		# else:
		# 	print("\nLET'S BOUNCE")
		# 	user_roll = input("\nType\n1- To ROLL\nQUIT- TO QUIT\n:").lower()
		# 	if user_roll == "1":
		# 		print("\nYOU'VE ROLLED")
		# 	else:
		# 		print("\nYOU QUIT")
		# 	plays += 1
	else:
		print("\nTHANK YOU FOR COMING")

# hidden_number = 12
# user_play = int(input("\nGuess my hidden number: "))
# while user_play != hidden_number :
# 	if user_play < 0:
# 		print("Don't be negative. Be positive, But")
# 	elif user_play <= 11:
# 		print("You're almost there, but")
# 	elif user_play < 20:
# 		print("You're going too far brr, and ")
# 	else:
# 		print("Dey play! Just dey play. I'm sure you're ManU fan.\n")
# 	print("You're locked in my infinite loop sha\nTry Again!\n")
# 	user_play = int(input())

# print("Wow! You're now free ;-)\n")






































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