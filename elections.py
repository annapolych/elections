#!/usr/bin/env python

def printing_the_example():
	print ("Hello! Please insert the votes of the three parties and the invalid votes for each Station:") 

def insert_votes():
	for i in stations:
 		print ("Please insert the votes from %s:") %i
 		for party in parties:
 			if party=="Yellow":
 				vot_y=raw_input("For %s party:" %party)
 				# print (vot, type(vot))
 				# print (int(vot), type(int(vot)))
 				if isinstance(int(vot_y), int) == True:
	 				votes_y.append(int(vot_y))
	 			else:
	 				raise ValueError("Not an integer")
	 		
	 		if party=="Red":
 				vot_r=raw_input("For %s party:" %party)
 				# print (vot, type(vot))
 				# print (int(vot), type(int(vot)))
 				if isinstance(int(vot_r), int) == True:
	 				votes_r.append(int(vot_r))
	 			else:
	 				raise ValueError("Not an integer")
	 		
	 		if party=="Purple":
 				vot_p=raw_input("For %s party:" %party)
 				# print (vot, type(vot))
 				# print (int(vot), type(int(vot)))
 				if isinstance(int(vot_p), int) == True:
	 				votes_p.append(int(vot_p))
	 			else:
	 				raise ValueError("Not an integer")
	 		
	 		if party=="Invalid":
	 			vot_in=raw_input("Invalid votes:")
	 			if isinstance(int(vot_in), int) == True:
	 				votes_in.append(int(vot_in))
	 			else:
	 				raise ValueError("Not an integer")
	 				
	votes = votes_y + votes_r + votes_p + votes_in
	if check_number_of_votes(votes)==True:
		return sum(votes_y), sum(votes_r), sum(votes_p), sum(votes_in), sum(votes), len(votes)

def check_number_of_votes(votes_to_check):	
	if sum(votes_to_check)>23355:
		raise ValueError("Too many votes!")
	if sum(votes_to_check)<=23355:
		return True

def calculate_results(party_name, party_votes, all_votes):
	return party_name, round((float(party_votes)/float(all_votes))*100, 2)					

def finding_the_winner(output_from_insert_votes):
	if output_from_insert_votes.index(max(output_from_insert_votes[:4])) == 0:
		#print "Yellow"
		return "Yellow"
		
	if output_from_insert_votes.index(max(output_from_insert_votes[:4])) == 1:
		#print "Red"
		return "Red"

	if output_from_insert_votes.index(max(output_from_insert_votes[:4])) == 2:
		#print "Purple"
		return "Purple"

	if output_from_insert_votes.index(max(output_from_insert_votes[:4])) == 3:
		#print "Yellow"
		return "Invalid"
		
	else:
		raise ValueError("None is the winner! Please check for tie")
	

def printing_the_outcome(output_from_insert_votes, outcome_of_finding_the_winner):
	for party in parties:
		if party == "Yellow":
			yellow = calculate_results(party,output_from_insert_votes[0],output_from_insert_votes[4])
			continue
		if party == "Red":
			red = calculate_results(party,output_from_insert_votes[1],output_from_insert_votes[4])
			continue
		if party == "Purple":
			purple = calculate_results(party,output_from_insert_votes[2],output_from_insert_votes[4])
			continue
		if party == "Invalid":
			invalid = calculate_results(party,output_from_insert_votes[3], output_from_insert_votes[4])
		else:
			raise ValueError("Not a valid party")

	print ("|| ----------------------------- ||")
	print ("|| Party  || Votes || Percentage ||")
	print ("|| {} || {} || {}%     ||".format(yellow[0], output_from_insert_votes[0], yellow[1]))
	print ("|| {}    || {} || {}%     ||".format(red[0], output_from_insert_votes[1], red[1]))
	print ("|| {} || {} || {}%      ||".format(purple[0], output_from_insert_votes[2], purple[1]))
	print ("|| {} || {} || {}%      ||".format(invalid[0], output_from_insert_votes[3], invalid[1]))
	print ("|| ----------------------------- ||")
	print ("|| Total  || {} || {}%     ||".format((output_from_insert_votes[0] + output_from_insert_votes[1] + output_from_insert_votes[2] + output_from_insert_votes[2]), int((yellow[1] + red[1] + purple[1] + invalid[1]))))
	print ("|| ----------------------------- ||")
	print ("And the Winner is {}".format(outcome_of_finding_the_winner))
	
	return yellow, red, purple, invalid # is not used in any function so far

dhxfdhfhxfghxfghxfh

if __name__ == '__main__':
	#My paarameters,data etc.
	stations = ["Station1", "Station2", "Station3", "Station4", "Station5"]
	parties = ["Yellow", "Red", "Purple", "Invalid"]
	votes_y = []
	votes_r = []
	votes_p = []
	votes_in = []
	votes = []
	output_insert_votes = []
	
	#The program needs the folowing functions to be called 
	#The program needs the folowing functions to be run in that order

	printing_the_example() # the function prints out a Hello message and gives the format 
	output_insert_votes = insert_votes()
	winner=finding_the_winner(output_insert_votes)	
	printing_the_outcome(output_insert_votes, winner)