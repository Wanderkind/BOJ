open Scanf
open Printf;;
let ( ** ) a b = Int64.mul a b;;

scanf "%Ld" (fun a -> printf "%Ld" (4L** a))
