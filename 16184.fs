open System
open System.IO 

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


let rec lst n =
    if n = 1L then [1L]
    else if n % 2L = 0L then lst (n/2L) @ [n]
    else
        let rec inner a b =
            match (a, b) with
            | (1L, 2L) -> [1L; 2L]
            | (2L, 3L) -> [1L; 2L; 3L]
            | _ -> inner (a/2L) (a/2L + 1L) @ [a; b]
        inner (n/2L) (n/2L + 1L) @ [n]

let show d : unit =
    let rec inner ind = function
    | h :: t ->
        match t with
        | [] -> ()
        | next :: _ ->
            if next = 2L*h then
                sw.WriteLine($"{ind} {ind}");
            else if next = 2L*h - 1L then
                sw.WriteLine($"{ind} {ind - 1}");
            else if next = 2L*h - 2L then
                sw.WriteLine($"{ind - 1} {ind - 1}");
            else // next + 1L
                sw.WriteLine($"{ind - 1} {ind - (if h % 2L = 0L then 2 else 1)}");
            inner (ind + 1) t
    | _ -> ()
    inner 0 d

let sol _ =
    let n = sr.ReadLine() |> int64
    let d = lst n
    let len = List.length d
    sw.WriteLine($"{len}\n-1 -1")
    show d
    sw.WriteLine(len - 1)


let main _ =
    for _ = 1 to sr.ReadLine() |> int do
        sol ()
    done

main ()

sr.Close()
sw.Close()
