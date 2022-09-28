open System

[<EntryPoint>]
let main _ =
    
    let n = Console.ReadLine() |> int    
    for i=1 to n do
        let k = Console.ReadLine() |> int
        printfn "Material Management %d" (i)
        Console.ReadLine()
        for j=1 to k do
            Console.ReadLine()
        done
        printfn "Classification ---- End!"
    done

    0
