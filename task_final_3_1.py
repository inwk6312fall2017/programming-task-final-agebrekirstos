
def replace_config():
    """this function replaces the ip addresses starting with 172 with 192"""
    #with open (filename) as f:
    fin = open("running-config.cfg")
    fout = open("running-config-new.cfg", "w+")

    ip_1 = '172'
    ip_2 = '192'
    for line in fin:
        # fout.write(line)
        fout.write(line.replace(ip_1, ip_2))

    fout.close()
    fin.close()

def acl_dict():
	fin = open("running-config.cfg")
	d = dict()

	config_line = iter(fin)
	first = "access-list "
	end = "extended"

	for line in fin:
		if line.startswith(first):
			#acl_1 = line.replace(first,"")

			acl = line.replace(first,"")
			d[acl] = d.get(acl, 0) + 1
	return d

#replace_config()
print(acl_dict())
