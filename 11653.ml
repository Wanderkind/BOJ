open Scanf
open Printf
open List
;;
let rec pow a b =
  if b = 0 then 1
  else a*(pow a (b-1))
;;
let rec ar p q =
  if q = 0 then []
  else ar p (q-1) @ [p]
;;
let pf_array n =
  let rec factor n k =
    let rec howmany n k =
      if n mod k > 0 then 0
      else howmany (n/k) k + 1 in
    let h = howmany n k in
    if h = 0 then factor n (k+1)
    else
      if n = pow k h then ar k h
      else ar k h @ factor (n/(pow k h)) (k+1) in
  factor n 2
;;
let n = read_int() in
let a = if n=1 then [] else n |> pf_array in
for i=0 to length a - 1 do
  printf "%d\n" (nth a i)
done
;;
