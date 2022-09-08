#NO SCREW WITH DIS
import pickle
import time
import os
import random, sys
if len(sys.argv) - 1:
    random.seed(int(sys.argv[1]))

#######################################
loadingrepeat = 0
def loadingscreen(loadingrepeat):
  loading = "Loading"
  while loadingrepeat != 0:
    
    dottimer = 4
    while dottimer != 0:
      print(loading)
      time.sleep(1)
      loading += "."
      dottimer -= 1
      
    loadingrepeat -= 1
    loading = "Loading"

print("Would You like to play a game?")
answer = input(": ")
if answer in ["yes", "Yes", "No", "no"]:
  if answer in ["no", "No"]:
    print("goodbye then")
    exit()
  elif answer in ["yes", "Yes"]:
    print("Let us Continue...")
    loadingscreen(2)
  