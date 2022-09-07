open Scanf
open Printf;;

let rec gcd a b =
  if a == b then a
  else if a > b then gcd (a - b) b
  else gcd a (b - a);;

scanf "%d %d\n%d %d\n" (fun a b c d ->
  let (p,q) = (a*d+b*c,b*d) in
    let g = gcd p q in
      printf "%d %d\n" (p/g) (q/g)
)
