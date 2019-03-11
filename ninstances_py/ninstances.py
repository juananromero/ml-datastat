
def ninstances(datafilename):
    datafilename="data/"+datafilename
    datafile=open(datafilename)
    l1=datafile.readline()
    l2=datafile.readline()
    l3=datafile.readline()
    instances=int(l1.split()[1])
    features=int(l2.split()[1])
    labels=int(l3.split()[1])
    
    print("datafile: ", datafilename, "instances: ", instances, "features: ",
          features, "labels: ", labels, "\n")
    datafile.close()
    
def cardinality(datafilename):
    print ("Computing the cardinality of the chosen dataset...")
    datafilename="data/"+datafilename
    datafile=open(datafilename)
    l1=datafile.readline()
    l2=datafile.readline()
    l3=datafile.readline()
    instances=int(l1.split()[1])
    features=int(l2.split()[1])
    labels=int(l3.split()[1])
    l4=datafile.readline()

    avg=0

    while l4 != "":
   
     label=list(map(int, l4.split()[features:]))
     #print (label)
     avg+=sum(label)

     l4=datafile.readline()

    print ("Cardinality: ", avg/instances)

    datafile.close()
