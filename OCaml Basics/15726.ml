open Scanf
open Printf;;

scanf "%d %d %d" (fun a b c-> printf "%d" (if b>c then a*b/c else a*c/b))
