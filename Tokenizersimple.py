# Define the set of states
states = {'Start', 'Englishword', 'Persianword'}

# Define the alphabet (English and Persian characters)
alphabet = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر',
    'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک',
    'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی'
}

# Define the transition function as a dictionary
transitions = {
    'Start': {char: 'Englishword' if char.isascii() and char.isalpha() else 'Persianword' if char in 'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی' else 'Start' for char in alphabet},
    'Englishword': {char: 'Englishword' if char.isascii() and char.isalpha() else 'Start' for char in alphabet},
    'Persianword': {char: 'Persianword' if char in 'آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی' else 'Start' for char in alphabet},
}

# Define the start state
start_state = 'Start'

# Define the set of accepting states
accepting_states = {'Englishword', 'Persianword'}

# Define a function to simulate the DFA
def simulate_dfa(input_string):
    current_state = start_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        current_state = transitions[current_state][symbol]
        if current_state == 'Start':
            return False
    
    return current_state

# Test the DFA
inputs = ["hello", "سلام","amirhossein"]
for input_str in inputs:
    result = simulate_dfa(input_str)
    if result == 'Start':
        print(f"'{input_str}' is rejected by the DFA")
    elif result == 'Englishword':
        print(f"'{input_str}' is accepted as an English word by the DFA")
    elif result == 'Persianword':
        print(f"'{input_str}' is accepted as a Persian word by the DFA")
        
    elif result == False:
            print(f"'{input_str}' is rejected by the DFA")
