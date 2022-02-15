"""
Project #1: CPU Scheduling Simulator

A program to implement a simulator with different scheduling algorithms. The simulator selects a task to run from ready queue based 
on the scheduling algorithm. Since the project intends to simulate a CPU scheduler, so it does not require any actual process creation
or execution. When a task is scheduled, the simulator will simply print out what task is selected to run at a time. 
"""
from process import Process
from first_come_first_served import FirstComeFirstServed
from round_robin import RoundRobin
from shortest_process_next import ShortestProcessNext
from shortest_remaining_time import ShortestRemainingTime
from highest_response_ratio_next import HighestResponseRatioNext
from feedback import Feedback

def creating_objects_list(lines, the_list):
    for p in lines:
        p_name, p_arrival_time, p_service_time = p[:-1].split(", ")
        the_list.append(Process(p_name, int(p_arrival_time), int(p_service_time)))

def waiting_times_average(processes, processes_num):
    return (sum([process.waiting_time for process in processes]) / processes_num)

def turnaround_times_average(processes, processes_num):
    return (sum([process.turnaround_time for process in processes]) / processes_num)

with open('CPU Scheduling Simulator/Text Files/input_processes.txt') as input_file:
    raw_lines = input_file.readlines()

raw_processes = []
creating_objects_list(raw_lines, raw_processes)

menu_controller = True
while menu_controller:
    print("Project #1: CPU Scheduling Simulator")
    print("0. First Come First Served")
    print("1. Round Robin")
    print("2. Shortest Process Next")
    print("3. Shortest Remaining Time")
    print("4. Highest Response Ratio Next")
    print("5. Feedback")
    print("-1. Exit")
    option = int(input("Choose The Algorithm: "))

    if option >= 0:
        if option == 0:
            print("-------------------------------------")
            print("\nFirst Come First Served:")
            fcfs_processes = []
            creating_objects_list(raw_lines, fcfs_processes)
            fcfs_scheduling = FirstComeFirstServed(len(fcfs_processes), fcfs_processes)
            fcfs_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(fcfs_processes, len(fcfs_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(fcfs_processes, len(fcfs_processes))))
            print("-------------------------------------\n")
        elif option == 1:
            print("-------------------------------------")
            print("\nRound Robin:")
            rr_processes = []
            creating_objects_list(raw_lines, rr_processes)
            quantum_t = int(input("Choose Quantum Time (1, 4, 8): "))
            rr_scheduling = RoundRobin(len(rr_processes), rr_processes, quantum_t)
            rr_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(rr_processes, len(rr_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(rr_processes, len(rr_processes))))
            print("-------------------------------------\n")
        elif option == 2:
            print("-------------------------------------")
            print("\nShortest Process Next:")
            spn_processes = []
            creating_objects_list(raw_lines, spn_processes)
            spn_scheduling = ShortestProcessNext(len(spn_processes), spn_processes)
            spn_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(spn_processes, len(spn_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(spn_processes, len(spn_processes))))
            print("-------------------------------------\n")
        elif option == 3:
            print("-------------------------------------")
            print("\nShortest Remaining Time:")
            srt_processes = []
            creating_objects_list(raw_lines, srt_processes)
            srt_scheduling = ShortestRemainingTime(len(srt_processes), srt_processes)
            srt_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(srt_processes, len(srt_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(srt_processes, len(srt_processes))))
            print("-------------------------------------\n")
        elif option == 4:
            print("-------------------------------------")
            print("\nHighest Response Ratio Next:")
            hrrn_processes = []
            creating_objects_list(raw_lines, hrrn_processes)
            hrrn_scheduling = HighestResponseRatioNext(len(hrrn_processes), hrrn_processes)
            hrrn_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(hrrn_processes, len(hrrn_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(hrrn_processes, len(hrrn_processes))))
            print("-------------------------------------\n")
        elif option == 5:
            print("-------------------------------------")
            print("\nFeedback(1, 4, 8):")
            f_processes = []
            creating_objects_list(raw_lines, f_processes)
            f_scheduling = Feedback(len(f_processes), f_processes, 1, 4, 8)
            f_scheduling.running_algorithm()
            print("\nResult:")
            print("Turnaround Times Average: {}".format(turnaround_times_average(f_processes, len(f_processes))))
            print("Waiting Times Average: {}".format(waiting_times_average(f_processes, len(f_processes))))
            print("-------------------------------------\n")
    else:
        menu_controller = False
        print("Farewell ^-^")