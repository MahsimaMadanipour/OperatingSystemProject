Project #1: CPU Scheduling Simulator

Project’s Objectives:
	You will write a program to implement a simulator with different scheduling algorithms. The
	simulator selects a task to run from ready queue based on the scheduling algorithm. Since the
	project intends to simulate a CPU scheduler, so it does not require any actual process creation
	or execution. When a task is scheduled, the simulator will simply print out what task is
	selected to run at a time.

Design Hints:
	The simulator first reads task information from input file and stores all data in a data
	structure. Then it starts simulating one scheduling algorithm in a time-driven manner. At each
	time unit (or slot), it adds any newly arrived task(s) into the ready queue and calls a specific
	scheduler algorithm in order to select appropriate task from ready queue. When a task is
	chosen to run, the simulator prints out a message indicating what process ID is chosen to
	execute for this time slot. If no task is running (i.e., empty ready queue), it is considered
	“idle”. Before advancing to the next time unit, the simulator should update all necessary
	changes in task and ready queue status.

Required Algorithms:
	- FCFS
	- Round Robin (q= 1, 4, 8)
	- SPN
	- SRT
	- HRRN
	- Feedback (q= 1, 4, 8)

Inputs:
	- Number of processes (tasks)
	- Arrival time of each process
	- Service time of each process (𝑇s)

Outputs:
	- Finish time of each process for each algorithm
	- Turnaround time of each process (𝑇r = Tf - Ta) for each algorithm
	- Waiting time of each process (𝑇w = Tr - Ts) for each algorithm
	- The average of mentioned values for each algorithm 