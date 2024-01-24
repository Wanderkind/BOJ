open System
open System.IO 

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let eight (r: int) : bool list =
    let rec inner (acc: bool list) (num: int) = function
    | 8 -> acc
    | x -> inner ((num % 2 = 1) :: acc) (num / 2) (x + 1)
    inner [] r 0

let main _ : unit =
    
    let rk = sr.ReadLine().Split ' ' |> Array.map int
    let r, k = rk[0], rk[1]
    
    let e = eight r
    let e0, e1, e2, e3, e4, e5, e6, e7 = e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7]
    let rule (x: (bool * bool * bool)) : bool =
        match x with
        | ( true,  true,  true) -> e0
        | ( true,  true, false) -> e1
        | ( true, false,  true) -> e2
        | ( true, false, false) -> e3
        | (false,  true,  true) -> e4
        | (false,  true, false) -> e5
        | (false, false,  true) -> e6
        | (false, false, false) -> e7
    let line = sr.ReadLine() |> Seq.map (fun (c: char) -> c = 'X') |> Seq.toList
    
    let rec show (prev: bool list) (indx: int) : unit =
        if indx = k then () else
        let rec next acc p2 p1 = function
        | [] -> rule (p2, p1, false) :: acc
        | h :: t -> next (rule (p2, p1, h) :: acc) p1 h t
        let nextlist = next [] false <|| (List.head prev, List.tail prev) |> List.rev
        for b in nextlist do
            sw.Write(if b then 'X' else '.')
        done
        sw.WriteLine()
        (nextlist, indx + 1) ||> show

    show line 0

main ()

sr.Close()
sw.Close()
