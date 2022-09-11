open Scanf
open Printf
;;

let f (a,b) =
  if a=b then (a,b)
  else if a>b then (a-b,b)
  else (a,b-a)
;;

let rec g (a,b) =
  if a=b then 1
  else g (f (a,b)) + 1
;;

scanf "%d %d\n" (fun a b-> printf "%d\n" (g (a,b)))
;;
