open Scanf
open Printf
;;
let f _ =
  scanf "%d %d %d\n" (fun y m d ->
    if y<1989 then printf "Yes\n"
    else if y>1989 then printf "No\n"
    else
      if m<2 then printf "Yes\n"
      else if m>2 then printf "No\n"
      else
        if d<28 then printf "Yes\n"
        else printf "No\n"
  )
;;
for i=1 to read_int() do
  f()
done
;;
