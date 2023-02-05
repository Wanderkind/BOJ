open System


let rec pow n = function
    | 0 -> 1
    | x -> (pow n (x-1)) * n

let sol h path =
    let rec seek num height path =
        if height = -1 then 0 else
        match path with
        | [] -> num
        | h :: t ->
            match h with
            | 'L' -> seek (num*2) (height - 1) t
            | _ -> seek (num*2 + 1) (height - 1) t
    seek 1 h path |> (fun n -> pow 2 (h+1) - n |> printf "%d\n") 

[<EntryPoint>]
let main _ =
    
    let line = Console.ReadLine().Split ' '
    let h = line[0] |> int
    let path = if line |> Array.length = 2 then line[1] |> Seq.toList else []
    sol h path
    
    0
