
states ={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
alphabet = {'0', '1'}
transition = {
        'A': {'0': 'B', '1': 'A'},
        'B': {'0': 'B', '1': 'C'},
        'C': {'0': 'D', '1': 'A'},
        'D': {'0': 'B', '1': 'E'},
        'E': {'0': 'H', '1': 'F'},
        'F': {'0': 'G', '1': 'F'},
        'G': {'0': 'G', '1': 'E'},
        'H': {'0': 'G', '1': 'E'}
}

initial_state = 'A'
accepting_states = {'E', 'F', 'G', 'H'}

def simulate_dfa(input_string):
    current_state = initial_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        current_state = transition[current_state][symbol]

    if current_state in accepting_states:
        return True
    return False


input_strings = ['00101', '101', '111001', '11010']
for string in input_strings:
    if(simulate_dfa(string)):
        print(string,'is ACCEPTED')
    else:
        print(string,'is REJECTED')
        
        
        