let rec f good max point =
  match Scanf.scanf "%c" (fun c -> c) with
  | '(' -> f true (max + 1) point
  | ')' -> f false (max - 1) @@ point + (if good then max else 1)
  |  _  -> point
in f false (-1) 0 |> print_int
