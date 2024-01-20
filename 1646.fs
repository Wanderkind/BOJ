open System
open System.IO 

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let replace ind newval lst =
    List.mapi (fun i x -> if i = ind then newval else x) lst

let fib n =
    let rec inner x =
        match x with
        | 0 | 1 -> 1L
        | _ ->
            let rec f a b z =
                if z = x then a + b + 1L
                else f b (a + b + 1L) (z + 1)
            f 1L 1L 2
    inner n

type tree =
| Root
| Left
| Right

let loc ord num =
    let rec inner acc n x =
        match x with
        | 0 | 1 -> (x, Root) :: acc
        | _ ->
            if n = 1L then (x, Root) :: acc else
            let ls = fib (x - 2)
            if n - 1L <= ls then inner ((x, Left) :: acc) (n - 1L) (x - 2)
            else inner ((x, Right) :: acc) (n - 1L - ls) (x - 1)
    inner [] num ord

let trim a b =
    let rec inner p q =
        match (p, q) with
        | ([], _) | (_, []) -> (List.rev p) @ q
        | (a :: b, c :: d) -> if a = c then inner b d else (List.rev p) @ q
    (List.rev a, List.rev b) ||> inner

let route lst =
    let rec inner acc = function
    | [] -> acc
    | h :: t ->
        let a, p = h
        match t with
        | [] -> acc
        | next :: _ ->
            let b = fst next
            if a < b then inner (acc + "U") t
            else if a > b then inner (acc + if p = Left then "L" else "R") t
            else inner acc t
    inner "" lst |> sw.WriteLine

let main _ =
    let line = sr.ReadLine().Split ' ' |> Array.map int64
    let n, s, e = int line[0], line[1], line[2]
    let ans = (loc n s, loc n e) ||> trim
    route ans

main ()

sr.Close()
sw.Close()
