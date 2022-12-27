open Scanf
open Printf
;;
scanf "%d %d\n%d %d\n%d\n" (fun w h p q t ->
  let (x, y) = (p+t, q+t) in
  let (u, v) = (x mod w, y mod h) in
  let (a, b) = (u+((x/w) mod 2)*(w-2*u), v+((y/h) mod 2)*(h-2*v)) in
  printf "%d %d\n" a b
)
;;
