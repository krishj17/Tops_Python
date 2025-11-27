class Val1Small(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

n1 = 0
n2 = 5

try:
    if n1 > n2:
        print(f"Difference: {n1 - n2}")
    else:
        raise Val1Small("Error")
except Val1Small as e:
    print(f"Exc: {e}")
