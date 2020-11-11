import query

def main():
    query1 = query.Query1()
    otheerClass = query.OtherClass()
    otheerClass.foo3(query1)
    return 0

if __name__ == "__main__":
    main()