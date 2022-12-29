open System


let rec f a b =
    if a <= b then b-a
    else if a%2=1 then 1 + f (a+1) b
    else 1 + f (a/2) b

[<EntryPoint>]
let main _ =
    
    let line = Console.ReadLine().Split ' ' |> Array.map int
    let a = line.[0]
    let b = line.[1]

    printf "%d\n" (f a b)

    0
