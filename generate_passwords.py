from random import *
import sys
import time
import os

# Unfinished: For HARD difficulty.
twelve_letters_words = ["RESURRECTION", "ORGANIZATION", "INFILTRATION",
"SUBTERRANEAN", "TRANSMISSION", "TRANSCRIBING", "CONSTRUCTION", "QUARTERSTAFF",
"CIVILIZATION", "REPLENISHING", "HEADQUARTERS", "CONVERSATION", "PURIFICATION",
"RELATIONSHIP", "RECUPERATING", "IMMACULATELY", "ANTICIPATING", "CONSPIRATORS",
"DISAPPEARING", "BROADCASTING", "TECHNOLOGIES"]


def create_possible_pws():
	five_letter_words = ["WARNS", "TRACK", "GRASS", "GRADE", "BRINK", "BRIEF", 
	"DREAM", "TRAIN", "CRASH", "TRAPS", "PICKS", "TRACE", "FRANK", "GLEAM", 
	"AGILE", "LINES", "TIRES", "PILED", "BREAK", "VIPER", "MINDS", "CRUEL", 
	"LIVES", "ELDER", "BATON", "MINES", "VITAL", "STONE", "ALARM", "SWAMP", 
	"SHAVE", "HEARS", "STAYS", "SCOPE", "STORE", "STATE", "SLIPS", "SWORE", 
	"SHADY", "STARK", "CHAIR", "TIMES", "SCENE", "DISKS", "TILES", "TREES", 
	"SKIES", "DEEDS", "WIELD", "KEEPS", "FAILS", "SPEAR", "TRIES", "WAVES", 
	"SOUTH", "POSED", "WASTE", "SWORD", "WORLD", "ANKLE", "WOULD", "FORTH", 
	"COULD", "WRITE", "WORTH", "TOWEL", "SAVED", "WORKS", "AVOID", "ARMED", 
	"CLOUD", "FRIED", "GROUP", "TROOP", "DRIED", "PROUD", "CRIED", "TRIED", 
	"TIRED", "WRONG", "RUINS", "WHOLE", "GOODS", "BANDS", "TRITE", "LANDS", 
	"SANDS", "CROSS", "GOALS", "SEEMS", "BOOTH", "BONDS", "JOINS", "DAILY", 
	"RATES", "SAVES", "FIBER", "STILL", "MILES", "JONES", "PANEL", "SIZES", 
	"CIVIL", "MALES", "RIVAL", "WINDS", "LINED", "BRASS",]
	
	flw_len = len(five_letter_words)

	possible_pws = []
	
	for i in range(14):
		random_index = randrange(flw_len)

		while five_letter_words[random_index] in possible_pws:
			random_index = randrange(flw_len)

		possible_pws.append(five_letter_words[random_index])
		
	return possible_pws
