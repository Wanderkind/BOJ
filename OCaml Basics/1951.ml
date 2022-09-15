open Printf
open String
;;
let ( ** ) a b = Int64.mul a b
let ( ++ ) a b = Int64.add a b
let ( -- ) a b = Int64.sub a b
let ( // ) a b = Int64.div a b
let ( %% ) a b = Int64.rem a b
let long x = Int64.of_int x
;;
let rec ten n =
  if n=0L then 1L
  else (ten (n--1L))**10L
;;
let rec elv n =
  if n=0L then 0L
  else (elv (n--1L))**10L ++ 1L
;;
let f a =
  let n = long (length @@ string_of_int a) -- 1L in 
    n**(ten n) -- elv n ++ (n++1L)**((long a)--(ten n)++1L)
;;
let a = read_int() in
  printf "%Ld\n" ((f a) %% 1234567L)
;;
