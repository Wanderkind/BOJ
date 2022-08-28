open Scanf
open Printf;;
let r _ =
  scanf "%d\n%d\n%d\n%d\n" (fun a b c d -> a+b+c+d)
let main =
  let s = r () in
  printf "%d\n%d" (s / 60) (s mod 60)
