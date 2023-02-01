open Scanf
open Printf
open Float
;;
let sol _ =
  scanf "%f %f\n" (fun l r ->
    let area = r *. pi *. sqrt (r*.r -. l*.l) /. 4. in
      (area /. 100. |> round |> to_int) * 100 |> printf "%d\n"
  )
;;
for i = 1 to read_int() do
  sol()
done
;;
