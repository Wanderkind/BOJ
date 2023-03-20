Scanf.scanf "%d %d %d\n" @@ fun a d k ->
  let f n = (float_of_int n)/.100. in
  let rec g a t b p =
    let w = t*.b in
    if p >= 1. then a +. w
    else g (a +. p*.w) (t +. 1.) ((1. -. p )*.b) @@ p*.(f k +. 1.) in
  g 0. 1. (float_of_int a) @@ f d |> print_float
