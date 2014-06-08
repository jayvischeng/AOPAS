import re
def myfunction1(filepath, x_index=1, y_index=2, x=[], y=[]):
    #x.append(122222)

    with open(filepath)as f_in:
        for each_line in f_in:
            val=re.split(r"\t|,| *", each_line.strip())
            if '-' in val[0]:
                val.pop(0)
            if ':' in val[x_index-1] and val[x_index-1].count(":")==2:
                (hours, mins, secs)=val[x_index-1].split(':')
                val[x_index-1]=int(hours)+int(mins)/60.0+int(secs)/3600
            elif ':' in val[x_index-1] and val[x_index-1].count(":")==1:
                (hours, mins)=val[x_index-1].split(':')
                val[x_index-1]=int(hours)+int(mins)/60.0
            if ':' in val[y_index-1] and val[y_index-1].count(":")==2:
                (hours, mins, secs)=val[y_index-1].split(':')
                val[y_index-1]=int(hours)+int(mins)/60.0+int(secs)/3600
            elif ':' in val[y_index-1] and val[y_index-1].count(":")==1:
                (hours, mins)=val[y_index-1].split(':')
                val[y_index-1]=int(hours)+int(mins)/60.0
            x.append(float(val[x_index-1]))
            y.append(float(val[y_index-1]))
    #x=[]
    #print "myfunction"
    #print x
        
    
