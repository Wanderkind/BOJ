open System

[<EntryPoint>]
let main _ =
    
    let line = Console.ReadLine().Split ' ' |> Array.map int
    let n = line[0]
    let b = line[1]

    let mutable arr = [||]

    for i = 1 to n do
        let k = Console.ReadLine() |> int
        arr <- Array.append arr [|k|]
    done

    let a = arr |> Array.sort |> Array.rev

    let mutable cont = true
    let mutable h = 0
    let mutable i = 0

    while cont do 
        
        h <- h + a[i]
        i <- i + 1

        if b <= h then
            cont <- false

    done

    printfn "%d" i

    0
