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

englishalphabet = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    }

persianalphabet = {
    'آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر',
    'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک',
    'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی'
    }
# Define the transition function as a dictionary
transitions = {
    'Start': {char: 'Englishword' if char in englishalphabet else 'Persianword' if char in persianalphabet else 'Start' for char in alphabet},
    'Englishword': {char: 'Englishword' if char in englishalphabet else 'Start' for char in alphabet},
    'Persianword': {char: 'Persianword' if char in persianalphabet else 'Start' for char in alphabet},
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
input_string = "مهدی university of zanjan اسt This is a test string to check the DFA's functionality. یک متن نمونه برای تست عملکرد DFA است. شلام دنیا! 12345 فارسی English محمد John سلام World متن تست دیگر 123ABC man time shop kitchen mirror calendar say doctor son آpple notebook student handle window machine television keyboard rhone homework pencil quit puppy damn friend dog run sun to double tip pick tick ten rather take school lesson shirt car cat shade race game hold ear phone parent play bike girl guy flower shower pet par brother war first day tun fix bell hurt sad fun run table chime home day house food door love sea sky sky star name"
inputs = []
current_word = ""
for char in input_string:
    if char == ' ':
        if current_word:
            inputs.append(current_word)
        current_word = ""
    else:
        current_word += char

if current_word:
    inputs.append(current_word)


print(inputs)
for input_str in inputs:
    result = simulate_dfa(input_str)
    if result == 'Start':
        print(f"'{input_str}' is rejected by the DFA")
    elif result == 'Englishword':
        print(f"'{input_str}' is an English word")
    elif result == 'Persianword':
        print(f"'{input_str}' is a Persian word ")
        
    elif result == False:
            print(f"'{input_str}' is rejected by the DFA")
