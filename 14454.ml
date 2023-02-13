open Printf
open Scanf
open Int64
;;
let ( ** ) a b = mul a b in
let ( -- ) a b = sub a b in
let (s, n) = scanf "%s %Ld\n" (fun s n -> (s, n)) in
let len = s |> String.length |> of_int in
let rec st (l : int64) (k : int64) (t : int) =
  if k <= l then t
  else st (2L**l) k (t + 1) in
let rec f n =
  let s = st len n 0 in
  match s with
  | 0 -> n
  | x ->
    let k = n -- (let rec pow = function 1 -> len | x -> pow (x-1) ** 2L in pow s) -- 1L in
    (if k = 0L then n -- 1L else k) |> f in
let k = n |> f |> to_int in
print_char s.[(k - 1) mod to_int len]
;;
