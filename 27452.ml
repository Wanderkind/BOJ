open Printf
open Scanf
open List
open Int64
;;
let ( + ) a b = add a b
let ( - ) a b = sub a b
let ( * ) a b = mul a b
let ( / ) a b = div a b
let ( % ) a b = rem a b
;;
let rec bin n =
  if n < 2L then [n % 2L = 1L]
  else bin (n/2L) @ [n % 2L = 1L]
;;
let cut = function
  | [] -> [] 
  | _ :: xs -> xs
;;
let mm a b =
  let ((p, q), (r, s)) = a in
  let ((t, u), (v, w)) = b in
  ((p*t+q*v, p*u+q*w), (r*t+s*v, r*u+s*w))
;;
let l n =
  let f n =
    let rec ff p q r =
      if length r = 1 then
        if nth r 0 then (mm p q, q)
        else (p, q)
      else
        let (pp, qq) = ff p q (cut r) in
        let qqq = mm qq qq in
        if nth r 0 then (mm pp qqq, qqq)
        else (pp, qqq) in
    ff ((1L, 0L), (0L, 1L)) ((1L, 1L), (1L, 0L)) (bin n) |> fst |> fst |> snd
  in 4L*(f n) - 2L 
;;
let (l83, l84) = (l 83L, l 84L) in
let rec sol n k =
  let ln = l n in
  if n < 85L then
    if k > ln then printf "0\n" else
      if k = 1L then printf "(\n"
      else if k = ln then printf ")\n"
      else
        let (status, loc) = (n - 2L, k - 1L) in
        if loc <= l status then sol status loc
        else sol (status + 1L) (loc - l status)
  else
    let d = (n - 83L)/2L in
    let newk = k - d in
    if newk < 1L then printf "(\n"
    else if n % 2L = 1L then
      if newk > l83 then sol 84L (newk - l83)
      else sol 83L newk
    else
      if newk > l84 then sol 85L (newk - l84)
      else sol 84L newk
in for i = 1 to read_int() do
  scanf "%Ld %Ld\n" (fun n k -> sol n k)
done
;;
