open System


let rec pow a b =
    if b = 0 then 1
    else a*(pow a (b-1))
;;
let rec ss p q =
    if q = 0 then 1
    else ss p (q-1) + pow p q
;;
let pf n =
    if n=1 then 1 else
    let rec factor n k =
        let rec howmany n k =
            if n % k > 0 then 0
            else howmany (n/k) k + 1
        let h = howmany n k in
        if h = 0 then factor n (k+1)
        else
            if n = pow k h then ss k h
            else ss k h * factor (n/(pow k h)) (k+1)
    factor n 2

[<EntryPoint>]
let main _ =
    
    let t = Console.ReadLine() |> int
    let line = Console.ReadLine().Split ' ' |> Array.map int
    for i=0 to t-1 do
        let n = line[i]
        let a = pf n - n
        if a > n then printf "Abundant\n"
        else if a < n then printf "Deficient\n"
        else printf "Perfect\n"
    done

    0
