### This Code merges COG annotation files###
## Elham Karimi, Algarve uiversity, Faro, Portugal, September2017 ##
###Karimi.elh@gmail.com; ekarimi@ualg.pt;###

#fuctions
def read_line(ind, data_in): # read line with ind
    for line in data_in:
        cog, count, dsa, dsb, dsc = line.split('\t')
        if ind in cog:
            return [cog, count, dsa, dsb, dsc]

def write_header(file, no): # write header for output file
    file.write('#COG')
    file.write('\t')
    for i in range(1, no + 1):
        file.write('count' + str(i))
        file.write('\t')
    file.write('description') 
    file.write('\t')
    file.write('class')
    file.write('\t')
    file.write('class description')
    file.write('\n')  

def file_len(fname): # no of line in a file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return int(l[3:7])    

# main
import sys
no = int(sys.argv[1])
data_out = open('file_out.txt','w') 
data_out.truncate()		 
write_header(data_out, no);

no_list = []
for i in range(1, no + 1):
    no_list.append(file_len(str(i) + '.extension'))
no_max = max(no_list) + 1

for k in range(1, no_max):
    #print '{0:.2f}'.format(k/5662*100)
    ind = 'COG' + '{0:0=4d}'.format(k)
    
    # write COG
    flag = False 
    for i in range(1, no + 1):
        line = read_line(ind, open(str(i) + '.extension', 'r'))
        if line:
            if not flag:
                data_out.write(ind)
                data_out.write('\t')
            flag = True
        else:
            pass
     
    # write counts 
    if flag:
        for i in range(1, no + 1):
            line = read_line(ind, open(str(i) + '.extension', 'r'))
            #print(line)        
            if line:
                #print(1)
                data_out.write(line[1])
                data_out.write('\t')
            else:
                #print(2)
                data_out.write('0')
                data_out.write('\t')
            
    # write description
    flag = False 
    for i in range(1, no + 1):
        line = read_line(ind, open(str(i) + '.extension', 'r'))
        if line:
            if not flag:
                data_out.write(line[2]) 
                data_out.write('\t')
                data_out.write(line[3])
                data_out.write('\t')
                data_out.write(line[4])
            flag = True
        else:
            pass   

data_out.close()  

#########################################################











