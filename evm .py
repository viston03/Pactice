import sys

def vote (voting_list, ballot_list, num):
 
    if num == 1:
        voting_list.append("TDP") 
        print("Voted for TDP")
    elif num == 2:
        voting_list.append("YSRCP") 
        print("Voted for YSRCP")
    elif num == 3:
        voting_list.append ("BJP")
        print("Voted for BJP")
    elif num == 4:
        voting_list.append ("Congress")
        print("Voted for Congress")
    elif num == 5:
        voting_list.append ("JANASENA")
        print("Voted for JANASENA") 
    elif num == 6:
        voting_list.append ("NOTA")
        print("Voted for NOTA")
    elif num == 7:
        sys.exit()
    else:
        print("input not given")


def vote_d (voting_list, ballot_list, num):
 
    if num == 1:
        voting_list.append("BJP") 
        print("Voted for TDP")
    elif num == 2:
        voting_list.append("BJP") 
        print("Voted for YSRCP")
    elif num == 3:
        voting_list.append ("BPJ")
        print("Voted for BJP")
    elif num == 4:
        voting_list.append ("BJP")
        print("Voted for Congress")
    elif num == 5:
        voting_list.append ("BJP")
        print("Voted for JANASENA") 
    elif num == 6:
        voting_list.append ("BJP")
        print("Voted for NOTA")
    elif num == 7:
        sys.exit()
    else:
        print("input not given")


voting_list = []
ballot_list = []
for i in range(5):
	b = input("Enter ballot number: ")
	if b in ballot_list:
		print("You have already voted")
	else:
		print("1. TDP")
		print("2. YSRCP")
		print("3. BJP")
		print("4. Congress")
		print("5. Janasena")
		print("6. NOTA")
		print("7. Exit")
		num = int(input("Press button whom you want to vote: "))
		ballot_list.append(b)
		if i>4:
			vote(voting_list, ballot_list, num)
		else:
			vote_d(voting_list, ballot_list, num)
print(voting_list)




















