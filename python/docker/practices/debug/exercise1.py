from my_module import sample2

if __name__ == "__main__":
    x = sample2.hash("hoge")
    x = sample2.hash(x)
    print(x)
