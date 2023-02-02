open Scanf
open Printf
;;
let f n =
  if n = 0 then 0 else
  let fin n =
    let rec rz n =
      if n mod 10 <> 0 then n
      else rz (n/10) in
    rz n < 10 in
  let rec round n k =
    let r = n mod k in
    if r = 0 then round n (k*10)
    else if r < k/2 then n - r
    else n + k - r in
  let rec doit n =
    if fin n then n
    else (round n 10) |> doit in
  doit n
;;
scanf "%d\n" (fun n -> n |> f |> printf "%d\n")
;;
