open System


[<EntryPoint>]
let main _ =
    
    let t = Console.ReadLine().Split ' ' |> Array.map int
    let n = t[0]
    let m = t[1]
    
    let k = min n m - 1
    let x = k/2
    let y = x + k%2

    let (p, q) =
        if k%2 = 1 then (x, y)
        else
            let z = y + max n m - 1 - k
            if n < m then (y, z)
            else (z, y)

    printf "%d %d\n" p q
        
    0
