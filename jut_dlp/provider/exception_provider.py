from jut_dlp.src.provider.src_exception_provider import SrcExceptionProvider
import traceback

#Exceptions type
from requests.exceptions import RequestException

class ExceptionProvider(SrcExceptionProvider):
    exception_messages: dict[type[Exception], str] = {
        RequestException: "❌ У вас отсутствует доступ к интернету",
        TimeoutError: "⏱️ Время ожидания истекло",
    }

    def default_exception(self, exception:Exception) -> str:
        full_error = traceback.format_exc()  
        return full_error