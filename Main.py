import numpy as np

#Creating the Charizard/Moltlres Ex deck from Pokemon Pocket TCG
#Used the most recent deck list for it in Limitless TCG by Felipe R

#Creates the deck using an Array

deck = np.array(['Charmander'] *2 +['Charmeleon'] *2 +
                ['Charizard ex'] *2 + ['Moltres ex'] *2 +
                ['Professors Research'] *2 + ['Dawn'] +
                ['Leaf'] + ['Sabrina'] + ['2X Speed'] *2 +
                ['Poke Ball'] *2 + ['Pokemon Communication'] *2 +
                ['Giant Cape'])

#Number of times the simulation is run
trials = 1000
#Number of times moltres and charmander appear in starting hand
success_count = 0

#Creates a loop containing the events in the simulations
for _ in range(trials):
    #Shuffles the deck
    shuffled_deck = np.random.permutation(deck)

    #Since we are guaranteed at least one base Pokemon when drawing the first five cards
    #In the beginning of the match we need to filter out that card in the deck
    #Note our only base pokemons are Charmander and Moltres Ex

    #Find the index of the base cards in the shuffled deck
    given_base = np.where(np.isin(shuffled_deck, ['Charmander', 'Moltres ex']))[0]
    #Randomly chooses a base cards index from the indexes of the base cards
    given_index = np.random.choice(given_base)

    #Filters the deck by deleting the guaranteed base cards
    filtered_deck = np.delete(shuffled_deck, given_index)

     #Draws 4 cards in the deck, we are drawing 4 cards because 1 is already guaranteed and decided
    drawn_hand = np.random.choice(filtered_deck, 4, replace=False )
    #Add the index of the randomly chosen base card into the drawn hand
    starting_hand = np.append(drawn_hand, shuffled_deck[given_index])

    #Boolean expression to increment if Charmander and Moltres is in the starting hand
    if 'Charmander' in starting_hand and 'Moltres ex' in starting_hand:
        success_count += 1

# Number of successes divided by # of trials
results = success_count / trials
print(f'The chances of getting Charmander and Moltres in your starting hand is: {results:.4f}')

#Analysis: So after running a simulation of 1000 trials we get a result of 0.3750. We could calculate the average
#and get a more solid answer .We could just store each trial(i) in a array
#and take the mean() for that array. From the theoretical results both seem to have similar results ranging from 38%-41%











