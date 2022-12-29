open Scanf
open Printf
;;
let rec f a b =
  if a <= b then b-a
  else if a mod 2=1 then 1 + f (a+1) b
  else 1 + f (a/2) b
;;
scanf "%d %d\n" (fun a b -> printf "%d\n" (f a b))
;;
