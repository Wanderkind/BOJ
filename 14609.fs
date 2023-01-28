open System

// 14609

[<EntryPoint>]
let main _ =
    
    let k = Console.ReadLine() |> int
    let line = Console.ReadLine().Split ' ' |> Array.map float
    let ab = Console.ReadLine().Split ' '
    let (a, b, n) = (ab[0] |> float, ab[1] |> float, ab[2] |> int)

    let actual =
        let antd x =
            let rec af i x =
                match i with
                | 0 -> line[i] * x / (float (k-i+1))
                | _ -> x * (af (i-1) x) + line[i] * x / (float (k-i+1))
            in af k x
        in antd b - antd a
    
    let good x = (abs (actual - x)) / actual < 0.00001

    let func x =
        let rec f i x =
            match i with
            | 0 -> line[i]
            | _ -> x * (f (i-1) x) + line[i]
        in f k x
    
    let summed x =
        let rec s i x =
            let z = func (a + (b-a) * (float (i-1)) / (float n) + x) in
            match i with
            | 0 -> 0.
            | _ -> s (i-1) x + z
        in (b-a) * (s n x) / (float n)
    
    let rec binsearch l r =
        let t = (l+r)/2.
        let s = summed t
        if good s then t
        else if s < actual then binsearch t r
        else binsearch l t
    
    printf "%f\n" (binsearch 0 ((b-a)/(float n)))

    0
