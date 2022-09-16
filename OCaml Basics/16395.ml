open Printf
open Scanf
;;
let rec comb n k =
  if k=1 || k=n then 1
  else (comb (n-1) (k-1)) + (comb (n-1) (k))
;;
scanf "%d %d\n" (fun n k -> printf "%d\n" (comb n k))
;;
