class Dependency:
    """A simple class to represent a dependency for the SimpleTest class."""

    def __init__(self, name: str):
        self.name = name


class SimpleTest:
    """A simple class to test pytest and coverage in this project."""

    def __init__(self, name: str, injected_dependency: Dependency):
        self.name = name
        self.injected_dependency = injected_dependency

    def add(self, a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtract two integers."""
        return a - b
