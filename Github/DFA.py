
states ={'q0', 'q1', 'q2', 'q3'}
alphabet = {'a', 'b'}
transition = {
        'q0': {'a': 'q1', 'b': 'q3'},
        'q1': {'a': 'q3', 'b': 'q2'},
        'q2': {'a': 'q2', 'b': 'q2'},
        'q3': {'a': 'q3', 'b': 'q3'}
}

initial_state = 'q0'
accepting_states = {'q2'}

def simulate_dfa(input_string):
    current_state = initial_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        current_state = transition[current_state][symbol]

    if current_state in accepting_states:
        return True
    return False


input_strings = ['001', 'bbba', 'aab', 'aba']
for string in input_strings:
    if(simulate_dfa(string)):
        print(string,'is ACCEPTED')
    else:
        print(string,'is REJECTED')
        
        
        