
import sys
import millionairedb2
import random
import time

class player:
	"""class player defines player attributes that will be tracked throughout the game"""
	def __init__(self, name):

		self.balance = ['0', '100', '200', '300', '500', '1,000', '2,000', '4,000', '8,000', '16,000', '32,000', '64,000', '125,000', '250,000', '500,000', '1,000,000']
		self.name = name


	def moneyMade(self, mLvl):
		"""Tracks money made by the player"""
		self.curMoney = self.balance[mLvl]
		if self.curMoney == '1,000,000':
			print("\nCONGRATULATIONS " + self.name + "!!!!!!! You have won $1,000,000!!!!!! YOU ARE NOW A MILLIONAIRE!")
			return False
		else:
			print("\nCongratulations! You answered correctly! Currently, you have $"+ str(self.curMoney) + '!\n')
			return True

	def walkAway(self, mLvl):
		"""if user selects to walk away"""
		self.curMoney = self.balance[mLvl]
		print("\nCongratulations! You are walking away with $" + str(self.curMoney) +"!\n")

	def playMore(self):
		"""this method is text that is sent to the player"""
		self.curMoney = self.balance[mLvl]
		self.decision = input("Did you want to continue with the game and play for $" + str(self.balance[mLvl+1]) + " (Y/N)? ")
		self.decision = self.decision.lower()

		while self.decision not in ['y','n']:
			self.decision = input("You did not enter a valid character. Please enter 'Y' to continue or 'N' to exit: ")
			self.decision = self.decision.lower()

		if self.decision == 'y':
			print("\nAlright " + self.name + "! Let's continue to play WHO WANTS TO BE A MILLIONAIRE!")
			print("Remember if you get one question wrong, you walk away with nothing!")
			print("****************This question is for $" + str(self.balance[mLvl+1]) + "!********************\n")
			return True

		elif self.decision == 'n':
			print('\nCongratulations! You are walking away with $' + str(self.curMoney) + "\n")
			return False

		elif self.decision == 'walk':
			print("\nCongratulations! You are walking away with $"+ str(self.curMoney) + "\n")
			return False


	def check_50(self):
		"""Check to see if 50/50 is still available"""
		global check50
		check50 += 1
		if check50 != 1:
			return False
		else:
			return True


	def check_Audience(self):
		"""check to see if poll the audience is still availble"""
		global checkAudience
		checkAudience += 1
		if checkAudience != 1:
			return False
		else:
			return True


	def check_Friend(self):
		"""check to see if phone a friend is still available"""
		global checkFriend
		checkFriend += 1
		if checkFriend != 1:
			return False
		else:
			return True


class intro:
	"""introduction with the rules to the player"""

	def __init__(self, name):
		self.name = name

	def welcome(self):
		print("***********************************************")
		print("                 Welcome To                    ")
		print("         Who Wants to be a Millionaire!        ")
		print("*********************************************** \n")
		print("Welcome " + self.name +"! Please take the time to read the rules carefully: \n ")

	def rules(self):
		"""rules to display for the player"""

		print("*There will be 15 questions that are arranged by difficulty.")
		print("*Simplier questions go first and are worth less.")
		print("*Every question will have four answer choices, of which only one is correct.")
		print("*Answering the hardest, 15th question, will make you a winner of $1,000,000!")
		print("*IF YOU GET A QUESTION WRONG, YOU WILL LOSE ALL YOUR MONEY!")
		print("*You have the option to walk away when you see the question and keep your money.")
		print("*To walk away, simply type 'walk' when you are prompted to answer.")
		print("*If you need to see the rules again, type 'help' when prompted to answer.")
		print("*If you want to see all the commands you can use, type 'commands' when prompted to answer.\n")

		print("You will also have 3 life lines that can only be used once:")
		print("1. 50/50. To activate this, type '50' to activate this life line.")
		print("2. Phone a friend. Type 'friend' in order to activate this life line.")
		print("3. Ask the audience. Type 'audience' to activate this life line.\n")
		print("Life lines can only be activated when you are prompted for an answer.\n")


	def commands(self):
		"""Commands to let the player know what they can use"""

		print("\nThe following commands are only applicable when answering a question in the game:")
		print("'exit' - to exit the game")
		print("'walk' - to walk away with your money")
		print("'help' - to see the rules again")
		print("'a,b,c,or d' - to answer the question")
		print("'50' - to use 50/50 life line and eliminate two answers")
		print("'audience' - life line to have audience help you")
		print("'friend' - to use phone a friend life line")




class lifeline:
	"""Life line class"""
	def __init__(self):
		Questions.__init__(self, mLvl)
		self.line_50 = True

	def wait(self, phrase, t):
	  """ Implements a pause with dots, to make it a little more realistic"""
	  print("\n\n %s" % phrase)
	  sys.stdout.flush()
	  for i in range(t):
	    print(".", end = ' ')
	    time.sleep(1)
	    sys.stdout.flush()


	def fifty(self):
		"""50/50 lifeline"""
		if self.line_50 == True:
			self.line_50 = False
			self.removedAns = 0 # To track how many answers have been removed
			while True:
				if self.removedAns == 2:
					break
				i = int(random.random()*4 + 1)
				if self.correct_ans != self.db[i] and self.db[i] != "":
					self.removedAns += 1
					self.db[i] = ""

			print("\nTwo incorrect answers have been eliminated. The two remaining are:")
			temp = [" A. ", " B. ", " C. ", " D. "]
			for i in range(1,5):
				if self.db[i] != "":
					print(temp[i-1] + self.db[i] + "\t\t")


	def audience(self):
		"""Poll the audience lifeline"""
		self.w = random.random()

		if self.w > 0.50: # Just a number for the "majority" of the audience
			self.w = int(self.w * 100)
			self.audience_answer = self.correct_ans
		else:
			self.w = 1 - self.w
			self.w = int(self.w * 100)
			self.audience_answer = self.correct_ans

		self.wait("The audience is voting", 3)
		print("\nThe majority, {}%, of the audience think that the correct answer is '{}'.\n".format(self.w, self.audience_answer))

	def friend(self):
		"""phone a friend lifeline"""
		if random.random() < 0.7: #provides an arbitrary percentage to display uncertainty in the print
			self.wait("Calling your friend", 2)
			print("\n Your friend thinks the correct answer is '{}'.".format(self.correct_ans))

		else:
			self.wait("Calling your friend", 2)
			print("\n Your friend is not sure but thinks the correct answer is '{}'.".format(self.correct_ans))


class Questions:
	"""a class jsut to pull in the Questions and define all variables"""
	def __init__(self, mLvl):
		self.mLvl = mLvl
		self.db = millionairedb2.get_question(mLvl)
		self.question = self.db[0]
		self.ans_a = self.db[1]
		self.ans_b = self.db[2]
		self.ans_c = self.db[3]
		self.ans_d = self.db[4]
		self.correct_ans = self.db[5]
		self.ans_h = 'help'
		self.exit = 'exit'
		self.walk = 'walk'
		self.fifty = '50'
		self.audience = 'audience'
		self.friend = 'friend'
		self.commands = 'commands'
		self.key = {"a": self.ans_a, "b": self.ans_b, "c": self.ans_c, "d": self.ans_d, "exit": self.exit, "walk": self.walk}
		self.useful = {"help": self.ans_h, "audience": self.audience, "friend": self.friend, "50": self.fifty, "commands": self.commands}

class gameMechanics(Questions, intro, player, lifeline):
	"""Controls the entire flow of the game"""
	def __init__(self):
		Questions.__init__(self, mLvl)
		intro.__init__(self, name)
		player.__init__(self, name)
		lifeline.__init__(self)


	def displayQuest(self):
		"""Displays the question and answer choices"""
		print("{} \n".format(self.question))
		self.listAns = "A. " + self.ans_a + "\t\t B. " + self.ans_b
		self.listAns += "\nC. " + self.ans_c + "\t\t D. " + self.ans_d
		print(self.listAns)
		#print("{}".format(self.listAns))

	def getAnswer(self):
		"""This will get the answer from the user and make sure it is valid according to the rules"""
		self.ans = input('What is your answer, {}? '.format(self.name))
		self.ans = self.ans.lower()

		while self.ans not in list(self.key.keys()):
			"""This logic is to make sure the answer provided form the user is valid and controlled"""

			if self.ans == 'help':
				intro.rules(self)
				self.ans = input('\nNow that you know the rules, what will be your answer? ')
				self.ans = self.ans.lower()

			elif self.ans == 'commands':
				intro.commands(self)
				self.ans = input('\nNow you know the commands, what will your answer be? ')
				self.ans = self.ans.lower()

			elif self.ans == 'exit':
				return False

			elif self.ans =='walk':

				player.walkAway(self, self.mLvl)

			elif self.ans == '50':

				if player.check_50(self) == True:
					lifeline.fifty(self)
					self.ans = input('You have used 50/50, what will your answer choice be? ')
					self.ans = self.ans.lower()
				else:
					self.ans = input('You have used 50/50 already, please select another answer choice: ')
					self.ans = self.ans.lower()

			elif self.ans == 'audience':

				if player.check_Audience(self) == True:
					lifeline.audience(self)
					self.ans = input('You have used your Ask the Audience lifeline, what will your answer choice be? ')
					self.ans = self.ans.lower()
				else:
					self.ans = input('You have already used Ask the Audience, please select another answer choice: ')
					self.ans = self.ans.lower()

			elif self.ans == 'friend':

				if player.check_Friend(self) == True:
					lifeline.friend(self)
					self.ans = input('You have used your Ask the Audience lifeline, what will your answer choice be? ')
					self.ans = self.ans.lower()
				else:
					self.ans = input('You have already used Ask the Audience, please select another answer choice: ')
					self.ans = self.ans.lower()

			else:
				self.ans = input("Your answer choice is not valid. Please enter A, B, C, or D as your answer? ")
				self.ans = self.ans.lower()


	def check_answer(self):
		"""This method checks the answer provided from the user and will determine to move forward or not"""

		if self.key[self.ans] == self.correct_ans:
			print("Good Job!")
			return True

		elif self.ans == 'help':
			intro.rules(self)

		elif self.ans == 'exit':
			return False

		elif self.ans == 'commands':
			intro.commands(self)

		elif self.ans == 'walk':
			player.walkAway(self, self.mLvl)

		else:
			print("\nBetter luck Next time! The correct answer was " + self.correct_ans)
			return False

#---------
if __name__ == "__main__":
	"""Script for the code"""
	mLvl = 0
	check50 = 0
	checkAudience = 0
	checkFriend = 0

	name = input("\nBefore we begin, what is your name: ")
	i = intro(name)
	p = player(name)
	i.welcome()
	i.rules()

	if p.playMore() == True:
		qBank = Questions(mLvl)
		gameMech = gameMechanics()
		gameMech.displayQuest()
		gameMech.getAnswer()

		while gameMech.check_answer() == True:
			mLvl += 1
			if p.moneyMade(mLvl) == True:
				if p.playMore() == False:
					break
				else:
					qBank = Questions(mLvl)
					gameMech = gameMechanics()
					gameMech.displayQuest()
					gameMech.getAnswer()
			else:
				print("\nThank you for playing! Have a great day!\n")
				break
		else:
			print("\nThank you for playing! Have a great day!\n")
