function f(n, k)
    if k==0 or k==n then return 1
    else return f(n-1, k-1) + f(n-1, k)
    end
end
n, k=io.read("*number", "*number")
print(f(n, k))
