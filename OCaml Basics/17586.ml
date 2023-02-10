open Printf
open Scanf
open Int64
;;
let rec gcd a b =
  if b = 0L then a
  else gcd b (rem a b) in
scanf "%Ld %Ld\n" (fun a b ->
  let g = gcd a b in
  let ans = if rem (add (div a g) (div b g)) 2L = 1L then 0L else g in
  ans |> printf "%Ld\n")
;;
