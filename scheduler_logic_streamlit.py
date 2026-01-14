"""
Scheduling Algorithm Logic for Streamlit App
Simplified and optimized for better integration with Streamlit
"""

def calculate_fcfs(processes):
    """
    First Come First Serve Scheduling
    Args: processes - list of [process_id, arrival_time, burst_time]
    Returns: (gantt_data, metrics)
    """
    processes = sorted(processes, key=lambda x: x[1])  # Sort by arrival time
    gantt_data = []
    current_time = 0
    process_details = []
    
    for proc_id, arrival, burst in processes:
        # Handle idle time
        if current_time < arrival:
            gantt_data.append([0, current_time, arrival])
            current_time = arrival
        
        start_time = current_time
        completion_time = start_time + burst
        
        gantt_data.append([proc_id, start_time, completion_time])
        
        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = start_time - arrival
        
        process_details.append({
            'process_id': proc_id,
            'completion_time': completion_time,
            'turnaround_time': turnaround_time,
            'waiting_time': waiting_time,
            'response_time': response_time
        })
        
        current_time = completion_time
    
    # Calculate averages
    avg_waiting = sum(p['waiting_time'] for p in process_details) / len(process_details)
    avg_turnaround = sum(p['turnaround_time'] for p in process_details) / len(process_details)
    avg_response = sum(p['response_time'] for p in process_details) / len(process_details)
    
    metrics = {
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround,
        'avg_response_time': avg_response,
        'process_details': process_details
    }
    
    return gantt_data, metrics


def calculate_sjf_non_preemptive(processes):
    """
    Shortest Job First (Non-Preemptive) Scheduling
    """
    processes = [[p[0], p[1], p[2]] for p in processes]  # Make a copy
    gantt_data = []
    current_time = 0
    process_details = []
    completed = 0
    n = len(processes)
    is_completed = [False] * n
    first_response = [None] * n
    
    while completed < n:
        # Find processes that have arrived and not completed
        available = []
        for i, (proc_id, arrival, burst) in enumerate(processes):
            if arrival <= current_time and not is_completed[i]:
                available.append((i, proc_id, arrival, burst))
        
        if not available:
            # No process available, add idle time
            next_arrival = min([p[1] for i, p in enumerate(processes) if not is_completed[i]])
            gantt_data.append([0, current_time, next_arrival])
            current_time = next_arrival
            continue
        
        # Select process with shortest burst time
        selected = min(available, key=lambda x: x[3])
        idx, proc_id, arrival, burst = selected
        
        start_time = current_time
        completion_time = start_time + burst
        
        if first_response[idx] is None:
            first_response[idx] = start_time
        
        gantt_data.append([proc_id, start_time, completion_time])
        
        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        response_time = first_response[idx] - arrival
        
        process_details.append({
            'process_id': proc_id,
            'completion_time': completion_time,
            'turnaround_time': turnaround_time,
            'waiting_time': waiting_time,
            'response_time': response_time
        })
        
        is_completed[idx] = True
        completed += 1
        current_time = completion_time
    
    # Calculate averages
    avg_waiting = sum(p['waiting_time'] for p in process_details) / len(process_details)
    avg_turnaround = sum(p['turnaround_time'] for p in process_details) / len(process_details)
    avg_response = sum(p['response_time'] for p in process_details) / len(process_details)
    
    metrics = {
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround,
        'avg_response_time': avg_response,
        'process_details': process_details
    }
    
    return gantt_data, metrics


def calculate_sjf_preemptive(processes):
    """
    Shortest Job First (Preemptive/SRTF) Scheduling
    """
    processes = [[p[0], p[1], p[2], p[2]] for p in processes]  # Add remaining time
    gantt_data = []
    current_time = 0
    completed = 0
    n = len(processes)
    process_details = [None] * n
    first_response = [None] * n
    last_process = None
    segment_start = 0
    
    # Find maximum completion time
    max_time = sum(p[2] for p in processes) + max(p[1] for p in processes)
    
    while completed < n and current_time < max_time:
        # Find available processes with remaining time > 0
        available = []
        for i, (proc_id, arrival, burst, remaining) in enumerate(processes):
            if arrival <= current_time and remaining > 0:
                available.append((i, proc_id, arrival, burst, remaining))
        
        if not available:
            # Add idle time if we have a previous segment
            if last_process is not None and last_process != 0:
                gantt_data.append([last_process, segment_start, current_time])
            gantt_data.append([0, current_time, current_time + 1])
            segment_start = current_time + 1
            last_process = 0
            current_time += 1
            continue
        
        # Select process with shortest remaining time
        selected = min(available, key=lambda x: x[4])
        idx, proc_id, arrival, burst, remaining = selected
        
        # Record first response time
        if first_response[idx] is None:
            first_response[idx] = current_time
        
        # If process changed, save previous segment
        if last_process is not None and last_process != proc_id:
            gantt_data.append([last_process, segment_start, current_time])
            segment_start = current_time
        elif last_process is None:
            segment_start = current_time
        
        # Execute for 1 time unit
        processes[idx][3] -= 1
        current_time += 1
        last_process = proc_id
        
        # Check if process completed
        if processes[idx][3] == 0:
            gantt_data.append([proc_id, segment_start, current_time])
            segment_start = current_time
            
            completion_time = current_time
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = first_response[idx] - arrival
            
            process_details[idx] = {
                'process_id': proc_id,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time,
                'response_time': response_time
            }
            
            completed += 1
            last_process = None
    
    # Add final segment if exists
    if last_process is not None and last_process != 0:
        gantt_data.append([last_process, segment_start, current_time])
    
    # Merge consecutive segments of same process
    merged_gantt = []
    for proc_id, start, end in gantt_data:
        if merged_gantt and merged_gantt[-1][0] == proc_id:
            merged_gantt[-1][2] = end
        else:
            merged_gantt.append([proc_id, start, end])
    
    # Calculate averages
    avg_waiting = sum(p['waiting_time'] for p in process_details) / len(process_details)
    avg_turnaround = sum(p['turnaround_time'] for p in process_details) / len(process_details)
    avg_response = sum(p['response_time'] for p in process_details) / len(process_details)
    
    metrics = {
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround,
        'avg_response_time': avg_response,
        'process_details': process_details
    }
    
    return merged_gantt, metrics


def calculate_round_robin(processes, time_quantum):
    """
    Round Robin Scheduling
    """
    from collections import deque
    
    processes = [[p[0], p[1], p[2], p[2]] for p in processes]  # Add remaining time
    gantt_data = []
    current_time = 0
    ready_queue = deque()
    process_details = [None] * len(processes)
    first_response = [None] * len(processes)
    completed = 0
    n = len(processes)
    last_arrival_check = -1
    in_queue = [False] * n
    
    # Sort by arrival time initially
    processes_sorted = sorted(enumerate(processes), key=lambda x: x[1][1])
    
    while completed < n:
        # Add newly arrived processes to ready queue
        for i, (proc_id, arrival, burst, remaining) in processes_sorted:
            if arrival <= current_time and arrival > last_arrival_check and remaining > 0 and not in_queue[i]:
                ready_queue.append(i)
                in_queue[i] = True
        last_arrival_check = current_time
        
        if not ready_queue:
            # No process in queue, move to next arrival
            next_arrivals = [p[1][1] for p in processes_sorted if p[1][3] > 0 and p[1][1] > current_time]
            if next_arrivals:
                gantt_data.append([0, current_time, min(next_arrivals)])
                current_time = min(next_arrivals)
            else:
                break
            continue
        
        idx = ready_queue.popleft()
        in_queue[idx] = False
        proc_id, arrival, burst, remaining = processes[idx]
        
        # Record first response
        if first_response[idx] is None:
            first_response[idx] = current_time
        
        # Execute for time quantum or remaining time, whichever is smaller
        exec_time = min(time_quantum, remaining)
        start_time = current_time
        current_time += exec_time
        processes[idx][3] -= exec_time
        
        gantt_data.append([proc_id, start_time, current_time])
        
        # Add newly arrived processes before re-adding current process
        for i, (p_id, arr, bur, rem) in processes_sorted:
            if arr <= current_time and arr > last_arrival_check and rem > 0 and not in_queue[i]:
                ready_queue.append(i)
                in_queue[i] = True
        last_arrival_check = current_time
        
        # Check if process completed
        if processes[idx][3] == 0:
            completion_time = current_time
            turnaround_time = completion_time - arrival
            waiting_time = turnaround_time - burst
            response_time = first_response[idx] - arrival
            
            process_details[idx] = {
                'process_id': proc_id,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time,
                'response_time': response_time
            }
            completed += 1
        else:
            # Add back to queue
            ready_queue.append(idx)
            in_queue[idx] = True
    
    # Calculate averages
    avg_waiting = sum(p['waiting_time'] for p in process_details) / len(process_details)
    avg_turnaround = sum(p['turnaround_time'] for p in process_details) / len(process_details)
    avg_response = sum(p['response_time'] for p in process_details) / len(process_details)
    
    metrics = {
        'avg_waiting_time': avg_waiting,
        'avg_turnaround_time': avg_turnaround,
        'avg_response_time': avg_response,
        'process_details': process_details
    }
    
    return gantt_data, metrics
