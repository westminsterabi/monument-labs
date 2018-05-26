import time
import subprocess

commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]


# extend subprocess class to make getting start time a little neater
class TimedSubprocess(subprocess.Popen):
    def __init__(self, cmd):
        subprocess.Popen.__init__(self, cmd, shell=True, stdout=subprocess.PIPE)
        self.start_time = time.time()

    def start_time(self):
        return self.start_time


# this array will hold the run times of the processes
times = []


for command in commands:
    p = TimedSubprocess(command)
    p.wait()
    time_delta = (time.time() - p.start_time)
    times.append(time_delta)

# print report
print(f'Maximum time: {max(times)} \n Minimum time: {min(times)} \n Average time: {sum(times)/len(times)}')

