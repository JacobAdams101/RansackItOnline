##################################################
# RansackIt
#
# Written by Jacob Adams 
##################################################



##################################################
# Module imports
##################################################

import random


def roll_dice(n):
    if n < 1:
        raise ValueError("Number of sides must be at least 1")
    return random.randint(1, n)

def vs_sequence(attacker=[], defender_sequence=[[]], max_compare_length=2):
    defender_empty = True
    for d in defender_sequence:
        if len(d) != 0:
            defender_empty = False
            break
    if len(attacker)==0 and defender_empty:
        return "DRAW"
    elif len(attacker)==0:
        return "DEFENDERWIN"
    elif defender_empty:
        return "ATTACKERWIN"
    
    
    defender = defender_sequence[0]

    attackerrolls=[(roll_dice(n), n) for n in attacker]
    defenderrolls=[(roll_dice(n), n) for n in defender]

    attackerrolls = sorted(attackerrolls, key=lambda x: x[0], reverse=True)
    defenderrolls = sorted(defenderrolls, key=lambda x: x[0], reverse=True)

    #print("ROLLS")
    #print(attackerrolls)
    #print(defenderrolls)

    COMPARE_LEN = min([len(attacker), len(defender), max_compare_length])

    for i in range(COMPARE_LEN):
        if attackerrolls[i][0] > defenderrolls[i][0]:
            for j, n in enumerate(defender):
                if n == defenderrolls[i][1]:
                    del defender[j]
                    break
        else:
            for j, n in enumerate(attacker):
                if n == attackerrolls[i][1]:
                    del attacker[j]
                    break

    if len(defender) == 0: #If no more defenders switch to next attack
        return vs_sequence(attacker, defender_sequence[1:], max_compare_length=max_compare_length)
    else:
        return vs_sequence(attacker, defender_sequence, max_compare_length=max_compare_length)


#PLayer 1 
def vs(attacker=[], defender=[], defender2=[], max_compare_length=2):
    if len(attacker)==0 and len(defender)==0 and len(defender2)==0:
        return "DRAW"
    elif len(attacker)==0:
        return "DEFENDERWIN"
    elif len(defender)==0 and len(defender2) ==0:
        return "ATTACKERWIN"
    
    
     
    attackerrolls=[(roll_dice(n), n) for n in attacker]
    defenderrolls=[(roll_dice(n), n) for n in defender]

    attackerrolls = sorted(attackerrolls, key=lambda x: x[0], reverse=True)
    defenderrolls = sorted(defenderrolls, key=lambda x: x[0], reverse=True)

    COMPARE_LEN = min([len(attacker), len(defender), max_compare_length])

    for i in range(COMPARE_LEN):
        if attackerrolls[i][0] > defenderrolls[i][0]:
            for j, n in enumerate(defender):
                if n == defenderrolls[i][1]:
                    del defender[j]
                    break
        else:
            for j, n in enumerate(attacker):
                if n == attackerrolls[i][1]:
                    del attacker[j]
                    break

    if len(defender) == 0: #If no more defenders switch to second attack
        return vs(attacker, defender2, [], max_compare_length=max_compare_length)
    else:
        return vs(attacker, defender, defender2, max_compare_length=max_compare_length)

def compute_prob_sequence(attacker=[], defender=[[]], runs=100000):
    attacker_win = 0
    defender_win = 0
    for _ in range(runs):
        attacker_copy = attacker.copy()

        defender_copy = [d.copy() for d in defender]
        result = vs_sequence(attacker_copy, defender_copy)
        if result == "ATTACKERWIN":
            attacker_win += 1
        elif result == "DEFENDERWIN":
            defender_win += 1
    
    return attacker_win/runs, defender_win/runs

def compute_prob(attacker=[], defender=[], defender2=[], runs=100000):
    attacker_win = 0
    defender_win = 0
    for _ in range(runs):
        attacker_copy = attacker.copy()
        defender_copy = defender.copy()
        defender2_copy = defender2.copy()
        result = vs(attacker_copy, defender_copy, defender2_copy)
        if result == "ATTACKERWIN":
            attacker_win += 1
        elif result == "DEFENDERWIN":
            defender_win += 1
    
    return attacker_win/runs, defender_win/runs