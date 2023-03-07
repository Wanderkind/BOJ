let sol x =
  let rec f a b = function
  | 0 -> b
  | n -> (
    match Scanf.scanf "%c" @@ fun c -> c with
    | 'Z' -> f (a + 1) b @@ n - 1
    |  _  -> f 0 (b + (a + 2)/3) @@ n - 1
  ) in f 0 0 @@ x + 1
in read_int () |> sol |> print_int
