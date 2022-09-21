open System

let line = Console.ReadLine().Split ' ' |> Array.map int

let ans = ((line.[0] - 1) / line.[1]) * line.[2] * line.[3]
printfn "%d\n" ans
