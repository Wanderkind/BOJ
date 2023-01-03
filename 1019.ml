open Scanf
open Printf
;;
let rec pow a b =
  if b=0 then 1
  else a*(pow a (b-1))
;;
let rec ls n =
  if n < 10 then 0
  else ls (n/10) + 1
;;
let f n j =
  let rec g k =
    let a k =
      let w = pow 10 k in
      let d = (n/w) mod 10 in
      let s = (n/w/10)*w + n mod w in
      if d > j then (s/w + 1)*w
      else if d < j then (s/w)*w
      else s+1 in
    if k = 0 then a 0
    else g (k-1) + a k in
  n |> ls |> g
;;
let f0 n =
  if n < 10 then 0 else
  let rec g0 k =
    let w = pow 10 k in
    let a0 k =
      let d = (n/w) mod 10 in
      if d > 0 then w-1
      else n mod w in
    let p k = (n/w/10)*w+1-w+(a0 k) in
    if k = 0 then p k
    else g0 (k-1) + p k in
  g0 (ls n -1)
;;
scanf "%d\n" (fun n ->
  printf "%d " (f0 n);
  for i=1 to 9 do
    printf "%d " (f n i)
  done
)
;;
