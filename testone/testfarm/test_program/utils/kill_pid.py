import os
class killPid:
    def kill_pid(self,port):
        pids = p.get_pid(port=port)
        for i in pids:
            cmd = 'kill -9 {}'.format(i)
            os.popen(cmd)
            print('kill掉 node', cmd)