open System

[<EntryPoint>]
let main _ =
   
    let line = Console.ReadLine().Split ' ' |> Array.map int
    
    let result = line.[0] + line.[1] + line.[2] + line.[3] + line.[4] + line.[5] 
    5*result |> Console.Write
    
    0 
