let rec stack ad temp point lst =
  let c = Scanf.scanf "%c" (fun c -> c) in
  let k w = if temp > 0 then temp*w else temp+w in 
  match c with
  | '(' -> stack true (k 2) point @@ 2 :: lst
  | '[' -> stack true (k 3) point @@ 3 :: lst
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
