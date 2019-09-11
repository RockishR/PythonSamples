def main():
    print("in Function main()...")
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a String "
    print(s)
    print(s+ " Test")
    print(s+str(b))
    print(s+ b.decode('utf-8'))

    print(s.encode('utf-8'))
    print(s.encode('utf-32'))
    
if __name__=="__main__":
    main();