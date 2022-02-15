class RoundRobin():
    def __init__(self, process_num, processes_list, quantum_t):
        self.processes_number = process_num
        self.processes = processes_list
        self.quantum = quantum_t
        self.time = 0
        self.context_switch = 0

    def running_algorithm(self):
        service_times = [[process.name, process.service_time] for process in self.processes]

        self.processes.sort(key = lambda p: p.arrival_time)
        processes_temp_list = [[process, process.name, process.arrival_time, process.service_time] for process in self.processes]

        last_process = None
        while True:
            turn_processes = [process for process in processes_temp_list if (process[2] <= self.time and process[3] != 0)]
            if len(turn_processes):                    
                for turn_process in turn_processes:
                    if len(turn_processes) == 1 and turn_process == last_process:
                        if turn_process[3] > self.quantum:
                            print("--> Running Process: {}".format(turn_process[1]))
                            self.time += self.quantum
                            turn_process[3] -= self.quantum
                            self.time += self.context_switch
                            last_process = turn_process
                        elif turn_process[3] <= self.quantum:
                            print("--> Running Process: {}".format(turn_process[1]))
                            self.time += turn_process[3]
                            turn_process[3] = 0
                            turn_process[0].finish_time = self.time
                            turn_process[0].calculate_turnaround_time()
                            turn_process[0].calculate_wating_time()
                            print("{} Turnaround Time: {}".format(turn_process[1], turn_process[0].turnaround_time))
                            print("{} Waiting Time: {}".format(turn_process[1], turn_process[0].waiting_time))
                            self.time += self.context_switch
                            last_process = turn_process
                        break
                    if turn_process != last_process:
                        if turn_process[3] > self.quantum:
                            print("--> Running Process: {}".format(turn_process[1]))
                            self.time += self.quantum
                            turn_process[3] -= self.quantum
                            self.time += self.context_switch
                            last_process = turn_process
                        elif turn_process[3] <= self.quantum:
                            print("--> Running Process: {}".format(turn_process[1]))
                            self.time += turn_process[3]
                            turn_process[3] = 0
                            turn_process[0].finish_time = self.time
                            turn_process[0].calculate_turnaround_time()
                            turn_process[0].calculate_wating_time()
                            print("{} Turnaround Time: {}".format(turn_process[1], turn_process[0].turnaround_time))
                            print("{} Waiting Time: {}".format(turn_process[1], turn_process[0].waiting_time))
                            self.time += self.context_switch
                            last_process = turn_process
                        break
            else:
                break
            
        print("--> Finishing Time:",self.time)