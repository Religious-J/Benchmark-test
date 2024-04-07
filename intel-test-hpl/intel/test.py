import os
from tqdm import tqdm    
class MPIRun:
    def __init__(self,Ns,NB,P,Q):
        self.Ns = Ns
        self.NB = NB
        self.P = P
        self.Q = Q
        self.HPLDAT = '''HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out      output file name (if any)
6            device out (6=stdout,7=stderr,file)
1            # of problems sizes (N)
%d           Ns
1            # of NBs
%d           NBs
0            PMAP process mapping (0=Row-,1=Column-major)
1            # of process grids (P x Q)
%d       Ps
%d       Qs
16.0         threshold
3            # of panel fact
0 1 2        PFACTs (0=left, 1=Crout, 2=Right)
2            # of recursive stopping criterium
2 4          NBMINs (>= 1)
1            # of panels in recursion
2            NDIVs
3            # of recursive panel fact.
0 1 2        RFACTs (0=left, 1=Crout, 2=Right)
1            # of broadcast
0            BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1            # of lookahead depth
0            DEPTHs (>=0)
2            SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0            L1 in (0=transposed,1=no-transposed) form
0            U  in (0=transposed,1=no-transposed) form
1            Equilibration (0=no,1=yes)
8            memory alignment in double (> 0)'''%(Ns,NB,P,Q)
    
    def run(self):
        HPLDAT_FILE = open("./HPL.dat","w",encoding="utf-8")
        HPLDAT_FILE.write(self.HPLDAT)
        HPLDAT_FILE.close()
        # cmd = "mpirun -np %d ./xhpl > %d-%d-%d-%d.txt"%(self.P*self.Q,self.Ns,self.NB,self.P,self.Q)
        cmd = "mpirun -np %d ./xhpl > result.txt" % (P * Q)
        # cmd = "mpirun -np %d ./xhpl"
        print("\r",cmd,end="",flush=True)
        os.system(cmd)


if __name__=="__main__":
    script_deal = open("./script.txt","r",encoding="utf-8")
    lines = script_deal.readlines()
    # print(lines)

    for line in tqdm(lines):
        # runlist = [int(i) for i in filter(None, line.split(" "))]
        runlist = [int(i) for i in line.split(" ")]
        Ns,NB,P,Q = runlist[0],runlist[1],runlist[2],runlist[3]
        mpirun = MPIRun(Ns,NB,P,Q)
        mpirun.run()

