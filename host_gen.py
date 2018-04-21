hosts = [
["csel-kh1200-%s.cselabs.umn.edu", 19],
["csel-kh1250-%s.cselabs.umn.edu", 37],
["kh4240-%s.cselabs.umn.edu", 10],
["csel-kh4250-%s.cselabs.umn.edu", 49],
["csel-lind40-%s.cselabs.umn.edu", 43]]

prefix = "ssh -t pidap004@"
postfix = " screen \"python3 portfolio-selection-research/algorithms/generalized_test.py\""
outfile = open("hostlist.txt", 'w')
list_of_hosts = []

for host in hosts:
	for i in range(1,host[1]+1):
		list_of_hosts.append(prefix+(host[0] % str(i).zfill(2))+postfix)


outfile.write("\n".join(list_of_hosts))