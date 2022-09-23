open System

[<EntryPoint>]
let main _ =
        
    let arr = Console.ReadLine().Split ' ' |> Array.map int64
    let m = arr[1]
    let k = arr[2]
    
    printfn "%d %d" (k/m) (k%m)
    
    0
