# CHMAQUINA Project - Simulation of a Fictional Computer

This is the README document for the CHMAQUINA software project, which consists of a graphical simulation of a fictional computer with basic functionality. The program is developed in Python using the PyQt5 library for the graphical user interface. Below, you will find information about the project, its functionality, and how to use it.

## Project Description

The CHMAQUINA project is a simulation of a fictional computer that includes a basic processor and a main memory represented by a one-dimensional vector or array. The size of the memory can vary when starting the program, with a default size of Z*10 + 50 positions, where Z is an arbitrary digit to simulate a storage limit.

The program is capable of loading a set of programs written in a pseudo machine language called CHMAQUINA from files with the ".ch" extension. Each line of the file represents an instruction. The program performs syntax checking on the loaded programs and, if no errors are found, loads them into memory for execution.

The project is divided into several phases, including the graphical interface, program loading and syntax checking, process scheduling, memory management, and more.

## Project Features

The CHMAQUINA project offers the following key features:

1. Graphical Interface: Design of an intuitive graphical interface for the user, allowing for program loading, syntax verification, and execution.

2. Loading and Syntax Checking: The program can load CHMAQUINA programs from files with the ".ch" extension and perform syntax checking to identify errors. In case of finding errors, a list of them is displayed.

3. Operations and Variables: Integer and floating-point operations can be performed, using an accumulator to store the results. Memory positions can be used as variables and must be created before being used.

4. Instruction Types: The program supports various instructions such as load, store, add, subtract, multiply, divide, power, modulus, concatenate, delete, extract, logical operations (AND, OR, NOT), display, and more.

5. Process Scheduling: The user can select the process scheduling method, including FCFS, Round Robin, SJF preemptive and non-preemptive, and priority scheduling. The size of CPU and I/O bursts can be adjusted.

## System Requirements

To run the CHMAQUINA project, the following requirements must be met:

1. Python 3: Make sure you have the latest stable version of Python 3 installed on your system.

2. Libraries: Ensure that the following Python libraries are installed:
   - PyQt5: For the graphical interface.
   - Other libraries required based on the specific dependencies of your code.

## Installation and Usage

Follow the steps below to install and run the CHMAQUINA project:

1. Clone the project repository from GitHub: [Repository URL].

2. Open a terminal and navigate to the project directory.

3. Create a virtual environment (optional but recommended) and activate it.

4. Install the necessary dependencies by executing the following command:
   ```
   pip install -r requirements.txt
   ```

5. Run the CHMAQUINA program using the following command:
   ```
   python main.py
   ```

6. The graphical interface of the program will open, and you can start using its various functionalities.

7. Follow the instructions provided in the interface to load programs, verify syntax, run simulations, and utilize the specific features of the project.

## Contribution

This project was developed as part of an academic project and, therefore, is not open to external contributions at this time.

## Issues and Support

If you encounter any issues or have any questions about the project, you can create an issue on the GitHub repository. We will do our best to resolve issues and respond to your inquiries as soon as possible.

## Authors

The CHMAQUINA project was developed by Jeison Steven Franco as part of an academic project.
