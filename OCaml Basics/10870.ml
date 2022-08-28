open Scanf
open Printf;;
let rec fib n = 
  if n<2 then n
  else fib(n-2)+fib(n-1);;
scanf "%d\n" (fun n -> printf "%d\n" (fib n))
