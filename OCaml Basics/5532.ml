open Scanf
open Printf
;;
let ceil a b =
  if a mod b = 0 then a/b else a/b+1
let f l a b c d =
  l - max (ceil a c) (ceil b d)
;;
scanf "%d\n%d\n%d\n%d\n%d\n"
  (fun l a b c d -> printf "%d\n" (f l a b c d))
;;
