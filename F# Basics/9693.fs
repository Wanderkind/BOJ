open System


let rec f n =
    let rec howmany a b =
        if a%b <> 0 then 0
        else 1 + howmany (a/b) b in
    let rec p k =
        if k=1 then 0
        else p (k-1) + howmany k 2 in
    let rec q k =
        if k=1 then 0
        else q (k-1) + howmany k 5 in
    min (p n) (q n)
    

[<EntryPoint>]
let main _ =
    
    let mutable i = 0
    let mutable cont = true

    while cont do
        
        i <- i+1
        let n = Console.ReadLine() |> int
        if n=0 then cont <- false
        else printf "Case #%d: %d\n" i (f n)

    0
