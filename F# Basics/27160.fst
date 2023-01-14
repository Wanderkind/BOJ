open System


let rec f n =
    if n=0 then (0, 0, 0, 0)
    else
        let (s, b, l, p) = f (n-1)
        let line = Console.ReadLine().Split ' '
        let a = line[0]
        let c = line[1] |> int 
        match a with
        | "STRAWBERRY" -> (s+c, b, l, p)
        | "BANANA" -> (s, b+c, l, p)
        | "LIME" -> (s, b, l+c, p)
        | _ -> (s, b, l, p+c)

[<EntryPoint>]
let main _ =
    
    let n = Console.ReadLine() |> int
    let (s, b, l, p) = f n in
    if s=5 || b=5 || l=5 || p=5 then printf "YES\n" else printf "NO\n"

    0
