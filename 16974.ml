open Printf
open Scanf
open Int64
;;
let ( + ) a b = add a b
let ( - ) a b = sub a b
let ( * ) a b = mul a b
let ( / ) a b = div a b
let ( % ) a b = rem a b
;;
let rec l = function 0L -> 1L | x -> 2L*(l (x - 1L)) + 3L in
let rec f (n : int64) (x : int64) =
  match n with
  | 0L -> 1L
  | k  -> (
    let w = k - 1L |> l in
    let g = f (k - 1L) in
    let v = g w in
    if      x =        1L then 0L
    else if x <    w + 2L then g (x - 1L)
    else if x =    w + 2L then v + 1L
    else if x < 2L*w + 3L then v + 1L + g (x - w - 2L)
    else                       2L*v + 1L
  )
in scanf "%Ld %Ld\n" (fun n x -> f n x |> printf "%Ld\n")
;;
