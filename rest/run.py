from eve import Eve
import platform
import os
from flask import request

import re
app = Eve()

@app.route('/proc')

def proc():
	my_path=request.args.get('path')
	proc_name=platform.processor()
	uname=platform.uname()
	
	# sys=platform.system()
	print 'path',my_path
	mem_info=open('/proc/meminfo').read()
	matched=re.search(r'^MemTotal:\s+(\d+)',mem_info)
	if matched:
		RAM=round(float(matched.groups()[0])/ 1048576,2)
	# print "ram",RAM
	sys_info={}
	sys_info['system']=uname[0]
	sys_info['Machine']=uname[1]
	st = os.statvfs(my_path)
	free = (st.f_bavail * st.f_frsize)/ 1048576
	total = (st.f_blocks * st.f_frsize) / 1048576
	used = ((st.f_blocks - st.f_bfree) * st.f_frsize) / 1048576

	# return "system: " + "".join(sys_info['system'])+ "Machine: " + "".join(sys_info['Machine'])
	return "Processor Name: "+str(proc_name)+"<br />"+"RAM: "+str(RAM)+" GB "+"<br />"+"freeDisk: "+str(free)+" MB "+"<br />"+"totalDisk: "+str(total)+" MB "+"<br />"+"UsedDisk: " +str(used)+" MB "





if __name__ == '__main__':
    app.run(host="127.0.0.1",port=int(5000))
