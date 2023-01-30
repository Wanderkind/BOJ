open System

let rec pow a b =
  if b = 0L then 1L
  else a*(pow a (b-1L))

let rec ls n =
    if n < 10L then 0L
    else ls (n/10L) + 1L

let f n j =
    let rec g k =
        let a k =
            let w = pow 10L k
            let d = (n/w) % 10L
            let s = (n/w/10L)*w + n % w
            if d > j then (s/w + 1L)*w
            else if d < j then (s/w)*w
            else s+1L in
        if k = 0L then a 0L
        else g (k-1L) + a k in
    (n |> ls |> g)*j

let ds n =
    let rec s k =
        if k = 1L then f n k else s (k-1L) + f n k in
    s 9L

[<EntryPoint>]
let main _ =
    
    let line = Console.ReadLine().Split ' ' |> Array.map int64
    let (l, u) = (line[0], line[1])

    printf "%d" (ds u - ds (l-1L))
    
    0
