open Scanf
open Printf;;

let ( ** ) a b = Int64.mul a b
let ( ++ ) a b = Int64.add a b
let ( -- ) a b = Int64.sub a b
let ( // ) a b = Int64.div a b
let ( %% ) a b = Int64.rem a b;;

let rec mul a n =
  if n = 0L then 1L
  else a**(mul a (n--1L));;

let f s k =
  let p = s // k in
    let q = s %% k in
      (mul (p++1L) q) ** (mul p (k--q));;

scanf "%Ld %Ld\n" (fun s k ->
  printf "%Ld\n" (f s k)
);;
