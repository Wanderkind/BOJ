open Printf;;

let f n = int_of_float @@ (-1.+.sqrt(1.+.8.*.(float_of_int(n))))/.2.;;

let g a i = if (a - i*(i-1)/2) mod i == 0 then 1 else 0;;

let rec m a n =
  if n = 0 then 0
  else m a (n-1) + (g a n);;

let a = read_int() in
  printf "%d" (m a (f a));;
