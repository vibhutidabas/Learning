with open('input.txt', 'r') as f1:
    inp=f1.readlines()                   #reading the input file
with open('instructions.txt','r') as f2:
    opc=f2.readlines()                   #reading opcode file
symtab=[]
optab=[]
errtab=[]
def onepass(lc):
    ln=0                                #line number
    while ln!=len(inp):                 #till input file is fully read
        line=inp[ln]                    #each line in the input.txt
        line=line[:len(line)-1]
        if '#' in line:                 #if line has a comment
            line=line.split('#')[0]
            line=line.strip()
            if len(line)==0:
                ln+=1
                continue
        if ':' in line:                 #if it has a symbol
            symtab.append(line.split(':')[0])#add the symbol in sym. table
            line=line.split(': ')[1]     #now check the rest of the line
    
        op=line
        if(ln==len(inp)-1):                 #end of file
            if(op!='STP'):                  #stp missing 
                errtab.append([ln,": End statement missing"])
        
        z=line[:3]
        if z is not None:
            optab.append(z[:3])
        else:
            errtab.append([ln,": Opcode not recognised"])

        ln+=1
        lc+=1

onepass(0)
if len(errtab)==0:
    print("opcode table")
    print(optab)
    print("symbol table")
    print(symtab)
else:
    print("error table")
    print(errtab)
    