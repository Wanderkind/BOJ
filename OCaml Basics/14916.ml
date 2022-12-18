open Scanf
open Printf
;;
let rec f n =
  if (n=1 || n=3) then -1
  else if (n mod 2=0) then (n/10)*2 + (n mod 10)/2
  else f (n-5) + 1
;;
scanf "%d\n" (fun n -> printf "%d" (f n))
;;
