open Scanf
open Printf
;;
let rec f h y =
  if y = 0 then h else let a = max h (f (21*h/20) (y-1)) in
  if y < 3 then a else let b = max a (f ( 6*h/ 5) (y-3)) in
  if y < 5 then b else let c = max b (f (27*h/20) (y-5)) in
  c
;;
scanf "%d %d\n" (fun h y -> f h y |> printf "%d\n")
;;
