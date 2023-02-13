open Printf
open Scanf
;;
let fl x = float_of_int x in
let sol x y n =
  let h p q r = hypot (fl x -. fl p) (fl y -. fl q) -. fl r in
  let rec f = function
  | 2 -> scanf "%d %d %d\n%d %d %d\n" (fun x1 y1 r1 x2 y2 r2 ->
      let (a, b) = (h x1 y1 r1, h x2 y2 r2) in 
      if a < b then (a, b, 10000.) else (b, a, 10000.))
  | n -> scanf "%d %d %d\n" (fun p q r ->
      let (a, b, c) = f (n-1) in
      let t = h p q r in
      if t < a then (t, a, b)
      else if t < b then (a, t, b)
      else if t < c then (a, b, t)
      else (a, b, c)) in
  let ans = let (a, b, c) = f n in c |> int_of_float in
  max 0 ans in
scanf "%d %d %d\n" (fun x y n -> sol x y n |> print_int)
;;
