open Scanf
open Printf
;;
let rec pow n k =
  if k=0 then 1
  else n*(pow n (k-1))
;;
let rec comb a b =
  if b=0 || a=b then 1
  else comb (a-1) (b-1) + comb (a-1) b
;;
let f _ =
  scanf "%d %d %d %d %d\n" (fun r s x y w ->
    let g i = (comb y i)*(pow (s-r+1) i)*(pow (r-1) (y-i)) in
    let rec h p q = if p=q then g q else (h p (q-1)) + g q in
    let a = w*(h x y) in
    if a > pow s y then printf "yes\n" else printf "no\n"
  )
;;
for i=1 to read_int() do
  f()
done
;;
