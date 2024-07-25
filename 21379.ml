open Scanf
open Printf
;;

let fr ((a, _, _) : 'T * 'T * 'T) : 'T = a
let sc ((_, b, _) : 'T * 'T * 'T) : 'T = b
let th ((_, _, c) : 'T * 'T * 'T) : 'T = c

let fn (n: int) : (('T * 'T * 'T) -> 'T) =
    if n = 0 then fr else if n = 1 then sc else th

let rp (n: int) (u: 'T) ((a, b, c) : ('T * 'T * 'T)) : ('T * 'T * 'T) =
    if n = 0 then u, b, c
    else if n = 1 then a, u, c
    else a, b, u

type result =
| Win
| Lose
| Draw

type g =
| Empty
| Marten
| Me

type board = (g * g * g) * (g * g * g) * (g * g * g) 

type conc =
| Board of board
| Won of board
| Lost
| Full of board

let opponent = function
| Marten -> Me
| Me -> Marten
| Empty -> failwith "..."

let opposition = function
| Win -> Lose
| Lose -> Win
| Draw -> Draw

let gr = function
| Empty -> '.'
| Marten -> 'o'
| Me -> 'x'

let rg = function
| 'o' -> Marten
| 'x' -> Me
| _ -> Empty

let writeboard (((a, b, c), (d, e, f), (g, h, i)) : board) : unit =
    printf "%c%c%c\n%!" (gr g) (gr h) (gr i);
    printf "%c%c%c\n%!" (gr d) (gr e) (gr f);
    printf "%c%c%c\n%!" (gr a) (gr b) (gr c)

let readrow () : g * g * g = scanf "%s\n" @@ fun l -> rg l.[0], rg l.[1], rg l.[2]

let readboard () : board = readrow (), readrow (), readrow ()

let emptyrow = Empty, Empty, Empty

let bingo (p: g) (b: board) : bool =
    let f x = fr x = p, sc x = p, th x = p in
    let a0, a1, a2 = fr b |> f in
    let a3, a4, a5 = sc b |> f in
    let a6, a7, a8 = th b |> f in
    (a0 && a1 && a2) || (a3 && a4 && a5) || (a6 && a7 && a8) ||
    (a0 && a3 && a6) || (a1 && a4 && a7) || (a2 && a5 && a8) ||
    (a0 && a4 && a8) || (a2 && a4 && a6)

let rec win (t: int) (p: g) (b: board) : result * conc =
    let o = opponent p in
    if t = 9 then
        if bingo p b then Win, Won b
        else if bingo o b then Lose, Lost
        else Draw, Full b
    else
        let o = opponent p in
        if bingo o b then Lose, Lost else (
        let rec loop (z: int) (aim: result) : result * board =
            if z = 9 then
                if aim = Win then loop 0 Draw
                else Lose, b
            else
                let u, v = z / 3, z mod 3 in
                if b |> fn u |> fn v <> Empty then loop (z + 1) aim else (
                let newboard: board = rp u (b |> fn u |> rp v p) b in
                if win (t + 1) o newboard |> fst |> opposition = aim then aim, newboard
                else loop (z + 1) aim) in
        let x, y = loop 0 Win in
        if bingo p y then Win, Won y else
        if t = 8 then Draw, Full y else x, Board y)

let rec exec (t: int) (b: board) : unit =
    match win t Me b |> snd with
    | Lost -> ()
    | Won r -> writeboard r
    | Full r -> if t = 8 then writeboard r else ()
    | Board r -> (
        writeboard r;
        readboard () |> exec (t + 2))

let main () : unit =
    if (scanf "%s\n" @@ (fun x -> x)) = "first" then (
        readboard () |> ignore;
        (emptyrow, (Empty, Me, Empty), emptyrow) |> writeboard;
        readboard () |> exec 2)
    else
        readboard () |> exec 1

let () = main ()
