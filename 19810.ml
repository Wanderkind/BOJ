open Printf;;

let n = read_int() in
  printf "%d\n" (n*((n-1)/2) - 2*(if n mod 3 = 0 then (n/3) else 0));;
