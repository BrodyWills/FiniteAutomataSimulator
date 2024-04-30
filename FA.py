class FA:
    def __init__(self, alphabet, states, start_state, accept_states, transitions):
        """
        Initializes a finite automaton with the provided parameters.

        Args:
        alphabet (list): The alphabet of the finite automaton.
        states (list): The list of states in the finite automaton.
        start_state (str): The start state of the finite automaton.
        accept_states (list): The list of accept states in the finite automaton.
        transitions (list): The list of transitions in the finite automaton.

        Returns:
        None
        """
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

    def get_next_states(self, current_state, input_char):
        """
        Retrieves the next possible states based on the current state and input character.

        Args:
        current_state (str): The current state of the finite automaton.
        input_char (str): The input character for which the next states are to be determined.

        Returns:
        list: A list of next possible states based on the current state and input character.
        """
        next_states = []
        for transition in self.transitions:
            if (transition[0] == current_state and transition[2] == input_char) or transition[0] == current_state and transition[2] == 'EPSILON':
                next_states.append(transition[1])
        return next_states

    def get_epsilon_states(self, current_states):
        epsilon_states = list(current_states)
        new_states = [1]
        found = False

        while new_states:
            for state in epsilon_states:
                new_states = []
                new_states = self.get_next_states(state, 'EPSILON')
                if new_states:
                    epsilon_states.extend(new_states)
                    # check if state has any non-epsilon transitions
                    for transition in self.transitions:
                        if (transition[0] == state and transition[2] != "EPSILON"):
                            found = True
                    if not found:
                        epsilon_states.remove(state)
        return epsilon_states
    def accept(self, input_string):
        """
        Determines whether the finite automaton accepts the given input.

        Args:
        input_string (str): The input string to be processed by the finite automaton.

        Returns:
        bool: True if the input is accepted by the finite automaton, False otherwise.
        """
        current_states = {self.start_state}
        current_states = self.get_epsilon_states(current_states)

        for char in input_string:
            next_states = set()
            for state in current_states:
                next_states.update(self.get_next_states(state, char))
            current_states = next_states

            if not next_states:
                return False

            current_states.update(self.get_epsilon_states(current_states))

        return bool(current_states.intersection(self.accept_states))
