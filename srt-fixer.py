import sys
import re
import argparse



regex = r'([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9]) --> ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9])'
rexp = re.compile(regex)

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()



with open(args.fname,'r+',newline='') as ifp:	
	for line in ifp:

		t = rexp.search(line)	
		
		
		if t is not None:
			
			LH = int(t.group(1))	
			LM = int(t.group(2)) 		
			LS = int(t.group(3))	
			LMs = int(t.group(4))
			
			RH = int(t.group(5))
			RM = int(t.group(6)) 
			RS = int(t.group(7))
			RMs = int(t.group(8))

			NewLH = LH
			NewLM = LM
			NewLS = LS + int(args.offset)
			NewLMs = LMs 
			
			NewRH = RH
			NewRM = RM 
			NewRS = RS + int(args.offset)
			NewRMs = RMs

			ms = args.offset - int(args.offset)
			s = args.offset - ms
			NewLS = NewLS+s
			NewRS = NewRS+s
			NewLMs = int(LMs + (ms*1000))
			NewRMs = int(RMs + (ms*1000))

			if NewLMs > 999:
				NewLMs = NewLMs -1000
				NewLS = NewLS + 1
			if NewRMs > 999:
				NewRMs = NewRMs -1000
				NewRS = NewRS + 1		
			if NewLS > 59:
				NewLS = NewLS - 60
				NewLM = NewLM + 1 
			if NewRS > 59:
				NewRS = NewRS - 60
				NewRM = NewRM + 1 

			NewLH = str(NewLH).zfill(2)  
			NewLM = str(NewLM).zfill(2)	
			NewLS = str(NewLS).zfill(2)
			NewLMs = str(NewLMs).zfill(2) 
			
			NewRH = str(NewRH).zfill(2)
			NewRM = str(NewRM).zfill(2) 
			NewRS = str(NewRS).zfill(2)
			NewRMs = str(NewRMs).zfill(3)
			
			ps = "%s:%s:%s,%s --> %s:%s:%s,%s\n"%(NewLH, NewLM, NewLS, NewLMs, NewRH, NewRM, NewRS, NewRMs)
			sys.stdout.write(ps)			
		else:
			sys.stdout.write(line)

		
ifp.close() 







