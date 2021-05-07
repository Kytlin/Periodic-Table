import matplotlib.pyplot as plt

data = {
    'lithium': 5.392,
    'beryllium': 9.323,
    'boron': 8.298,
    'carbon': 11.260,
    'nitrogen': 14.534,
    'oxygen': 13.618,
    'fluorine': 17.423
}
names = list(data.keys())
values = list(data.values())

def first_IE():
    plt.plot(names, values)
    plt.show()