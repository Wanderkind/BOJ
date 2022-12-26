open Scanf
open Printf
;;
scanf "%d\n" (
  fun n ->
    let s = (1.+.sqrt(1.+.8.*.(float_of_int n)))/.2. |> ceil |> int_of_float
      in let d = s*(s-1)/2-n+1
        in printf "%d " (d); printf "%d\n" (s-d)
)
;;
