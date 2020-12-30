# python template code for exercise ID GC (Computing GC Content)
# your code *must* define a function called run to work
#from operator import itemgetter
def run(fasta_str) :
# print(fasta_str)
 gc = 0
 at = 0
 l = []
 r = []
 count = 0
 for i in fasta_str:
  count += 1
  i = i.rstrip()
  if i.startswith( '>'):
   seq_ID = fasta_str[count: count+13]
   l.append(seq_ID)
   if (gc + at) > 0:
    leng = gc + at
    GCcont = float(gc)/float(leng) *100
    r.append(GCcont)
    gc = at = 0
  else:
   str_n = list(i.strip())
  #print(str_n)
   for j in str_n:
    if j == "G" or j == "C":
     gc += 1
    elif j == "A" or j == "T":
     at += 1
#get final gc appended
 leng = gc + at
 GCcont = float(gc)/float(leng) *100
 r.append(GCcont)
 gc = at = 0

# print(l)
# print(r)
 n  = r.index(max(r))
 print(l[n])
 print(max(r))

  # calculate the %GC content of each DNA sequence in the fasta records of fasta_str
  # fasta_str is a single string with each line separated by a newline character
  # retain the sequence name and gc content of the sequence with the highest %gc
  # print out the sequence name with the print function on its ownline
  # then print out the %GC of the sequence with the print function on the next line
