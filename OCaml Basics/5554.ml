open Scanf
open Printf;;
let ( // ) a b = Int.div a b
let ( %% ) a b = Int.rem a b;;
let r _ =
  scanf "%d\n%d\n%d\n%d\n" (fun a b c d -> a+b+c+d)
let main =
  let s = r () in
  printf "%d\n%d" (s // 60) (s %% 60)
