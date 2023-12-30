# The Singleton design pattern states that, a class has only one instance and provides a 
# global point of access to that instance.

from typing import Dict

class Borg:
    _shared_state: Dict[str, str] = {}
    def __init__(self) -> None:
        self.__dict__ = self._shared_state

class Singleton(Borg):
    def __init__(self, state: str = None) -> None:
        # Singleton initializes with state if given
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"
    
    def __str__(self) -> str:
        return self.state

rm1 = Singleton()
rm2 = Singleton()
rm1.state = "Idle"
rm2.state = "Running"
print('rm1: {0}'.format(rm1))  # running
print('rm2: {0}'.format(rm2))  # running

rm2.state = "Completed"
print('rm1: {0}'.format(rm1))  # completed
print('rm2: {0}'.format(rm2))  # completed

print(rm1 == rm2) #false, they share the state, but address is different.
rm3 = Singleton()
rm1.state = "Started"
print('rm1: {0}'.format(rm1))  # started
print('rm2: {0}'.format(rm2))  # started
print('rm3: {0}'.format(rm3))  # started
