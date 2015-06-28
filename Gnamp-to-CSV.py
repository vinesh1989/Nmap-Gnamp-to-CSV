__author__ = 'Vinesh Redkar'
__name__ = 'Gnmap to CSV Parser'
import os,sys

def nmaptocsv(CSVname,Outputfile):
    o = open(CSVname,"w") #open for append
    InputLocation="%s.txt"%Outputfile
    o.write("PORT,status,Protocol,service")
    for line in open(InputLocation):
        line.strip()
        line = line.replace("///, ","\n")
        line = line.replace("Host: ","\n")
        line = line.replace("	Ports: ","\n")
        line = line.replace("///","")
        line = line.replace("//", "/")
        line = line.replace("/",",")
       # line = line.replace("Host: ","\n")
        o.write('%s'%line)
        #o.write(line)
    o.close()
    
print "Author Name: Vinesh Redkar /n"
print "version 1.0 /n"
print "Convert Nmap Gnamp to CSV "
InputLocation = raw_input("Input File Name of gnmap file :\n")
Outputfile = raw_input("Output CSV File Name :\n")
os.system('type %s.gnmap | find "open" >%s.txt' %(InputLocation,Outputfile))
CSVname = os.path.join(Outputfile+".csv")
nmaptocsv(CSVname,Outputfile)
print "CSV File generation has been completed"
