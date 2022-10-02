open System

[<EntryPoint>]
let main _ =
    
    let n = Console.ReadLine() |> int
    let p = Console.ReadLine() |> int
    
    let f1 = p-500
    let f2 = p*9/10
    let f3 = p-2000
    let c = min f3 (p*3/4)
    let z =[|p;f1;min f1 f2;min f2 f3;c;c;c|][n/5]

    printf "%d" (max 0 z)

    0
