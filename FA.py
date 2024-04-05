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

    def accept(self, input_string):
        """
        Determines whether the finite automaton accepts the given input.

        Args:
        input_string (str): The input string to be processed by the finite automaton.

        Returns:
        bool: True if the input is accepted by the finite automaton, False otherwise.
        """
        current_state = self.start_state  # Set the current state to the start state
        for char in input_string:  # For each character in the input string
            transition_found = False
            for transition in self.transitions:
                if transition[0] == current_state and transition[2] == char:
                    current_state = transition[1]  # Update the current state based on the transition
                    transition_found = True
                    break
            if not transition_found:
                return False  # If no valid transition is found, reject the input
        return current_state in self.accept_states  # Check if the final state is an accept state and return the result
