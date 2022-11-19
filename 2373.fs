open System

let sol n =
    
    let mutable a = 0
    let mutable b = 0
    let mutable c = 1
    let mutable s = 1

    while s < n do
        a <- b
        b <- c
        c <- a+b
        s <- s+c

    let mutable k = c-s+n-1

    while k>0 && (k <> b) do
        
        if k < b then
            c <- b
            b <- a
            a <- c-b
        else
            k <- k-b
            b <- b-a
            a <- a-b
            c <- a+b

    if k>0 then b else -1


[<EntryPoint>]
let main _ =
    
    let n = Console.ReadLine() |> int

    n |> sol |> Console.Write

    0
