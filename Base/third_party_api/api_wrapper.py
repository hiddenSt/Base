

class ApiWrapper:
    """Base class for APIWrappers."""
    def make_query(self, parameters: str):
        raise RuntimeError("Method make_query() is not overridden!")

    def get_result(self):
        raise RuntimeError("Method get_result() is not overridden!")
