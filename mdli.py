from time import time
class Prog:
    def __init__(self):
        self.iters = 0
    def mdli(self):
        while True:
            if self.iters == 0:
                print("input \"STOP\" to stop entering points")
            else:
                print("\ninput \"STOP\" to stop entering points")
                
            # point array creation begin
            p_arr = []
            dim = int(input("# of input values (total values - 1)\n"))
            x = input("\nenter a point.\n").split()
            while len(x) != dim + 1:
                x = input(f"\nwrong amount of values, enter a point. ({dim + 1} numbers)\n").split()
            while x[0].lower() != "stop":
                for i in range(len(x)):
                    x[i] = int(x[i])
                p_arr.append(x)
                print(f"\ncurrent point array:")
                for point in p_arr:
                    print(*point)
                x = input("\nenter a point\n").split()
                while (len(x) != dim + 1 and x[0].lower() != "stop"):
                    x = input(f"\nwrong amount of values, enter a point. ({dim + 1} numbers)\n").split()
            # point array creation complete
            
            start_time = time()
            
            f_str = ""
            # printing function, LHS
            f_str += "f("
            for i in range(dim):
                f_str += f"x_{i + 1}"
                if i + 1 != dim:
                    f_str += ","
            f_str += ") = "
            
            # printing function, RHS
            for i in range(len(p_arr)):
                f_str += str(p_arr[i][dim])
                for j in range(len(p_arr)):
                    if j != i:
                        f_str += f" * "
                        for k in range(dim):
                            if p_arr[i][k] != p_arr[j][k]:
                                #print(f"(x_{k + 1} - {p_arr[j][k]})/({p_arr[i][k] - p_arr[j][k]})", end="")
                                no_dim = (dim == 1)
                                no_subtract = (p_arr[j][k] == 0)
                                no_denom = (p_arr[i][k] - p_arr[j][k] == 1)
                                f_str += f"(x"
                                if no_dim == False:
                                    f_str += f"_{k + 1}"
                                if no_subtract == False:
                                    if p_arr[j][k] > 0:
                                        f_str += f" - {p_arr[j][k]}"
                                    else:
                                        f_str += f" + {-1 * p_arr[j][k]}"
                                f_str += ")"
                                if no_denom == False:
                                    f_str += f"/({p_arr[i][k] - p_arr[j][k]})"
                                    
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
                                        # if there exists a valid future multiplier
                                        if p_arr[i][k + b] != p_arr[j][k + b]:
                                            fine = True
                                            break
                                        b += 1
                                    # if there exists a valid future multiplier
                                    if fine == True:
                                        f_str += " * "
                                        
                # the edge case also applies to this!!
                if i != len(p_arr) - 1:
                    fine2 = False
                    c = 1
                    # loops through every c in range of the array
                    while c + i <= len(p_arr) - 1: 
                        # if there exists a future valid summer
                        if j != i:
                            fine2 = True
                            break
                        c += 1
                    # if there exists a valid future summer
                    if fine2 == True:
                        f_str += " + "
            
            valid_p_arr = True
            
            # checking for point dupliation
            for i in range(len(p_arr)):
                for j in range(len(p_arr)):
                    if i != j:
                        count = 0
                        for k in range(dim):
                            if p_arr[i][k] == p_arr[j][k]:
                                count += 1
                        # if a point is duplicated
                        if count == dim:
                            valid_p_arr = False
            
            # if array is valid
            if valid_p_arr == True:
                print(f"\n{f_str}")
                print("\ntime taken to find a valid function:", time() - start_time)
                """
                cant for the life of me find out why this code returns the wrong value
                changing this to work soon, hopefully
                
                # taking input
                true_inp = input(f"\nenter your input point for the function ({dim}-variable function), or enter \"STOP\" to stop\n").split()
                while true_inp[0].lower() != "stop":
                    start_time_2 = time()
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
                    end_time_2 = time()
                    print("\ntime taken to find ", end="")
                    print("f(", end="")
                    for i in range(len(true_inp)):
                        print(f"{true_inp[i]}", end="")
                        if i < len(true_inp) - 1:
                            print(",", end="")
                    print(f"): ", end="")
                    print(end_time_2 - start_time_2)
                    
                    true_inp = input(f"\nenter your input point for the function ({dim}-variable function), or enter \"STOP\" to stop\n").split()
                """
            # if array is not valid
            else:
                print("you have a duplicated point in your point array. try again")
            
            self.iters += 1
            if self.iters > 1 or self.iters < 1:
                print(f"\n{self.iters} iterations of this program have been done.")
            else:
                print(f"\n{self.iters} iteration of this program has been done.")
            
            again = input("\nenter \"AGAIN\" to run the program again.\n")
            if again.lower() != "again":
                break
program = Prog()
program.mdli()
