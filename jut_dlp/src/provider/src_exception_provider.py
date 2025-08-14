from abc import ABC, abstractmethod

class SrcExceptionProvider(ABC):
    exception_messages: dict[type[Exception], str]

    @abstractmethod
    def default_exception(exception:Exception) -> str:
        pass
    
    def get_message(self, exception:Exception) -> str:
        for exc_type, message in self.exception_messages.items():
            if isinstance(exception, exc_type):
                return message
        else:
            return self.default_exception(exception)