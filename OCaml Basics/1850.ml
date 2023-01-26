open Scanf
open Printf
open Int64
;;
let ( + ) a b = add a b
let ( - ) a b = sub a b
let ( * ) a b = mul a b
let ( / ) a b = div a b
let ( % ) a b = rem a b
;;
let rec gcd a b = if b = 0L then a else gcd b (a%b)
let sol n =
  for i=1 to to_int n do
    print_int 1
  done
;;
scanf "%Ld %Ld\n" (fun a b -> gcd a b |> sol)
;;
