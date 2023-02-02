open Scanf
open Printf
;;
let rec rz n =
  if n mod 10 <> 0 then n
  else rz (n/10)
;;
let sol n =
  let rec f n =
    if n = 1 then 1
    else
      let rec g n =
      if n mod 10000 = 0 then (g (n/10)) mod 10000
      else n mod 10000 in
    (f (n-1) * n) |> g |> rz in
  (f n) mod 10
;;
for i = 1 to read_int() do
  scanf "%d\n" (fun n -> n |> sol |> printf "%d\n")
done
;;
