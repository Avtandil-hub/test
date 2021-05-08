class B:
    count = 0
    def __init__(self):
        B.count += 1
    def __del__(self):
        B.count -= 1
    def _end(self):
        print('end')
a = B()
print(a.count)
a._end()