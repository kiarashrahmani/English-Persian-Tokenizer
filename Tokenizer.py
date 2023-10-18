# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:17:03 2023

@author: Kiarash Rahmani
"""

# Define the set of states
states = {'Start', 'Englishword'}

# Define the alphabet
alphabet = {
    # Numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    # English alphabet
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    # Signs
    '!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '*', '=', '+',
    '[', ']', '{', '}', '|', ';', ':', '<', '>', ',', '.', '?', '/',
    '`', '~', "'", '"',
    # Space
    ' '
}

# Define the transition function as a dictionary
transitions = {
    'Start': {
         # With this transitions DFA from Start goes to Englishword
              'A': 'Englishword', 'B': 'Englishword', 'C': 'Englishword', 'D': 'Englishword',
              'E': 'Englishword', 'F': 'Englishword', 'G': 'Englishword', 'H': 'Englishword',
              'I': 'Englishword', 'J': 'Englishword', 'K': 'Englishword', 'L': 'Englishword', 
              'M': 'Englishword', 'N': 'Englishword', 'O': 'Englishword', 'P': 'Englishword', 
              'Q': 'Englishword', 'R': 'Englishword', 'S': 'Englishword', 'T': 'Englishword',
              'U': 'Englishword', 'V': 'Englishword', 'W': 'Englishword', 'X': 'Englishword', 
              'Y': 'Englishword', 'Z': 'Englishword',
              
              'a': 'Englishword', 'b': 'Englishword', 'c': 'Englishword', 'd': 'Englishword',
              'e': 'Englishword', 'f': 'Englishword', 'g': 'Englishword', 'h': 'Englishword',
              'i': 'Englishword', 'j': 'Englishword', 'k': 'Englishword', 'l': 'Englishword',
              'm': 'Englishword', 'n': 'Englishword', 'o': 'Englishword', 'p': 'Englishword',
              'q': 'Englishword', 'r': 'Englishword', 's': 'Englishword', 't': 'Englishword',
              'u': 'Englishword', 'v': 'Englishword', 'w': 'Englishword', 'x': 'Englishword',
              'y': 'Englishword', 'z': 'Englishword',
              
              # With this transitions DFA from Start goes to Start
              '!': 'Start', '@': 'Start', '#': 'Start', '$': 'Start', '%': 'Start', '^': 'Start',
              '&': 'Start', '(': 'Start', ')': 'Start', '-': 'Start', '*': 'Start',
              '=': 'Start', '+': 'Start', '[': 'Start', ']': 'Start', '{': 'Start', 
              '}': 'Start', '|': 'Start', ';': 'Start', ':': 'Start', '<': 'Start', 
              '>': 'Start', ',': 'Start', '.': 'Start', '?': 'Start',
              '/': 'Start', '`': 'Start', '~': 'Start', "'": 'Start', '"': 'Start',
              '0': 'Start', '1': 'Start', '2': 'Start', '3': 'Start', '4': 'Start', 
              '5': 'Start', '6': 'Start', '7': 'Start', '8': 'Start',
              '9': 'Start', ' ': 'Start',
            }
    }

# Define the start state
start_state = 'Start'

# Define the set of accepting states
accepting_states = {'Englishword'}

# Define a function to simulate the DFA
def simulate_dfa(input_string):
    if input_string == '':
        return False
    current_state = start_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        current_state = transitions[current_state][symbol]
    return current_state in accepting_states

# Test the DFA
inputs = ["a", "hi", "1101", "111", "101010101", "111111111", "hello"]
for input_str in inputs:
    if simulate_dfa(input_str):
        print(f"'{input_str}' is accepted by the DFA")
    else:
        print(f"'{input_str}' is rejected by the DFA")
