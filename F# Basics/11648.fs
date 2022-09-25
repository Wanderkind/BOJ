open System

[<EntryPoint>]
let main _ =
    
    let mutable x = 0
    let mutable n = Console.ReadLine() |> int32
    
    while n>9 do
        
        let s = n.ToString()
        let len = s.Length
        let mutable k = 1

        for i=0 to len-1 do
            k <- k*(string s[i] |> int32)
        done

        n <- k
        x <- x+1

    done

    Console.Write $"{x}"

    0 
