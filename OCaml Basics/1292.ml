open Scanf
open Printf
;;
let s n = (-1.+.sqrt(1.+.8.*.(float_of_int n)))/.2. |> ceil |> int_of_float
;;
let rec k a b =
  if a>b then 0
  else k a (b-1) + b*b
;;
let f a b =
  let (aa, bb) = (s a, s b) in
    if aa=bb then aa*(b-a+1)
    else 
      let w = aa*(aa*(aa+1)/2-a+1) + bb*(b-bb*(bb-1)/2) in
      w + k (aa+1) (bb-1)
;;
scanf "%d %d\n" (fun p q ->
  printf "%d\n" (f p q)
)
;;
