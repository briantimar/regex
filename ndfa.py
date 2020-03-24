"""Simple python code for nondeterministic finite automata."""

ALPHABET = "abcd"

class NDFA:
    """Defined by a finite number of states, as well as allowed transitions between them.
    """

    def __init__(self, num_states, transitions, alphabet=ALPHABET):
        """num_states = number of internal states.
            transitions: maps a state to a dictionary, which maps characters to allowed states.
            alphabet = character set for the inputs. Any input outside the alphabet automatically 
            produces a REJECT
            """
        
        self.num_states = num_states
        self.alphabet = alphabet
        self.transitions = transitions
        self._state = None
        #track different branches of the computation
        self._branches = []

    def init(self):
        self._state = 0
        self._branches = []
        self.epsilon_expand()

    def read(self, s):
        """Read the given string and either accept or reject it."""
        self.init()
        for c in s:
            self.transition(c)
        return any(b.accepts() for b in self._branches )

    def epsilon_expand(self):
        """Take all possible epsilon-moves and add them as new branches.
            In the NDFA execution graph, this is a horizontal move."""
        
    