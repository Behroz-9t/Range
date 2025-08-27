class Range:
    """A simple version of Python's built-in range class."""

    def __init__(self, start, stop=None, step=1):
        # Handle case when only one argument is given (Range(n))
        
        if stop is None:
            
            stop = start
            start = 0


        if step == 0:
            raise ValueError("Step cannot be zero")

        self.start = start
        self.stop = stop
        self.step = step

        # Calculate length (number of elements)
        self.length = max(0, (stop - start + step - 1) // step)

    def __len__(self):
        """Return how many numbers are in the range"""
        return self.length

    def __getitem__(self, index):
        """Return the number at a given position in the range"""
        # Convert negative index to positive
        if index < 0:
            index += self.length

        # Check if index is valid
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")

        # Formula to compute the value
        return self.start + index * self.step

    def __iter__(self):
        """Allow looping with for"""
        value = self.start
        for _ in range(self.length):
            yield value
            value += self.step



R=Range(5,10,2)
print([x for x in R])
