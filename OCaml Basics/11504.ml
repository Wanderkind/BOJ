open Scanf
;;
let sol _ =
  scanf "%d %d\n" @@ fun n x ->
    let rec ten = function 0 -> 1 | n -> 10*(ten @@ n - 1) in
    let rec bound = function 1 -> scanf "%d\n" @@ fun t -> t | x -> scanf "%d " @@ fun t -> t*(ten @@ x - 1) + (bound @@ x - 1) in
    let (r, l) = (bound x, bound x) in
    let rec intarr = function 1 -> [scanf "%d\n" @@ fun t -> t] | x -> scanf "%d " @@ fun t -> t :: intarr (x - 1) in
    let lst = intarr n in
    let rec f i = function 0 -> 0 | x -> (List.nth lst @@ (i + x) mod n) + 10*(f i @@ x - 1) in
    let rec g = function 0 -> 0 | n -> let t = f n x in (let k = if l <= t && t <= r then 1 else 0 in k + g (n - 1))
    in g n |> Printf.printf "%d\n"
;;
for i = 1 to read_int () do sol () done
;;
