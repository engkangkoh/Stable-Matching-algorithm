# Stable-Matching-algorithm
In this project, the Stable Matching algorithm, or more commonly know as the Gale-Shapley Algorithm was implemented.

The objective is to find a stable matching between two equally sized sets of elements given an ordering of preferences
for each element.
A matching is a bijection from the elements of one set to the elements of the other set.

A matching is only stable when:
Given n men and n women, where each person has ranked all members of the opposite sex in order of preference, marry the
men and women together such that there are no two people of opposite sex who would both rather have each other than
their current partners. When there are no such pairs of people, the set of marriages is deemed stable.

The following was stored:

1. unmarriedMen -- the list of currently unmarried men;

2. manSpouse -- the list of current spouses of all man;

3. womanSpouse -- the list of current spouses of all woman;

4. nextManChoice -- contains the number of proposals each man has made.

Men and Women's behaviour:

Men:
a. Proposals made according to their preference
b. Will not propose to a woman who rejected him
#partner will deprove (for the lack of a better 'word') in each iteration

Women:
a. Accept proposals if no partner, if partner higher up on the list available, change partner
#partner will only improve in each iteration
