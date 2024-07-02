from typing import Any, Callable
def get_variable_name(variable: Any, namespace: dict[str, Any] = globals()):
    return [nombre for nombre in namespace if namespace[nombre] is variable][0]

class BetterVariable:
    def __init__(self, value, description: str) -> None:
        self.value = value
        self.description = description
    def __str__(self) -> str:
        return f"""Variable name: {get_variable_name(self)}
Variable type: {type(self.value)}
Variable value: {self.value}
Variable description: {self.description}
"""
    def __matmul__(self, function: Callable) -> Any:
        return function(self.value)
