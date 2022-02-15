class HighestResponseRatioNext():
    def __init__(self, process_num, processes_list):
        self.processes_number = process_num
        self.processes = processes_list
        self.time = 0
        self.context_switch = 0

    def running_algorithm(self):
        while True:
            if min(self.processes, key = lambda p : p.arrival_time).arrival_time > self.time:
                self.time = min(self.processes, key = lambda p : p.arrival_time).arrival_time
            arrived_processes = [process for process in self.processes if process.finish_time == 0 and process.arrival_time <= self.time]
            if len(arrived_processes):
                highest_ratio_process = arrived_processes[0]
                highest_ratio = (((self.time - highest_ratio_process.arrival_time) + highest_ratio_process.service_time) / highest_ratio_process.service_time)
                for p in arrived_processes:
                    temp_highest_ratio = (((self.time - p.arrival_time) + p.service_time) / p.service_time)
                    if temp_highest_ratio > highest_ratio:
                        highest_ratio_process = p
                print("--> Running Process: {}".format(highest_ratio_process.name))
                self.time += highest_ratio_process.service_time
                highest_ratio_process.finish_time = self.time
                highest_ratio_process.calculate_turnaround_time()
                highest_ratio_process.calculate_wating_time()
                print("{} Turnaround Time: {}".format(highest_ratio_process.name, highest_ratio_process.turnaround_time))
                print("{} Waiting Time: {}".format(highest_ratio_process.name, highest_ratio_process.waiting_time))
                self.time += self.context_switch
            else:
                break

        print("--> Finishing Time:",self.time)