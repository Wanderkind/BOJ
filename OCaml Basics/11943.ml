open Printf
open Scanf
;;
let f a b c d =
  let (p,q) = (a+d,b+c) in min p q
;;
scanf "%d %d\n%d %d\n"
  (fun a b c d -> printf "%d\n" (f a b c d))
;;
