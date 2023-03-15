let rec f cnt s pair =
  let (p, q) = pair in
  match Scanf.scanf "%c" @@ fun c -> c with
  | '(' -> if s = -1 then (cnt/2 + 1, -1, 0) else f (cnt + 1) (s + 1) (p + 1,  q)
  | ')' -> f (cnt + 1) (s - 1) @@ if s = 1 then (0, q + p/2 + 1) else (p + 1, q)
  |  _  -> (cnt/2 + 1, s, q)
;;
let (a, s, q) = f 0 0 (0, 0) in
(if s = -1 then a else a - q) |> print_int
;;
