let rec stack ad temp point lst =
  let c = Scanf.scanf "%c" (fun c -> c) in
  let on = temp > 0 in
  match c with
  | '(' -> stack true (if on then temp*2 else temp+2) point @@ 2 :: lst
  | '[' -> stack true (if on then temp*3 else temp+3) point @@ 3 :: lst
  | ')' -> (
    match lst with
    | 2 :: t -> stack false (temp/2) (if ad then point+temp else point) t
    | _ -> 0)
  | ']' -> (
    match lst with
    | 3 :: t -> stack false (temp/3) (if ad then point+temp else point) t
    | _ -> 0)
  | _ -> (
    match lst with
    | [] -> point
    | _ -> 0)
in stack false 0 0 [] |> print_int
