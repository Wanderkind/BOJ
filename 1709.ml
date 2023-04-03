let n = read_int () in
let d = n/2 in
let r = d*d in
let rec f x y acc =
  match y with
  | 0 -> acc
  | t -> (
    if x*x + t*t = r then f x (t - 1) @@ acc + 1
    else if (x + 1)*(x + 1) + t*t > r then f x (t - 1) acc
    else f (x + 1) y acc
  ) in
let a = f 0 (d - 1) 0 in
4*(n - a - 1) |> print_int
