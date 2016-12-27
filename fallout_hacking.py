import time
import sys
import random
import gibberish_code
import generate_passwords

possible_passwords = generate_passwords.create_possible_pws()

password = possible_passwords[random.randrange(14)]
pw_len = len(password)


def erase_screen():
	print("\033c", end="")

def print_as_typing(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush() # defeat buffering
		time.sleep(random.random() * 0.12)

def print_by_letter(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush() # defeat buffering
		time.sleep(0.015)

def print_word_by_word(l):
	for i in range(len(l)-1):
		words = l[i].split()
		for j in words:
			word = j + " "
			sys.stdout.write(word)
			sys.stdout.flush() # defeat buffering
			time.sleep(0.02)
		print()

def intro():
	"""Prints the intro screen."""
	erase_screen()
	welcome = "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK"
	typing1 = "SET TERMINAL/INQUIRE"
	typing2 = "SET FILE/PROTECTION=OWNER:RWED ACCOUNTS.F"
	typing3 = "SET HALT RESTART/MAINT"
	typing4 = "RUN DEBUG/ACCOUNTS.F"
	text1 = "RIT-V300"
	text2 = "Initializing Robco Industries(TM) MF Boot Agent v2.3.0\nRETROS BIOS\nRBIOS-4.02.08.00 52EE5.E7.E8\nCopyright 2201-2203 Robco Ind.\nUppermem: 64 KB\nRoot (5A8)\nMaintenance Mode"
	print_by_letter(welcome)
	print()
	print(">", end="")
	time.sleep(1)
	print_as_typing(typing1)
	print()
	time.sleep(.5)
	print_by_letter(text1)
	print()
	print(">", end="")
	time.sleep(1)
	print_as_typing(typing2)
	print(">", end="")
	time.sleep(1)
	print_as_typing(typing3)
	print()
	time.sleep(1)
	print_by_letter(text2)
	print()
	print(">", end="")
	time.sleep(1)
	print_as_typing(typing4)
	time.sleep(1)

def correct_password(pw):
	return password == pw

def how_many_correct(pw):
	"""Given a password, counts how many letters in the same position 
	match the input."""
	count = 0
	input_len = len(pw)
	if pw_len >= input_len:
		for i in range(input_len):
			if pw[i] == password[i]:
				count += 1
	else:
		for i in range(pw_len):
			if pw[i] == password[i]:
				count += 1
	return count

def main_code():
	"""Generates the code with the possible passwords in it."""
	rand_i = random.randrange(21)

	rand_i2 = rand_i+18
			
	gib_code = gibberish_code.gibberish_code()
	gib_str = gibberish_code.add_words_to_gib_st(possible_passwords)
	
	lines = []
	
	for i in range(17):
		line = gib_code[rand_i+i] + " " + gib_str[i*12:i*12+12] + " " + gib_code[rand_i2+i-1] + " " + gib_str[i*12+204:i*12+216]
		lines.append(line)

	return lines

def print_code(l, length):
	for i in range(len(l)-length-1):
		print(l[i])

def f_print_pw_screen(attempts, code, length):
	erase_screen()
	line = str(attempts) + " ATTEMPT(S) LEFT: " + ("■ " * attempts)
	robco_line = "ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL"
	print_by_letter(robco_line)
	print_by_letter("ENTER PASSWORD NOW")
	print()
	print_by_letter(line)
	print()
	print_word_by_word(code)
	

def re_print_pw_screen(attempts, code, length):
	erase_screen()
	line = str(attempts) + " ATTEMPT(S) LEFT: " + ("■  " * attempts)
	print("ROBCO INDUSTRIES (TM) TERMLINK PROTOCOL")
	if attempts <= 1:
		print("!!! WARNING: LOCKOUT IMMINENT !!!")
	else:
		print("ENTER PASSWORD NOW")
	print()
	print(line)
	print()
	print_code(code, length)

def print_success(c):
	success = [">Exact match!", ">Please wait", ">while system", ">is accessed.", "", ">"]
	
	for i in c:
		if 11 <= c.index(i) < 16:
			print(i, success[c.index(i)-11])
		if c.index(i) == 16:
			print(i, success[c.index(i)-11], "\033[1A")
	
	time.sleep(3)
			

def print_failure(c):
	success = [">Entry denied", ">Lockout in", "progress.", "", ">"]
	
	for i in c:
		if 12 <= c.index(i) <= 16:
			print(i, success[c.index(i)-12])
	
	for i in range(30):
		print()
		time.sleep(.08)
	
	print("\033c")
	erase_screen()
	
	for i in range(9):
		print()

	print(" " * 19 + "TERMINAL LOCKED")
	print()
	print(" " * 11 + "PLEASE CONTACT AN ADMINISTRATOR")
	
	for i in range(10):
		print()
	time.sleep(3)

def pw_entering_screen():
	erase_screen()
	print_by_letter("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
	print()
	print("> ", end="")
	time.sleep(1)
	print_as_typing("LOGON ADMIN")
	print()
	time.sleep(.5)
	print_by_letter("ENTER PASSWORD NOW")
	print()
	print("> ", end="")
	time.sleep(1)
	print_as_typing("*" * pw_len)
	for i in range(14):
		print()
	time.sleep(2)

def print_data_screen():
	erase_screen()
	print_by_letter(" " * 6 + "ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM")
	print_by_letter(" " * 8 + "COPYRIGHT 2075-2077 ROBCO INDUSTRIES")
	print(" " * 20, "-Server 6-")
	print()
	print_by_letter("Welcome, Overseer.")
	print_by_letter("__________________")
	print()
	print_by_letter("> View Security Dossiers")
	print()
	print_by_letter("> View Scouting Reports")
	print()
	print_by_letter("> Vault-Tec Instructions")
	print()
	print_by_letter("> Open Overseer's Tunnel")
	for i in range(7):
		print()
	input(">")
	
	

def main():
	intro()
	attempts = 4
	code = main_code()
	length = 1
	f_print_pw_screen(attempts, code, length)
	pw = input(code[16] + " >").upper()
	
	while not correct_password(pw):
		attempts -= 1
		length += 3
		if attempts == 3:
			re_print_pw_screen(attempts, code, length)
			print(code[12] + " >" + pw)
			print(code[13] + " >Entry denied")
			print(code[14], " >", how_many_correct(pw), "/", pw_len, " correct.", sep="")
			print(code[15])
			pw3 = pw
			pwc3 = str(how_many_correct(pw3)) + "/" + str(pw_len) + " correct."
		elif attempts == 2:
			re_print_pw_screen(attempts, code, length)
			print(code[9] + " >" + pw3)
			print(code[10] + " >Entry denied")
			print(code[11] + " >" + pwc3)
			print(code[12] + " >" + pw)
			print(code[13] + " >Entry denied")
			print(code[14], " >", how_many_correct(pw.upper()), "/", pw_len, " correct.", sep="")
			print(code[15])
			pw2 = pw
			pwc2 = str(how_many_correct(pw2)) + "/" + str(pw_len) + " correct."
		elif attempts == 1:
			re_print_pw_screen(attempts, code, length)
			print(code[6] + " >" + pw3)
			print(code[7] + " >Entry denied")
			print(code[8] + " >" + pwc3)
			print(code[9] + " >" + pw2)
			print(code[10] + " >Entry denied")
			print(code[11] + " >" + pwc2)
			print(code[12] + " >" + pw)
			print(code[13] + " >Entry denied")
			print(code[14], " >", how_many_correct(pw), "/", pw_len, " correct.", sep="")
			print(code[15])
			pw1 = pw
			pwc1 = str(how_many_correct(pw1)) + "/" + str(pw_len) + " correct."
		elif attempts <= 0:
			break
		pw = input(code[16] + " >").upper()
	
	if correct_password(pw):
		length += 2
		if attempts == 4:
			length += 3
			re_print_pw_screen(attempts, code, length)
			print(code[10] + " >" + pw)
			print_success(code)
		elif attempts == 3:
			length += 3
			re_print_pw_screen(attempts, code, length)
			print(code[7] + " >" + pw3)
			print(code[8] + " >Entry denied")
			print(code[9] + " >" + pwc3)
			print(code[10] + " >" + pw)
			print_success(code)
		elif attempts == 2:
			length += 3
			re_print_pw_screen(attempts, code, length)
			print(code[4] + " >" + pw3)
			print(code[5] + " >Entry denied")
			print(code[6] + " >" + pwc3)
			print(code[7] + " >" + pw2)
			print(code[8] + " >Entry denied")
			print(code[9] + " >" + pwc2)
			print(code[10] + " >" + pw)
			print_success(code)
		elif attempts == 1:
			length += 3
			re_print_pw_screen(attempts, code, length)
			print(code[1] + " >" + pw3)
			print(code[2] + " >Entry denied")
			print(code[3] + " >" + pwc3)
			print(code[4] + " >" + pw2)
			print(code[5] + " >Entry denied")
			print(code[6] + " >" + pwc2)
			print(code[7] + " >" + pw1)
			print(code[8] + " >Entry denied")
			print(code[9] + " >" + pwc1)
			print(code[10] + " >" + pw)
			print_success(code)
		pw_entering_screen()
		print_data_screen()
	if attempts <= 0:
		length += 1
		re_print_pw_screen(attempts, code, length)
		print(code[2] + " >" + pw3)
		print(code[3] + " >Entry denied")
		print(code[4] + " >" + pwc3)
		print(code[5] + " >" + pw2)
		print(code[6] + " >Entry denied")
		print(code[7] + " >" + pwc2)
		print(code[8] + " >" + pw1)
		print(code[9] + " >Entry denied")
		print(code[10] + " >" + pwc1)
		print(code[11] + " >" + pw)
		print_failure(code)	

main()
