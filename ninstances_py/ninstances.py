
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

def occLabels(datafilename):
    datafile=open("data/"+datafilename)

    instances=datafile.readline()
    datafile.readline()
    labels=datafile.readline()
    instances=int(instances.split()[1])
    labels=int(labels.split()[1])
	occurrences = [0]*labels

	for counter in range(instances):
		line = datafile.readline()
		aux=line.split(" ")
		for i in range(labels):
			occurrences[i]= occurrences[i]+int(aux[i+len(aux)-labels])

    datafile.close()
	return occurrences
