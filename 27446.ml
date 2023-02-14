open Printf
open Scanf
;;
let rec intarr = function | 1 -> [scanf "%d\n" (fun n -> n)] | x -> scanf "%d " (fun n -> n :: intarr (x-1))
;;
let (n, m) = scanf "%d %d\n" (fun n m -> (n, m)) in
let pages = intarr m in
let rec notin k = function
| [] -> true
| h :: t -> if k = h then false else notin k t in
let rec f = function
| 1 -> if notin 1 pages then [1] else []
| x -> f (x-1) @ (if notin x pages then [x] else []) in
let lost = f n in
match lost with
  | [] -> print_int 0
  | h :: t -> (
    let rec sol ans left right w = (
      let d = (right - left)*2 + 7 in
      match w with
        | [] -> d + ans
        | p :: q ->
          if p - right < 4 then sol ans left p q
          else sol (ans + d) p p q)
    in sol 0 h h t |> print_int)
;;
