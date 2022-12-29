open System

let f n =
    let k = pown 10 n
    n*k - (k-1)/9

let digits n =
    let v k = f (k-1) < n && n <= f k
    let rec p k = if v k then k else p (k+1)
    p 1

let sol n =
    let d = digits n
    let nn = n - f (d-1) - 1
    let rec numm p q = if q = 0 then p%10 else numm (p/10) (q-1)
    let num p q = numm p (d-q-1)
    let rec s k w = if k/d = 0 then num ((pown 10 (d-1))+w) k else s (k-d) (w+1)
    s nn 0

[<EntryPoint>]
let main _ =    
    Console.ReadLine() |> int |> sol |> Console.WriteLine
    0
