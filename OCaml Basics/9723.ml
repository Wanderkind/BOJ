open Scanf
open Printf
open List
open Int64
;;
let f a b c =
  if a*a = b*b + c*c ||
     b*b = c*c + a*a ||
     c*c = a*a + b*b then printf "YES\n"
  else printf "NO\n"
;;
for i=1 to read_int() do
  printf "Case #%d: " i;
  scanf "%d %d %d\n" (fun a b c -> (f a b c))
done
;;
