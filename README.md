# Finite Automaton (FA) Implementation

This Python program implements a Finite Automaton (FA) class that models both deterministic finite automata (DFA) and nondeterministic finite automata (NFA). The FA is capable of processing input strings and determining whether they are accepted by the automaton.

## DFA/NFA Defintion File Format
The first line contains the alphabet symbols (no spaces or commas)

The second line contains the number of states

Subsequent lines contain each state

The next line contains the start state

The next line contains the number of accept states

Subsequent lines contain each accept state

The next line contains the number of transitions

Subsequent lines contain each transition in the format: current_state,next_state,input_symbol

## How to Use
1. Place the DFA/NFA definition file in the definitions folder
2. Place input strings inside the inputs.txt file, with each string on a separate line
3. Execute the Simulator.py script in your Python environment
4. Enter the name of the definition file
5. The script outputs whether each input string is accepted or rejected by the FA

