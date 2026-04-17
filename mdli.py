# multi-dimensional lagrangian interpolation

print("input \"STOP\" to stop entering points")

# point array creation begin
p_arr = []
dim = int(input("# of input values (total values - 1)\n"))
x = input("\nenter a point\n").split()
while x[0].lower() != "stop":
    for i in range(len(x)):
        x[i] = int(x[i])
    p_arr.append(x)
    print(f"\ncurrent point array:")
    for point in p_arr:
        print(*point)
    x = input("\nenter a point\n").split()
# point array creation complete

# taking input
true_inp = input(f"\nenter your input point for the function ({dim}-variable function)\n").split()

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

print(f"for point {true_inp}, f({true_inp[:len(true_inp) - 1]}) = {full_val}")
