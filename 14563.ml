open Scanf
open Printf
open List
;;
let rec pow a b =
  if b = 0 then 1
  else a*(pow a (b-1))
;;
let rec ss p q =
  if q = 0 then 1
  else ss p (q-1) + pow p q
;;
let pf n =
  if n=1 then 1 else
  let rec factor n k =
    let rec howmany n k =
      if n mod k > 0 then 0
      else howmany (n/k) k + 1 in
    let h = howmany n k in
    if h = 0 then factor n (k+1)
    else
      if n = pow k h then ss k h
      else ss k h * factor (n/(pow k h)) (k+1) in
  factor n 2
;;
for i=1 to read_int() do
  scanf "%d " (fun n ->
    let a = pf n - n in
    if a > n then printf "Abundant\n"
    else if a < n then printf "Deficient\n"
    else printf "Perfect\n"
  )
done
;;
