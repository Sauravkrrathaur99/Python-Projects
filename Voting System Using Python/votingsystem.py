nominee_1 = input("Enter the name of the 1st Nominee : ")
nominee_2 = input("Enter the name of the 2nd Nominee : ")
nm1_vote = 0
nm2_vote = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_of_voters = len(voter_id)
while True:
    if voter_id == []:
        print("Votting Session is over !!")
        if nm1_vote > nm2_vote:
            percent = (nm1_vote / no_of_voters) * 100
            print(nominee_1, "has won the election with ", percent, "% of votes")
            break
        elif nm2_vote > nm1_vote:
            percent = (nm2_vote / no_of_voters) * 100
            print(nominee_2, "has won the election with ", percent, "% votes")
            break
        else:
            print("Both have equal number of votes !!! Government will decide who will rule")
            break

    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are a voter ")
        voter_id.remove((voter))
        print("---------------------------------------")
        print("To give vote to ", nominee_1, "Press 1 ")
        print("To give vote to ", nominee_2, "Press 2 ")
        print("---------------------------------------")
        vote = int(input("Enter your precious vote : "))
        if vote == 1:
            nm1_vote += 1
            print(nominee_1, "Thanks you to give your important vote to them !!")
        elif vote == 2:
            nm2_vote += 1
            print(nominee_2, "Thanks you to give your important vote to them !!")
        elif vote > 2:
            print("Check your pressed key !!")
        else:
            print("You are not a voter OR You have already voted !!")
