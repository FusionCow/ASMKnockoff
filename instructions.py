import address as addr

def iprint(address):
  aout=str(addr.returnAddr(address))
  bout=aout.replace(".s"," ")
  print(bout,end="")


def parsecmd(cmd,args):
  match cmd:
    case "brk":
      addr.prgm_counter=addr.prgm_len
    case "prt":
      iprint(eval(args[0]))
    case "saa":
      addr.setAddr(eval(args[0]),addr.register_a)
    case "sab":
      addr.setAddr(eval(args[0]),addr.register_b)
    case "sav":
      addr.setAddr(eval(args[0]),addr.register_v)
    case "ada":
      addr.register_a=addr.returnAddr(eval(args[0]))
    case "adv":
      addr.register_v=addr.returnAddr(eval(args[0]))
    case "adb":
      addr.register_b=addr.returnAddr(eval(args[0]))
    case "sra":
      addr.register_a=eval(args[0])
    case "srv":
      addr.register_v=eval(args[0])
    case "srb":
      addr.register_b=eval(args[0])
    case "ica":
      addr.register_a+=eval(args[0])
    case "icv":
      addr.register_v+=eval(args[0])
    case "icb":
      addr.register_b+=eval(args[0])
    case "jmp":
      addr.prgm_counter=addr.returnAddr(eval(args[0]))-1
    case "jpp":
      addr.register_a=addr.prgm_counter+eval(args[0])
    case "jmc":
      if(addr.register_c==1):
        addr.prgm_counter=addr.returnAddr(eval(args[0]))-1
    case "cmp":
      addr.register_c=addr.compare(addr.register_b,addr.register_v,args[0])
    case "mul":
      addr.setAddr(eval(args[0]),addr.returnAddr(eval(args[0]))*addr.register_a)
    case "add":
      addr.setAddr(eval(args[0]),addr.returnAddr(eval(args[0]))+addr.register_a)
    case "sub":
      addr.setAddr(eval(args[0]),addr.returnAddr(eval(args[0]))-addr.register_a)
    case "div":
      addr.setAddr(eval(args[0]),addr.returnAddr(eval(args[0]))/addr.register_a)