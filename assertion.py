# check assumptions to pre-emptively catch bugs
# Examples:
    # checking types or classes
    # checking value bounds
    # impossible situations

# Assertions vs Exceptions
    # Assertions: check for conditions that should NEVER happen
        # use to crash early if program state has corrupted
    # Exceptions: check for conditions that can conceivably happen and would cause program failure


# a class containing mappings between integer keys and sring values
class TwoWayMap:
    def __init__(self):
        self._k2v_map = {}
        self._v2k_map = {}

    def add(self, k, v):
        assert type(k) is IntType, "k is not an int: " + str(k)
        assert type(v) is StringType, "v is not a string: " + str(v)
        self._k2v_map[k] = v
        self._v2k_map[v] = k

    def k_to_v(self, k):
        v = self._k2v_map[k]
        assert self._v2k_map[v] == k
        return v

    def v_to_k(self, v):
        k = self._v2k_map[v]
        assert self._k2v_map[k] == v
        return k