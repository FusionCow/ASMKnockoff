prgm_counter=0
prgm_len=0
register_a = 0
register_c = 0
register_v = 0
register_b = 0

addrlist={}

def returnAddr(addr):
  return(addrlist[addr])

def setAddr(addr,content):
  addrlist[addr]=content

def compare(val1,val2,type):
  match type:
    case ">":
      if(val1>val2):
        return 0
      else:
        return 1
    case "<":
      if(val1<val2):
        return 0
      else:
        return 1
    case ">=":
      if(val1>=val2):
        return 0
      else:
        return 1
    case "<=":
      if(val1<=val2):
        return 0
      else:
        return 1
    case "==":
      if(val1==val2):
        return 0
      else:
        return 1