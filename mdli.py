print("starting program")
class Prog:
    def mdli(self):
        # multi-dimensional lagrangian interpolation
        
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
        
        # printing function
        print("F = ", end="")
        for i in range(len(p_arr)):
            if p_arr[i][dim] != 1:
                print(p_arr[i][dim], end="")
            for j in range(len(p_arr)):
                if j != i:
                    if p_arr[i][dim] != 1:
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
                                print(f" - {p_arr[j][k]}", end="")
                            print(")", end="")
                            if no_denom == False:
                                print(f"/({p_arr[i][k] - p_arr[j][k]})", end="")
                        if k != dim - 1:
                            print(" * ", end="")
            if i != len(p_arr) - 1:
                print(" + ", end="")
        
        
        true_inp = input(f"\nenter your input point for the function ({dim}-variable function)\nenter \"STOP\" to stop\n").split()
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
            
            print(f"\nfor point {true_inp}, f({true_inp[:len(true_inp) - 1]}) = {full_val}\n")
            true_inp = input(f"\nenter your input point for the function ({dim}-variable function)\nenter \"STOP\" to stop\n").split()

program = Prog()
program.mdli()
