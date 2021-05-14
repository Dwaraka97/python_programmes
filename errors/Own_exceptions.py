class RuntimeException(Exception):
    def __init__(self, message, code):
        super().__init__(f"Error code {code} : {message}")
        self.code = code


err = RuntimeException('Page not found', 500)
print(err)
