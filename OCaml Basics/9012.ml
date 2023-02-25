let rec f good n =
  let c = Scanf.scanf "%c" @@ fun c -> c in match c with
  | '(' -> f good @@ n + 1
  | ')' -> if n = 0 then f false 0 else f good @@ n - 1
  | _   -> if n = 0 && good then "YES" else "NO" in
for i = 1 to Scanf.scanf "%d\n" @@ fun n -> n do
  f true 0 |> print_endline
done
