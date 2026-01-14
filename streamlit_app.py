import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scheduler_logic_streamlit import (
    calculate_fcfs, calculate_sjf_non_preemptive, 
    calculate_sjf_preemptive, calculate_round_robin
)

# Page configuration
st.set_page_config(
    page_title="CPU Scheduling Simulator",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 15px;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    .process-input {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    h1, h2, h3 {
        color: white;
    }
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.95);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'num_processes' not in st.session_state:
    st.session_state.num_processes = 3

# Header
st.title("⚙️ CPU Process Scheduling Simulator")
st.markdown("### Visualize and compare different CPU scheduling algorithms")

# Sidebar for algorithm selection
with st.sidebar:
    st.header("⚙️ Configuration")
    
    algorithm = st.selectbox(
        "Select Scheduling Algorithm",
        ["FCFS (First Come First Serve)", 
         "SJF - Non-Preemptive (Shortest Job First)", 
         "SJF - Preemptive (Shortest Remaining Time First)",
         "Round Robin"],
        help="Choose the CPU scheduling algorithm to simulate"
    )
    
    # Time Quantum for Round Robin
    time_quantum = None
    if "Round Robin" in algorithm:
        time_quantum = st.number_input(
            "Time Quantum", 
            min_value=1, 
            max_value=10, 
            value=2,
            help="Time slice for Round Robin scheduling"
        )
    
    st.markdown("---")
    
    # Number of processes
    st.session_state.num_processes = st.slider(
        "Number of Processes", 
        min_value=3, 
        max_value=5, 
        value=st.session_state.num_processes,
        help="Select the number of processes to schedule"
    )
    
    st.markdown("---")
    
    # Color legend
    st.markdown("### 🎨 Process Colors")
    colors = {
        "Process 1": "#FF6B6B",
        "Process 2": "#4ECDC4",
        "Process 3": "#45B7D1",
        "Process 4": "#FFA07A",
        "Process 5": "#98D8C8"
    }
    for proc, color in list(colors.items())[:st.session_state.num_processes]:
        st.markdown(f'<div style="display: flex; align-items: center; margin: 5px 0;">'
                   f'<div style="width: 20px; height: 20px; background-color: {color}; '
                   f'border-radius: 3px; margin-right: 10px;"></div>'
                   f'<span>{proc}</span></div>', unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📋 Process Information")
    
    # Create a nice table layout for process inputs
    processes = []
    
    # Header row
    cols = st.columns([1, 2, 2, 2])
    cols[0].markdown("**Process**")
    cols[1].markdown("**Process ID**")
    cols[2].markdown("**Arrival Time**")
    cols[3].markdown("**Burst Time**")
    
    # Input rows for each process
    for i in range(st.session_state.num_processes):
        cols = st.columns([1, 2, 2, 2])
        
        with cols[0]:
            st.markdown(f"**P{i+1}**")
        
        with cols[1]:
            proc_id = st.number_input(
                f"ID {i+1}", 
                min_value=1, 
                max_value=5, 
                value=i+1, 
                key=f"proc_id_{i}",
                label_visibility="collapsed"
            )
        
        with cols[2]:
            arrival = st.number_input(
                f"Arrival {i+1}", 
                min_value=0, 
                max_value=100, 
                value=0, 
                key=f"arrival_{i}",
                label_visibility="collapsed"
            )
        
        with cols[3]:
            burst = st.number_input(
                f"Burst {i+1}", 
                min_value=1, 
                max_value=20, 
                value=5, 
                key=f"burst_{i}",
                label_visibility="collapsed"
            )
        
        processes.append([proc_id, arrival, burst])
    
    st.markdown("---")
    
    # Simulate button
    if st.button("🚀 Simulate Scheduling", use_container_width=True):
        with st.spinner("Simulating..."):
            # Call appropriate algorithm
            if "FCFS" in algorithm:
                result = calculate_fcfs(processes)
            elif "Non-Preemptive" in algorithm:
                result = calculate_sjf_non_preemptive(processes)
            elif "Preemptive" in algorithm:
                result = calculate_sjf_preemptive(processes)
            else:  # Round Robin
                result = calculate_round_robin(processes, time_quantum)
            
            if result:
                gantt_data, metrics = result
                
                # Create Gantt Chart
                st.markdown("### 📊 Gantt Chart")
                
                fig, ax = plt.subplots(figsize=(14, 4))
                fig.patch.set_facecolor('#f0f2f6')
                ax.set_facecolor('#ffffff')
                
                # Color map for processes
                color_map = {
                    1: '#FF6B6B',
                    2: '#4ECDC4',
                    3: '#45B7D1',
                    4: '#FFA07A',
                    5: '#98D8C8'
                }
                
                y_pos = 0
                max_time = 0
                
                for process_id, start, end in gantt_data:
                    if process_id == 0:  # Idle time
                        color = '#E0E0E0'
                        label = 'Idle'
                    else:
                        color = color_map.get(process_id, '#888888')
                        label = f'P{process_id}'
                    
                    duration = end - start
                    ax.barh(y_pos, duration, left=start, height=0.6, 
                           color=color, edgecolor='black', linewidth=1.5)
                    
                    # Add process label in the middle of the bar
                    mid_point = start + duration / 2
                    ax.text(mid_point, y_pos, label, ha='center', va='center', 
                           fontweight='bold', fontsize=12, color='white')
                    
                    # Add time labels
                    ax.text(start, -0.5, str(start), ha='center', fontsize=10)
                    max_time = max(max_time, end)
                
                # Add final time label
                ax.text(max_time, -0.5, str(max_time), ha='center', fontsize=10)
                
                ax.set_ylim(-1, 1)
                ax.set_xlim(0, max_time * 1.05)
                ax.set_yticks([])
                ax.set_xlabel('Time', fontsize=12, fontweight='bold')
                ax.set_title(f'{algorithm} - Gantt Chart', fontsize=14, fontweight='bold', pad=20)
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.spines['left'].set_visible(False)
                ax.grid(axis='x', alpha=0.3, linestyle='--')
                
                st.pyplot(fig)
                plt.close()
                
                # Display metrics
                st.markdown("### 📈 Performance Metrics")
                
                metric_cols = st.columns(3)
                
                with metric_cols[0]:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">⏱️ Avg Waiting Time</h3>
                            <h1 style="color: #333; margin: 10px 0;">{metrics['avg_waiting_time']:.2f}</h1>
                            <p style="color: #666; margin: 0;">time units</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with metric_cols[1]:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">🔄 Avg Turnaround Time</h3>
                            <h1 style="color: #333; margin: 10px 0;">{metrics['avg_turnaround_time']:.2f}</h1>
                            <p style="color: #666; margin: 0;">time units</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                with metric_cols[2]:
                    st.markdown(f"""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">⚡ Avg Response Time</h3>
                            <h1 style="color: #333; margin: 10px 0;">{metrics['avg_response_time']:.2f}</h1>
                            <p style="color: #666; margin: 0;">time units</p>
                        </div>
                    """, unsafe_allow_html=True)
                
                # Detailed process table
                st.markdown("### 📝 Detailed Process Information")
                
                import pandas as pd
                process_details = []
                for i, (proc_id, arrival, burst) in enumerate(processes):
                    if i < len(metrics['process_details']):
                        details = metrics['process_details'][i]
                        process_details.append({
                            'Process': f'P{proc_id}',
                            'Arrival Time': arrival,
                            'Burst Time': burst,
                            'Completion Time': details['completion_time'],
                            'Turnaround Time': details['turnaround_time'],
                            'Waiting Time': details['waiting_time'],
                            'Response Time': details['response_time']
                        })
                
                df = pd.DataFrame(process_details)
                st.dataframe(df, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### ℹ️ Algorithm Information")
    
    info_box = st.container()
    
    with info_box:
        if "FCFS" in algorithm:
            st.info("""
            **First Come First Serve (FCFS)**
            
            - Simplest CPU scheduling algorithm
            - Processes are executed in the order they arrive
            - Non-preemptive algorithm
            - May cause convoy effect
            
            **Best for:** Batch systems
            """)
        elif "Non-Preemptive" in algorithm:
            st.info("""
            **Shortest Job First (Non-Preemptive)**
            
            - Selects process with smallest burst time
            - Once started, runs to completion
            - Minimizes average waiting time
            - May cause starvation
            
            **Best for:** Processes with known burst times
            """)
        elif "Preemptive" in algorithm:
            st.info("""
            **Shortest Remaining Time First (Preemptive SJF)**
            
            - Preemptive version of SJF
            - Can interrupt current process
            - Always runs process with shortest remaining time
            - Optimal for minimum average waiting time
            
            **Best for:** Time-sharing systems
            """)
        else:  # Round Robin
            st.info("""
            **Round Robin**
            
            - Each process gets a fixed time quantum
            - Preemptive algorithm
            - Fair allocation of CPU time
            - Performance depends on time quantum
            
            **Best for:** Interactive systems
            """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Quick Tips")
    st.markdown("""
    - **Arrival Time**: When the process enters the ready queue
    - **Burst Time**: CPU time required by the process
    - **Waiting Time**: Time spent waiting in ready queue
    - **Turnaround Time**: Total time from arrival to completion
    - **Response Time**: Time from arrival to first execution
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: white; padding: 20px;">
        <p>Built with ❤️ using Streamlit | CPU Scheduling Simulator v2.0</p>
    </div>
""", unsafe_allow_html=True)
