open Scanf
open Printf
;;
let sol n =
  let rec f a b lst =
  if b = n then (a, lst) else
  if n mod b = 0 then f (a + b) (b + 1) @@ lst @ [b] else f a (b + 1) lst
  in let (s, l) = f 0 1 [] in
  let rec out = function
  | [] -> ()
  | [x] -> printf "%d\n" x
  | h :: t -> printf "%d + " h; out t in
  if s = n then (printf "%d = " n; out l)
  else printf "%d is NOT perfect.\n" n in
let rec main _ =
  match read_int () with
  | -1 -> ()
  | x  -> sol x; main () in
main ()
;;
