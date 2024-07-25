arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class FujtManager:
    def __init__(self, filename, mode = 'w'):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        self