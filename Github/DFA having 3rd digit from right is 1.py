
states ={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
alphabet = {'0', '1'}
transition = {
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'C', '1': 'E'},
        'C': {'0': 'D', '1': 'F'},
        'D': {'0': 'A', '1': 'B'},
        'E': {'0': 'G', '1': 'H'},
        'F': {'0': 'C', '1': 'E'},
        'G': {'0': 'D', '1': 'F'},
        'H': {'0': 'G', '1': 'H'}
}

initial_state = 'A'
accepting_states = {'D', 'F', 'G', 'H'}

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
        
        
        