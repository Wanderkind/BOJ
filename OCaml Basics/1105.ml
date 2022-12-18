open Scanf
open Printf
;;
let rec common (l, r) =
  if l = r then l
  else common (l/10, r/10)
;;
let rec eight n =
  if n = 0 then 0
  else if n mod 10 = 8 then 1 + eight (n/10)
  else eight (n/10)
;;
scanf "%d %d\n" (fun l r -> printf "%d\n" (common (l, r) |> eight))
;;
