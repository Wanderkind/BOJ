open Printf
open String;;

let rec ten n =
  if n==0 then 1
  else (ten (n-1))*10

let rec elv n =
  if n==0 then 0
  else (elv (n-1))*10 + 1

let f a =
  let n = (length @@ string_of_int a) - 1 in 
    n*(ten n) - elv n + (n+1)*(a-(ten n)+1);;

let a = read_int() in
  printf "%d\n" (f a);;
