import random
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

#print(len(states_of_america))
states_index = random.randint(0, len(states_of_america))
#states_index = random.randint(0, 500)
#print(states_index)
print(str(states_index) + " - " + str(states_of_america[states_index]))
