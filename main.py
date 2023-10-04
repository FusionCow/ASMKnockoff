from run import runprgm

with open("prgm.txt","r") as f:
  inptest=f.read()

runprgm(inptest)