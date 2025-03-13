#Code bedore refactoring
#def f(l, t): r = [] for i in range(len(l)): if l[i]["t"] == t: r.append(l[i]) return r
#Code after refactoring
def f(l, t): return [l[i] for i in range(len(l)) if l[i]["t"] == t]

#Test cases
# Test case 1
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 1
# Expected output: [{"t": 1}, {"t": 1}]
print(f(l, t))

# Test case 2
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 2
# Expected output: [{"t": 2}, {"t": 2}]
print(f(l, t))

# Test case 3
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 3
# Expected output: [{"t": 3}]
print(f(l, t))

# Test case 4
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 4
# Expected output: []
print(f(l, t))

# Test case 5
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 0
# Expected output: []
print(f(l, t))

# Test case 6
l = [{"t": 1}, {"t": 2}, {"t": 3}, {"t": 2}, {"t": 1}]
t = 5
# Expected output: []
print(f(l, t))