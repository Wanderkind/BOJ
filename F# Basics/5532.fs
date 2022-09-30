open System

let ceil a b =
    if a%b=0 then a/b else a/b+1

[<EntryPoint>]
let main _ =
    
    let l = Console.ReadLine() |> int
    let a = Console.ReadLine() |> int
    let b = Console.ReadLine() |> int
    let c = Console.ReadLine() |> int
    let d = Console.ReadLine() |> int

    printfn "%d" (l - max (ceil a c) (ceil b d))

    0
