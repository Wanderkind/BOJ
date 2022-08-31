open Scanf
open Printf;;
 
let s a b =
  if a>b then a-b
  else 0;;

scanf "%d %d %d\n%d %d %d" (fun a b c d e f -> printf "%d\n" ((s d a) + (s e b) + (s f c)))
