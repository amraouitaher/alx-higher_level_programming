#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    
    total_result = 0
    
    for arg in sys.argv:
        total_result += int(arg)
        print("{}".format(total_result))
