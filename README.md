# 🧠 **Process Scheduling Simulation (OS Semester Project)**

This project is a **graphical simulation of CPU process scheduling algorithms** developed using **Python**, **Tkinter**, and **Turtle graphics**.  
It visually demonstrates how different scheduling algorithms execute processes and helps in understanding core **Operating System concepts**.

This project was developed as part of the **Operating Systems (OS) semester project**.

---

## 📚 **Table of Contents**
- [Overview](#-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [User Interface](#-user-interface)
- [Scheduling Algorithms](#-scheduling-algorithms)
- [Working Mechanism](#-working-mechanism)
- [Screenshots](#-screenshots)
- [License](#-license)
- [Author](#-author)

---

## 🔍 **Overview**
The **Process Scheduling Simulator** provides a **visual and interactive** way to understand how **CPU scheduling algorithms** work.  
Users can input **process data** and observe the **execution order** using a **Gantt Chart**, along with calculated **performance metrics**.

---

## ✨ **Features**
- 📊 **Gantt chart visualization** of process execution
- ⚙️ **Simulation of popular CPU scheduling algorithms**:
  - **First-Come, First-Served (FCFS)**
  - **Shortest Job First (SJF – Preemptive & Non-Preemptive)**
  - **Round Robin (RR)**
- 🧮 **Automatic calculation** of:
  - **Waiting Time**
  - **Turnaround Time**
  - **Response Time**
- 🖥️ **Interactive GUI** built using **Tkinter**
- 🎨 **Visual execution** using **Turtle graphics**

---

## 🛠️ **Technologies Used**
- **Python 3**
- **Tkinter** (**GUI**)
- **Turtle Graphics** (**Visualization**)
- **Operating System Concepts**

---

## 💻 **Installation**

### **1. Clone the repository**
```bash
git clone https://github.com/Iqra-Hayder/Process-Scheduler.git
### **2. Navigate to the project folder**
```bash
cd Process-Scheduler

✅ No external libraries required
Tkinter and Turtle come pre-installed with Python.

▶️ How to Run
```bash
python simulator.py

🖥️ User Interface

The simulator provides a simple and user-friendly interface consisting of:
**Input Section**

-Process ID

-Arrival Time

-Burst Time

-Algorithm Selection

-FCFS

-SJF

-Round Robin

**Controls**

-Add or remove processes

-Start Simulation button

**Output**

-Gantt chart visualization

-Average waiting time

-Average turnaround time

-Average response time

⚙️ Scheduling Algorithms
First-Come, First-Served (FCFS)

Executes processes in the order they arrive

Non-preemptive

Simple but may cause long waiting times

Shortest Job First (SJF)

Executes the process with the shortest burst time

Available in:

Preemptive

Non-preemptive

Minimizes average waiting time

Round Robin (RR)

Each process gets a fixed time quantum

Preemptive algorithm

Ideal for time-sharing systems

🔄 Working Mechanism

     User inputs process data
     
     Selects a scheduling algorithm
     
     Simulator executes algorithm logic
     
     Turtle draws the Gantt chart
     
     Performance metrics are calculated and displayed

🖼️ Screenshots
🖥️ User Interface
<p align="center"> <img src="./img/User-interface.png"> </p>
📊 FCFS Output
<p align="center"> <img src="./img/FCFS-example.png"> </p>
📊 SJF (Non-Preemptive)
<p align="center"> <img src="./img/SJF-non-preemptive-example.png"> </p>
📊 SJF (Preemptive)
<p align="center"> <img src="./img/SJF-preemptive-example.png"> </p>
📊 Round Robin
<p align="center"> <img src="./img/RR-example.png"> </p>



👩‍💻 Author

Iqra Hayder
GitHub: https://github.com/Iqra-Hayder
