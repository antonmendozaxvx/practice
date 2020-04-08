import os
#define function
def get_results(data):

    # define variables
    vote_count = 0
    votes = []
    vote_errors = 0
    candidate_count = []
    Candidates = []
    percent = []

    #start loop
    for row in data:
        
        row = row[0].split('\t')
        #total number of votes
        vote_count +=1


        #append names to the candidates list
        # google error handlijng (specifically try catch equivalent in python)
        # if python throws an error list index out of range, use row[0]
            #if index out of range again skip function and  add one to vote errors
        if row[2] in Candidates():
            Candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        #make a list of all votes
        votes.append(row[2])

    # start a loop to populate the candidate count with each vote
    for candidate in Candidates:
        candidate_count.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/vote_count*100,3))

    #fine winner using index positioning of the max count in candidate_count
    winner = Candidates[candidate_count.index(max(candidate_count))]

    #print results, use a loop for the number of unique candidates
    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {vote_count}')
    print('------------------------')
    for i in range(len(Candidates)):
        print(f'{Candidates[i]}: {percent[i]}% {candidate_count[i]}')
    print('------------------------')
    print(f'Winner: {winner}')
    print('------------------------')

    #set exit path
    poll_output = os.path.join("PyPollResults.txt")

    #write out results to text file
    with open(poll_output, "w'") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------')
        txtfile.write(f'\nTotal Votes: {vote_count}')
        txtfile.write('\n------------------------')
        for i in range (len(Candidates)):
            txtfile.write(f'\n{Candidates[i]}: {percent[i]}% {candidate_count[i]}')
        txtfile.write('\n------------------------')
        txtfile.write(f'\nWinner" {winner}')
        txtfile.write('\n------------------------')