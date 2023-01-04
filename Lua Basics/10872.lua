function f(n)
    if n==0 then return 1
    else return n*f(n-1)
    end
end
n=io.read("*number")
print(f(n))
