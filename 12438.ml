open Scanf
open Printf
open Int64
;;
let ( * ) a b = mul a b
let ( + ) a b = add a b
let ( - ) a b = sub a b
let ( / ) a b = div a b
let ( % ) a b = rem a b
;;
let rec gcd a b =
  if b=0L then a
  else gcd b (a%b)
;;
let f a b c =
  let (p, q) = (b/c, b%c) in
  if q = 0L then a*p else
  let g = gcd b c in
  let (bb, cc) = (b/g, c/g) in
  let k = a*bb in
  let t = if k%cc = 0L then 0L else 1L in
  a-1L + k/cc + t - ((a-1L)/cc)
;;
for i=1 to read_int() do
  scanf "%Ld %Ld %Ld\n" (fun a b c ->
    printf "Case #%d: %Ld\n" i (f a b c))
done
;;
