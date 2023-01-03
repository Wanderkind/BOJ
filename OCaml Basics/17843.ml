open Scanf
open Printf
open Stdlib
;;
let ang p q =
  let k = abs_float (p-.q)
  in min k (360.-.k)
let f h m s =
  let hh = 30.*.h +. 0.5*.(m +. s/.60.) in
  let mm = 6.*.(m +. s/.60.) in
  let ss = 6.*.s in
  let (a, b, c) = (ang hh mm, ang mm ss, ang ss hh) in
  min (min a b) c
;;
for i=1 to read_int() do
  scanf "%f %f %f\n" (fun h m s -> printf "%f\n" (f h m s))
done
;;
