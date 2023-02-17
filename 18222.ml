open Int64;;
let sol n =
  let rec two a n =
    if n <= a then div a 2L else n |> two @@ mul 2L a in
  let rec f = function
    1L -> 0 | n -> let x = two 1L n in sub n x |> f |> ( - ) 1
  in f n in
Scanf.scanf "%Ld\n" (fun n -> n |> sol |> print_int);;
