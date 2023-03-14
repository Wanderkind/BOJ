open Scanf
open Int64;;
let rec intarr = function | 1 -> [scanf "%Ld\n" (fun n -> n)] | x -> scanf "%Ld " (fun n -> n :: intarr (x-1));;
let rec pow = function
| 0 -> 1L
| x -> mul 2L @@ pow @@ x - 1;;
let rec f s i = function
| [] -> add s 1L
| h :: t -> (
  let p = pow i in
  match h with
  | 0L -> if s >= p then f s (i + 1) t else add s 1L
  | x -> f (add s @@ mul x p) (i + 1) t
);;
f 0L 0 @@ intarr @@ read_int () + 1 |> Printf.printf "%Ld\n";;
