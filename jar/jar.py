class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n > self._capacity or self._size + n > self._capacity:
            raise ValueError("Exceeded capacity")
        self._size += n


    def withdraw(self, n):
        if n > self._size or n > self._capacity:
            raise ValueError("Invalid number of cookies")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)


if __name__ == "__main__":
    main()
