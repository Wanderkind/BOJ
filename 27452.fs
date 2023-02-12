open System


let rec bin n =
    if n < 2L then [n % 2L = 1L]
    else bin (n/2L) @ [n % 2L = 1L]

let mm a b =
    let ((p, q), (r, s)) = a
    let ((t, u), (v, w)) = b
    ((p*t+q*v, p*u+q*w), (r*t+s*v, r*u+s*w))

let f n =
    let rec ff p q r =
        if List.length r = 1 then
            if r[0] then (mm p q, q)
            else (p, q)
        else
            let (pp, qq) = ff p q r[1..] in
            let qqq = mm qq qq in
            if r[0] then (mm pp qqq, qqq)
            else (pp, qqq) in
    ff ((1L, 0L), (0L, 1L)) ((1L, 1L), (1L, 0L)) (bin n) |> fst |> fst |> snd

let l n = 4L*(f n)-2L

let rec sol n k =
    //printf "n = %d, k = %d\n" n k//////

    let (l83, l84) = (l 83, l 84)
    
    if n < 85L then
        
        if k > (l n) then printf "0\n"
    
        else
        
            let mutable status = n
            let mutable loc = k
            let mutable cont = true
        
            while cont do
                if loc = 1L then
                    printf "(\n"
                    cont <- false
                else if status < 85L && loc = l status then
                    printf ")\n"
                    cont <- false
                else
                    loc <- loc - 1L
                    if loc <= l (status - 2L) then
                        status <- status - 2L
                    else
                        loc <- loc - l (status - 2L)
                        status <- status - 1L
            done
    
    else
        
        let d = (n - 83L)/2L
        let newk = k - d
        //printf "newk = %d\n" newk///////////

        if newk < 1 then printf "(\n"

        else if n % 2L = 1L then
            if newk > l83 then sol 84L (newk - l83)
            else sol 83L newk
        
        else
            if newk > l84 then sol 85L (newk - l84)
            else sol 84L newk

            

[<EntryPoint>]
let main _ =
    
    for i = 1 to Console.ReadLine() |> int do
        let nk = Console.ReadLine().Split ' ' |> Array.map int64
        let (n, k) = (nk[0], nk[1])
        sol n k
    done

    0
