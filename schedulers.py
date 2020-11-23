import sys
from bisect import insort

from des import SchedulerDES
from process import ProcessStates, Process
from event import Event, EventTypes
import math


class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):

        cur_process.process_state = ProcessStates.RUNNING
        actually_run_for = cur_process.run_for(quantum=self.quantum, cur_time=self.time)  # quantum=math.inf
        if cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_DONE)
        elif cur_process.remaining_time > 0:
            cur_process.process_state = ProcessStates.READY
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_REQ)
        self.processes[cur_process.process_id] = cur_process

        return new_event


class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        shortest_process = Process(process_id=sys.maxsize, service_time=math.inf,
                                   arrival_time=math.inf)
        for process in self.processes:
            if process.process_state == ProcessStates.READY:
                if process.service_time < shortest_process.service_time:
                    shortest_process = process
        return shortest_process

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        actually_run_for = cur_process.run_for(quantum=self.quantum, cur_time=self.time)  # quantum=math.inf
        if cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_DONE)
        elif cur_process.remaining_time > 0:
            cur_process.process_state = ProcessStates.READY
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_REQ)
        self.processes[cur_process.process_id] = cur_process

        return new_event


class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        actually_run_for = cur_process.run_for(quantum=self.quantum, cur_time=self.time)
        if cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_DONE)
        elif cur_process.remaining_time > 0:
            cur_process.process_state = ProcessStates.READY
            new_event = Event(process_id=cur_process.process_id, event_time=self.time + actually_run_for,
                              event_type=EventTypes.PROC_CPU_REQ)
        self.processes[cur_process.process_id] = cur_process

        return new_event


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        pass

    def dispatcher_func(self, cur_process):
        pass
