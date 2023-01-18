open System


let f x y =
    if x = 0 then false
    else
    let (x, y) = if x > y then (y, x) else (x, y)
    let rec p n k i =
        if n <= k then (i-1, i-1-k+n)
        else p n (k+i) (i+1)
    let (a, b) = p x 0 1
    let (A, B) = p y 0 1
    let (s, t) = (A-a, B-b)
    let steps =
        if s < t then t
        else if t < 0 then s-t
        else s
    printf "%d\n" steps
    true

[<EntryPoint>]
let main _ =
    
    let mutable cont = true
    while cont do
        let line = Console.ReadLine().Split ' ' |> Array.map int
        let (x, y) = (line[0], line[1])
        cont <- f x y
    done

    0
