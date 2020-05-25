def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Now "he" proposes to "she".
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice

        if currentHusband == None: #if no current husband
            manSpouse[he] = she
            womanSpouse[she] = he
            nextManChoice[he] += 1 #partner matched, cursor moved to next man
            del unmarriedMen[0] #delete first man off the unmarried man list
        else:
            index = herPreferences.index(currentHusband)
            his_index = herPreferences.index(he)

            if index > his_index:  # newmatch
                manSpouse[he] = she
                womanSpouse[she] = he
                nextManChoice[he] += 1
                del unmarriedMen[0]
                unmarriedMen.insert(0, currentHusband)
            else:
                nextManChoice[he] += 1

    # Note that if you don't update the unmarriedMen list,
    # then this algorithm will run forever.
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse

# You might want to test your implementation on the following two tests:
# assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
# assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])