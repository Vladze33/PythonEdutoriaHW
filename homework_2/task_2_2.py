class Buffer:
    def __init__(self, maxcapacity=5):
        self.maxcapacity = maxcapacity
        self.size = 0
        self.buffer = []

    def add_data(self, data):
        if self.size >= self.maxcapacity:
            print("Buffer overflow. Clearing in progress...")
            self.clear_data()
        self.size+=1
        self.buffer.append(data)

    def get_data(self):
        if not self.buffer:
            print("No buffer data")
        return self.buffer

    def clear_data(self):
        self.buffer.clear()
        self.size = 0


# Usage example
b = Buffer()
print("Adding 4:")
b.add_data(4)
print(b.get_data())

b.clear_data()

print()
print("After clearing:", b.get_data())
b.add_data([10]); b.add_data((5,6)); b.add_data(-1); b.add_data(2); b.add_data(0)
print(b.get_data())
b.add_data(20)
print(b.get_data())
