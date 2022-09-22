open System

let f a b n w =
    if a=b then (if n=2 && a+b=w then 1 else -1)
    else if (w-a*n)%(b-a)<>0 then -1
    else
        let y = (w-a*n)/(b-a) in
            if y<=0 || n<=y then -1
            else y

[<EntryPoint>]
let main _ =
    
    let line = Console.ReadLine().Split ' ' |> Array.map int
    
    let a = line.[0]
    let b = line.[1]
    let n = line.[2]
    let w = line.[3]
    
    let r = (f a b n w)
    if r = -1 then printfn "%d\n" -1
    else printfn "%d %d\n" (n-r) r
    
    0
