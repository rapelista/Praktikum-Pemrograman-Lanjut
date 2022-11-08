from collections import Counter


def remov_duplicates(input):
    input = input.split(" ")

    UniqW = Counter(input)
    print(UniqW)
    s = " ".join(UniqW.keys())
    print(s)


if __name__ == "__main__":
    input = input()
    remov_duplicates(input)
