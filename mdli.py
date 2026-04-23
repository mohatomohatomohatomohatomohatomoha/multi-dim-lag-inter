class Prog:
    def __init__(self):
        self.ilovearbyschitlins = 0
    def mdli(self):
        if self.ilovearbyschitlins == 0:
            print("input \"STOP\" to stop entering points")
        else:
            print("\ninput \"STOP\" to stop entering points")
            
        # point array creation begin
        p_arr = []
        dim = int(input("# of input values (total values - 1)\n"))
        x = input("\nenter a point\n").split()
        while len(x) <= dim:
            x = input(f"\nnot enough values, enter a point ({dim + 1} numbers)\n").split()
        while x[0].lower() != "stop":
            for i in range(len(x)):
                x[i] = int(x[i])
            p_arr.append(x)
            print(f"\ncurrent point array:")
            for point in p_arr:
                print(*point)
            x = input("\nenter a point\n").split()
            while (len(x) <= dim and x[0].lower() != "stop"):
                x = input(f"\nnot enough values, enter a point ({dim + 1} numbers)\n").split()
        # point array creation complete
        
        # printing function, LHS
        print("f(", end="")
        for i in range(dim):
            print(f"x_{i + 1}", end="")
            if i + 1 != dim:
                print(",", end="")
        print(") = ", end="")
        
        # printing function, RHS
        for i in range(len(p_arr)):
            print(p_arr[i][dim], end="")
            for j in range(len(p_arr)):
                if j != i:
                    print(f" * ", end="")
                    for k in range(dim):
                        if p_arr[i][k] != p_arr[j][k]:
                            #print(f"(x_{k + 1} - {p_arr[j][k]})/({p_arr[i][k] - p_arr[j][k]})", end="")
                            no_dim = (dim == 1)
                            no_subtract = (p_arr[j][k] == 0)
                            no_denom = (p_arr[i][k] - p_arr[j][k] == 1)
                            print(f"(x", end="")
                            if no_dim == False:
                                print(f"_{k + 1}", end="")
                            if no_subtract == False:
                                if p_arr[j][k] > 0:
                                    print(f" - {p_arr[j][k]}", end="")
                                else:
                                    print(f" + {-1 * p_arr[j][k]}", end="")
                            print(")", end="")
                            if no_denom == False:
                                print(f"/({p_arr[i][k] - p_arr[j][k]})", end="")
                                
                            """
                            
                            really icky edge case for multiplying
                            
                            current multiplier isnt the last of the sum, but every past multiplier in the sum is invalid
                            a.k.a. every multiplier past it creates a division by zero case
                            in that case, we stop the multiplier notation because every multiplier past it wont be printed
                            
                            this edge case appears here and in the addition notation part as well
                            
                            """
                            
                            if k != dim - 1:
                                fine = False
                                b = 1
                                # loops through every b in range of the array
                                while b + k <= dim - 1:
                                    if p_arr[i][k + b] != p_arr[j][k + b]:
                                        fine = True
                                        break
                                    b += 1
                                if fine == True:
                                    print(" * ", end="")
                                    
            # the edge case also applies to this!!
            if i != len(p_arr) - 1:
                fine2 = False
                c = 1
                # loops through every c in range of the array
                while c + i <= len(p_arr) - 1: 
                    if j != i:
                        fine2 = True
                        break
                    c += 1
                if fine2 == True:
                    print(" + ", end="")
                
        print()
        
        # taking input
        true_inp = input(f"\nenter your input point for the function ({dim}-variable function), or enter \"STOP\" to stop\n").split()
        while true_inp[0].lower() != "stop":
            for i in range(len(true_inp)):
                true_inp[i] = int(true_inp[i])
                
            true_point = true_inp
            # input complete
            
            # returning f(true_point)
            full_val = 0
            for i in range(len(p_arr)):
                for j in range(len(p_arr)):
                    if j != i:
                        a = 1
                        for k in range(dim):
                            if p_arr[i][k] != p_arr[j][k]:
                                a *= (true_point[k] - p_arr[j][k])/(p_arr[i][k] - p_arr[j][k])
                a *= p_arr[i][dim]
                full_val += a
            
            print("\nf(", end="")
            for i in range(len(true_inp)):
                print(f"{true_inp[i]}", end="")
                if i < len(true_inp) - 1:
                    print(",", end="")
            print(f") = {full_val}\n", end="")
            
            true_inp = input(f"\nenter your input point for the function ({dim}-variable function)\nenter \"STOP\" to stop\n").split()
        self.ilovearbyschitlins += 1

program = Prog()
program.mdli()
