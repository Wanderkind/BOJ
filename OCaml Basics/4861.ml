open Scanf
open Printf
;;
let dfr n =
  if n > 4 then n-1 else n
;;
let rec f n =
  if n < 10 then dfr n
  else 9*(f (n/10)) + f (n mod 10)
;;
let break = ref false in
  while not !break do
    let n = read_int() in
      if n = 0 then break := true
      else printf "%d: %d\n" (n) (f n)
  done
;;
