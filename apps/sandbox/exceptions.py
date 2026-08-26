class SandboxError(Exception):
    def __init__(self, message: str, code: str = "sandbox_error"):
        super().__init__(message)
        self.message = message
        self.code = code


class ForbiddenSQLError(SandboxError):
    def __init__(self, message="Bu so‘rov ruxsat etilmagan."):
        super().__init__(message, "forbidden_sql")


class QueryTimeoutError(SandboxError):
    def __init__(self, message="So‘rov juda uzoq vaqt bajarilyapti. So‘rovni soddalashtirib qayta urinib ko‘ring."):
        super().__init__(message, "timeout")


class QueryLimitError(SandboxError):
    def __init__(self, message="So‘rov hajmi yoki natija limiti oshib ketdi."):
        super().__init__(message, "limit")
