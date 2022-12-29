open Scanf
open Printf
;;
let rec pow n k = if k = 0 then 1 else n*(pow n (k-1))
;;
let f n =
  let k = pow 10 n in
  n*k - (k-1)/9
;;
let digits n =
  let v k = f (k-1) < n && n <= f k in
  let rec p k = if v k then k else p (k+1) in
  p 1
;;
let sol n =
  let d = digits n in
  let nn = n - f (d-1) - 1 in
  let rec numm p q = if q=0 then p mod 10 else numm (p/10) (q-1) in
  let num p q = numm p (d-q-1) in
  let rec s k w = if k/d = 0 then num ((pow 10 (d-1))+w) k else s (k-d) (w+1) in
  s nn 0
;;
printf "%d\n" (read_int() |> sol)
;;
