open System

[<EntryPoint>]
let main _ =
    
    let arr = Console.ReadLine().Split ' ' |> Array.map int |> Array.sort
    let a = arr[0]
    let b = arr[1]
    let c = arr[2]
    
    let x =
        if a+b<=c then 0
        else if a=b && b=c then 2
        else if pown a 2 + pown b 2 = pown c 2 then 1
        else 0
    
    printfn "%d" (x)

    0
