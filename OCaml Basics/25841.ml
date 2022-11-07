open Scanf
open Printf
;;
let last n d =
    if n mod 10 = d then 1 else 0
;;
let rec count n d =
    if n<10 then last n d
    else last n d + count (n/10) d
;;
let rec sol l r d =
    if l = r then count l d
    else count l d + sol (l+1) r d
;;
scanf "%d %d %d\n" (fun l r d ->
    printf "%d\n" (sol l r d)
)
;;
