let n = read_int () in
let rec f acc = function
| 1 -> Scanf.scanf "%d\n" @@ fun t -> acc lxor t
| x -> Scanf.scanf "%d "  @@ fun t -> f (acc lxor t) @@ x - 1 in
print_string @@ if f 0 n = 0 then "cubelover" else "koosaga"
