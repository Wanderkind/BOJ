open Scanf
open Printf
open List
open Int64
;;
let rec f n =
  if n < 2L then [rem n 2L]
  else f (div n 2L) @ [rem n 2L]
;;
scanf "%Ld\n" (
  fun n ->
    let a = f n in
    for i=0 to length a -1 do
      printf "%Ld" (nth a i)
    done
)
;;
