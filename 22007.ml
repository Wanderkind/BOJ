open Scanf
open Printf
open Int64
open Stdlib
;;
let ( ** ) a b = mul a b
let ( ++ ) a b = add a b
let ( -- ) a b = sub a b
let ( // ) a b = div a b
let ( %% ) a b = rem a b
;;
let rec pow a b = 
  if b = 0 then 1L
  else a**(pow a (b-1))
;;
let log k n =
  let rec g p q r =
    if p < (pow q r) then r-1
    else g p q (r+1)
  in g n k 1
;;
let f a b =
  let cmpr at b k =
    let a = at--1L in
    let (aa, bb) = (log k a, log k b) in
    if aa < bb then bb
    else
      let rec down p q k init =
        let i = pow k init in
        if p//i < q//i then init
        else down p q k (init-1) in
      down a b k aa in
  min (cmpr a b 2L) (cmpr a b 5L)
;;
scanf "%Ld %Ld\n" (fun a b -> printf "%d\n" (f a b))
;;
