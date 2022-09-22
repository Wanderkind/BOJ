open Printf
open Scanf
;;
let f a b n w =
  if a=b then (if n=2 && a+b=w then 1 else -1)
  else if (w-a*n) mod (b-a)!=0 then -1
  else
      let y = (w-a*n)/(b-a) in
          if y<=0 || n<=y then -1
          else y
;;
scanf "%d %d %d %d\n"
  (fun a b n w -> let r = f a b n w in
    if r = -1 then printf "%d" (-1)
    else printf "%d %d\n" (n-r) (r))
;;
