open Scanf
open Printf;;

let m x:int = if x < 10 then 10 else (if x < 100 then 100 else (if x < 1000 then 1000 else (if x < 10000 then 10000 else (if x < 100000 then 100000 else (if x < 1000000 then 1000000 else 10000000)))));;

scanf "%d %d %d %d\n" (fun a b c d -> printf "%d\n" (a*m(b) + c*m(d) + b + d))
