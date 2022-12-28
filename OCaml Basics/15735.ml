open Scanf
open Printf
;;
let g n =
  n*(n+1)/2
;;
let f n =
  let rec top n =
    if n = 0 then 0
    else g n + top (n-1) in
  let rec bot n =
    if n < 2 then n
    else g n + bot (n-2) in
  top n + bot (n-1)
;;
scanf "%d\n" (fun n ->
  printf "%d\n" (f n)
)
;;
