from FA import FA


def read_file(file_name):
    """
    Reads the content of a file and constructs a Finite Automaton (FA) based on the file content.

    Parameters:
    file_name (str): The name of the file to be read.

    Returns:
    FA: An instance of the FA class representing the Finite Automaton constructed from the file content.
    """
    with open(file_name, 'r') as f:
        alphabet = f.readline().strip()  # Read the alphabet from the first line of the file

        num_states = int(f.readline().strip())  # Read the number of states
        states = []
        for i in range(num_states):
            states.append(f.readline().strip())  # Read each state and add it to the list of states

        start_state = f.readline().strip()  # Read the start state

        num_accept_states = int(f.readline().strip())  # Read the number of accept states
        accept_states = []
        for i in range(num_accept_states):
            accept_states.append(f.readline().strip())  # Read each accept state and add it to the list of accept states

        num_transitions = int(f.readline().strip())  # Read the number of transitions
        transitions = []
        for i in range(num_transitions):
            transition = f.readline().strip().split(',')  # Read each transition and split it into components
            transitions.append((transition[0], transition[1], transition[2]))  # Add the transition to the list of transitions

        return FA(alphabet, states, start_state, accept_states, transitions)

strings = ['aaa', 'aab', 'aba', 'abb', 'bbb', 'bba', 'bab', 'baa']

file = input('Enter the name of the file: ')
file = 'definitions/' + file + '.txt'

file2 = 'inputs.txt'
with open(file2, 'r') as f:
    strings = f.readlines()
strings = [s.strip() for s in strings]

for string in strings:
    fa = read_file(file)
    if fa.accept(string):
        print('Accepted the string: ', string)
    else:
        print('Rejected the string: ', string)
