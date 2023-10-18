# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:17:03 2023

@author: Kiarash Rahmani
"""

# Define the set of states
states = {'q0', 'q1', 'q2'}

# Define the alphabet
alphabet = {'0', '1'}

# Define the transition function as a dictionary
transitions = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q1', '1': 'q2'},
    'q2': {'0': 'q2', '1': 'q0'}
}

# Define the start state
start_state = 'q0'

# Define the set of accepting states
accepting_states = {'q0'}

# Define a function to simulate the DFA
def simulate_dfa(input_string):
    current_state = start_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        current_state = transitions[current_state][symbol]
    return current_state in accepting_states

# Test the DFA
inputs = ["", "0110", "1101", "111", "101010101", "111111111"]
for input_str in inputs:
    if simulate_dfa(input_str):
        print(f"'{input_str}' is accepted by the DFA")
    else:
        print(f"'{input_str}' is rejected by the DFA")
