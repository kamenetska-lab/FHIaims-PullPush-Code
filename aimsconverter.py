import re
import sys
f = open("geometry.in", "w")
g = open("control.in", "w")

#n = len(sys.argv)

nmolecule = 26
nelectrodeL = 18
nLrelax = 4
nelectrodeR = 32
nRrelax = 4
InorOut = "Out"

#nmolecule = int(sys.argv[1])
#nelectrodeL = int(sys.argv[2])
#nLrelax = int(sys.argv[3])
#nelectrodeR = int(sys.argv[4])
#nRrelax = int(sys.argv[5])
#InorOut = sys.argv[6]

stepsize = float(0.05)
n_a = int(nmolecule + nelectrodeL)
n_b = int(nmolecule - 1)
n_c = int(nmolecule + nelectrodeL - 1)
n_d = int(nmolecule)
n_e = int(nmolecule + nLrelax - 1)
n_f = int(nmolecule + nelectrodeL + nRrelax - 1)
n_g = int(n_a - 3)
inoutvar = 0
testin = "In"
testout = "Out"
myxyzdata = []
mylines = []
mylinesb = []
mydata = []
mydatab = []
myseconddata = []
moveddata = []
titleline = []
linenum=0
startindex = 0
endindex = 0
itemnum = 0
ErrorFlag = False

if ( InorOut.find(testin) == -1  and InorOut.find(testout) == -1):
    quit()
if InorOut.find(testin) == -1:
    inoutvar = 2            # inoutvar = 2 if electrodes are moving out
else:
    inoutvar = 1            # inoutvar = 1 if electrodes are moving in
    
    

with open ("geometry.in.next_step", "rt") as myfile:
    for myline in myfile:
        linenum += 1
        mylines.append(myline.rstrip('\n'))
        substra = "# What follows is the current estimated Hessian matrix constructed by the BFGS algorithm."
        #print(myline)
        #linenum = len(myfile)-1
        if myline.find(substra) != -1:
            endindex = linenum-1
            #print(startindex)
        else:
            continue
    linenum = 0
    startindex = 4
    for myline in mylines:
        linenum += 1
        if (linenum > startindex and linenum < endindex):
            mydata.append(myline)
        else:
            continue
    
#    myxyzdata = mydata.copy()
#    itemnum = 0
#    flagvar = True
#    for item in mydata:
#        strn = mydata[itemnum]
#        #print(itemnum)
#        #print(strn)
#        if (itemnum < n_a and itemnum > n_b):
#            chunk = re.split(' +', strn)
#            chunk.pop(0)
#            flt = float(chunk[3])
#            if inoutvar == 1:
#                flt = flt + stepsize
#            else:
#                flt = flt - stepsize
#            flt = round(flt, 8)
#            strnn = str(flt)
#            chunk[3] = strnn
#            sp = '     '
#            sp = sp.join(chunk)
#            moveddata.append(sp)
#            itemnum += 1
#        elif (itemnum > n_c):
#            chunk = re.split(' +', strn)
#            chunk.pop(0)
#            flt = float(chunk[3])
#            if inoutvar == 1:
#                flt = flt - stepsize
#            else:
#                flt = flt + stepsize
#            flt = round(flt, 8)
#            strnn = str(flt)
#            chunk[3] = strnn
#            #print(type(chunk[3]))
#            #print(chunk)
#            sp = '     '
#            sp = sp.join(chunk)
#            #print(sp)
#            moveddata.append(sp)
#            itemnum += 1
#        else:
#            chunk = re.split(' +', strn)
#            chunk.pop(0)
#            flt = float(chunk[3])
#            flt = flt 
#            flt = round(flt, 8)
#            strnn = str(flt)
#            chunk[3] = strnn
#            sp = '     '
#            sp = sp.join(chunk)
#            moveddata.append(sp)
#            itemnum += 1
#            #print('\n')
#            #print(moveddata)    
#    linenum = len(moveddata)-1
#    #print(linenum)
#    flagvar = True
#    for item in reversed(moveddata):
#        #print(linenum)
#        auline = moveddata[linenum]
#        if auline.find('Au') == -1: 
#            flagvar = False
#        elif (linenum >= n_d and linenum <= n_e):
#            flagvar = False
#        elif (linenum >= n_a and linenum <= n_f):
#            flagvar = False
#        else:
#            liney = linenum+1
#            moveddata.insert(liney,'  constrain_relaxation .true.')
#            if linenum == n_g:
#                lineyb = linenum+2
#                moveddata.insert(lineyb,'  initial_moment 1.')
#            else:
#                flagvar = False
#        linenum-= 1
#    titleline.append("# opt: au ".rstrip('\n'))
#    titleline = titleline + moveddata
#    for item in titleline:
#        f.writelines("%s\n" % item)
#    f.close()
#
#    itemnum=0
#    for item in myxyzdata:
#        strxyz = myxyzdata[itemnum]
#        strxyznew = strxyz.replace("atom","")
#        myxyzdata[itemnum] = strxyznew
#        itemnum += 1
#
#    itemnum = 0
#    for item in myxyzdata:
#        strxyz = myxyzdata[itemnum]
#        elementa = "Fe"
#        elementb = "C"
#        elementc = "H"
#        elementd = "Au"
#        elemente = "Ru"
#        elementf = "N"
#        elementg = "Ag"
#        elementh = "V"
#        elementi = "O"
#
#
#        if strxyz.find(elementa) != -1:
#            strxyznew = "26" + strxyz
#            strxyznew = strxyznew.replace("Fe","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strnew)
#        elif strxyz.find(elementb) != -1:
#            strxyznew = "6" + strxyz
#            strxyznew = strxyznew.replace("C","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementc) != -1:
#            strxyznew = "1" + strxyz
#            strxyznew = strxyznew.replace("H","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementd) != -1:
#            strxyznew = "79" + strxyz
#            strxyznew = strxyznew.replace("Au","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementi) != -1:
#            strxyznew = "8" + strxyz
#            strxyznew = strxyznew.replace("O","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elemente) != -1:
#            strxyznew = "44" + strxyz
#            strxyznew = strxyznew.replace("Ru","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementf) != -1:
#            strxyznew = "7" + strxyz
#            strxyznew = strxyznew.replace("N","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementg) != -1:
#            strxyznew = "47" + strxyz
#            strxyznew = strxyznew.replace("Ag","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        elif strxyz.find(elementh) != -1:
#            strxyznew = "23" + strxyz
#            strxyznew = strxyznew.replace("V","")
#            myxyzdata[itemnum] = strxyznew
#            #print(strxyznew)
#        else:
#            #print(strxyz)
#            myxyzdata[itemnum] = strxyz
#        itemnum += 1
#    print(myxyzdata)
#    #del myxyzdata[0]                

    for item in mydata:
        f.writelines("%s\n" % item)
    f.close()
    
    linenum = 0
    with open ("controltemp.in", "rt") as myfileb:
        for mylineb in myfileb:
            linenum += 1
            mylinesb.append(mylineb.rstrip('\n'))
            substra = "#  KS_method	     lapack_fast"
            substrb = "  relax_geometry   bfgs 1.e-2"
            substrc = "#   output aitranss"
            if mylineb.find(substra) != -1:
                KSindex = linenum
                print(KSindex)
            elif mylineb.find(substrb) != -1:
                relaxindex = linenum
                print(relaxindex)
            elif mylineb.find(substrc) != -1: 
                aitranssindex = linenum
                print(aitranssindex)
            else:
                continue
        linenum = 0
        
        for mylineb in mylinesb:
            linenum += 1
            #print(mylineb)
            if (linenum == KSindex):
                mydatab.append("  KS_method	     lapack_fast")
            elif (linenum == relaxindex):
                mydatab.append("#  relax_geometry   bfgs 1.e-2")
            elif (linenum == aitranssindex):
                mydatab.append("   output aitranss")
            else:
                mydatab.append(mylineb)
        
        for item in mydatab:
            g.writelines("%s\n" % item)
        g.close()    


