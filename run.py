import instructions as inst
import address as addr

def splitcmd(cmd):
  splitc=cmd.split(" ")
  command = splitc[0]
  splitc.pop(0)
  args=splitc
  return(command,args)

def runcmd(com):
  icmd,iargs=splitcmd(com)
  inst.parsecmd(icmd,iargs)

def runprgm(prgm):
  prgm=prgm.split("\n")
  program=[]
  for x in prgm:
    if(not(x=="" or x[0]=="#")):
      program.append(x)
  addr.prgm_counter=0
  addr.prgm_len=len(program)
  while(True):
    if(addr.prgm_counter>=addr.prgm_len):
      break
    else:
      runcmd(program[addr.prgm_counter])
    addr.prgm_counter+=1