while True:
    print("\n" + "="*30)
    print("      MAIN MENU")
    print("="*30)
    print("1 : GROCERY LIST")
    print("2 : RAISED TO A NUMBER")
    print("3 : FACTORIAL")
    print("4 : FIBONACCI SEQUENCE")
    print("5 : DECIMAL TO BINARY")
    print("6 : BINARY TO DECIMAL")
    print("X : EXIT")

    choice = input("\nENTER CHOICE (1-6): ").upper()

    if choice == 'X':
        print("\nEnd of program...")
        break

    elif choice == '1':
        while True:
            f = open("grocery.txt", "w")
            print("\nEnter items (type 'done' to finish list):")
            while True:
                item = input("> ")
                if item.lower() == 'done': 
                    break
                f.write(item + "\n")
            f.close()
            print("\nList saved to grocery.txt")
            if input("\nProcess another list? [Y/N]: ").lower() == 'n':
                break

    elif choice == '2':
        while True:
            f = open("raised.txt", "w")
            n = int(input("\nEnter Number: "))
            for i in range(1, n + 1):
                res = f"2 raised to {i} : {2**i}"
                print(res)
                f.write(res + "\n")
            f.close()
            print("\nResults saved to raised.txt")
            if input("\nTry another number? [Y/N]: ").lower() == 'n':
                break

    elif choice == '3':
        while True:
            f = open("factorial.txt", "w")
            n = int(input("\nEnter Number: "))
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            
            output = f"FACTORIAL OF {n} IS : {fact}"
            print(output)
            f.write(output + "\n")
            
            if n > 0:
                desc = ""
                asc = ""
                for i in range(n, 0, -1):
                    desc += str(i) + (" * " if i > 1 else "")
                for i in range(1, n + 1):
                    asc += str(i) + (" * " if i < n else "")
                print(f"= {desc}\n= {asc}")
                f.write(f"= {desc}\n= {asc}\n")
                
            f.close()
            print("\nResults saved to factorial.txt")
            if input("\nCalculate another factorial? [Y/N]: ").lower() == 'n':
                break

    elif choice == '4':
        while True:
            f = open("fibonacci.txt", "w")
            n = int(input("\nEnter Number: "))
            a, b = 1, 1
            seq = ""
            for i in range(n):
                seq += str(a) + ("-" if i < n - 1 else "")
                a, b = b, a + b
            print(f"Result: {seq}")
            f.write(seq + "\n")
            f.close()
            print("\nSequence saved to fibonacci.txt")
            if input("\nGenerate another sequence? [Y/N]: ").lower() == 'n':
                break

    elif choice == '5':
        while True:
            f = open("decimal_to_binary.txt", "w")
            val = int(input("\nEnter decimal value: "))
            temp_val = val
            remainders = []
            if temp_val == 0:
                binary_result = "0"
            else:
                while temp_val > 0:
                    remainders.append(str(temp_val % 2))
                    temp_val = temp_val // 2
                remainders.reverse()
                binary_result = "".join(remainders)
            
            output = f"Binary of {val} is : {binary_result}"
            print(output)
            f.write(output + "\n")
            f.close()
            print("\nConversion saved to decimal_to_binary.txt")
            if input("\nConvert another decimal? [Y/N]: ").lower() == 'n':
                break

    elif choice == '6':
        while True:
            f = open("binary_to_decimal.txt", "w")
            binary_str = input("\nEnter binary value: ")
            decimal_val = 0
            power = 0
            for digit in binary_str[::-1]:
                if digit == '1':
                    decimal_val += 2 ** power
                power += 1
            
            output = f"Decimal value of {binary_str} is : {decimal_val}"
            print(output)
            f.write(output + "\n")
            f.close()
            print("\nConversion saved to binary_to_decimal.txt")
            if input("\nConvert another binary? [Y/N]: ").lower() == 'n':
                break

    else:
        print("\nInvalid choice. Please enter 1-6 or X.")
