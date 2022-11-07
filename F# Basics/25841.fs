open System

let last n d =
    if n%10 =  d then 1 else 0

let rec count n d=
    if n<10 then last n d
    else last n d + count (n/10) d

let rec sol l r d =
    if l = r then count l d
    else count l d + sol (l+1) r d

[<EntryPoint>]
let main _ =

    let line = Console.ReadLine().Split ' ' |> Array.map int
    let l = line[0]
    let r = line[1]
    let d = line[2]

    printf "%d" (sol l r d)

    0
