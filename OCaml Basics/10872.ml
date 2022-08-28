open Scanf
open Printf;;
let rec fact n = 
  if n = 0 then 1
  else n*fact(n-1);;
scanf "%d\n" (fun n -> printf "%d\n" (fact n))
