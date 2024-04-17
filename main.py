import math
import queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  # TO DO - modify to account for insertions, deletions and substitutions
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      #insert_cost = 1 + MED(S, T[1:])
      #delete_cost = 1 + MED(S[1:], T)  # Deletion
      #substitute_cost = 1 + MED(S[1:], T[1:])  # Substitution

      # Choose the minimum cost among the three operations
      #return min(insert_cost, delete_cost, substitute_cost)
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  #MED = {}
  #insertion_cost = 1
  #deletion_cost = 1
  #substitution_cost = 1

  # Helper function to calculate the minimum edit distance
  #def med_helper(i, j):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    return len(T)

  elif T == "":
    return len(S)
  elif S[0] == T[0]:
    result = fast_MED(S[1:], T[1:], MED)
  else:
    insert_cost = fast_MED(S, T[1:], MED)
    delete_cost = fast_MED(S[1:], T, MED)
    #substitute_cost = 1 + fast_MED(S[1:], T[1:], MED)
    result = 1 + min(insert_cost, delete_cost)
    MED[(S, T)] = result
  return result


def fast_align_MED(S, T, MED={}):
  # if MED == {}:
  #   MED = {}
  if (S, T) in MED:
    return MED[(S, T)]
  elif S == "":
    MED[(S, T)] = ("-" * len(T), T)
    return MED[(S, T)]
  elif T == "":
    MED[(S, T)] = (S, "-" * len(S))
    return MED[(S, T)]
  else:
    if S[0] == T[0]:
      alignS, alignT = fast_align_MED(S[1:], T[1:], MED)
      MED[(S, T)] = (S[0] + alignS, T[0] + alignT)
    else:
      insert_alignS, insert_alignT = fast_align_MED(S, T[1:], MED)
      delete_alignS, delete_alignT = fast_align_MED(S[1:], T, MED)

      insert_cost = 1 + len(insert_alignS)
      delete_cost = 1 + len(delete_alignS)

      if insert_cost <= delete_cost:
        MED[(S, T)] = ("-" + insert_alignS, T[0] + insert_alignT)
      else:
        MED[(S, T)] = (S[0] + delete_alignS, "-" + delete_alignT)

    # MED[(S, T)] = result
    return MED[(S, T)]


test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]


def test_MED():
  for S, T in test_cases:
    print(fast_MED(S, T) == MED(S, T))


test_MED()


def test_align():
  for i in range(len(test_cases)):
    S, T = test_cases[i]
    align_S, align_T = fast_align_MED(S, T)
    print(align_S == alignments[i][0] and align_T == alignments[i][1])


test_align()
