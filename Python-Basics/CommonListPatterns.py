#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
#code here
friends.extend(new_friend)
friends.sort()
print(friends)
# This was part of initial execise to fix 
#print(friends.sort() + new_friend)

#other solutions
#1. joinedfriends = sorted(friends + new_friends)
#   print(joinedfriends)
