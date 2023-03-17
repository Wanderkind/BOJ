open Scanf
open List;;
scanf "%d %d\n" @@ fun n m ->
  let rec f = function
  | 0 -> scanf "%c" @@ fun c -> []
  | m -> scanf "%c" @@ fun c -> c :: f (m - 1) in
  let rec g = function
  | 0 -> []
  | n -> f m :: g (n - 1) in
  let ls = g n in
  let rec h j = function
  | 0 -> []
  | n -> nth (nth ls @@ n - 1) j :: h j (n - 1) in
  let rec l = function
  | 0 -> []
  | m -> h (m - 1) n :: l (m - 1) in
  let nwl = l m in
  let rec fin = function
  | [] -> true
  | h :: t -> (
    match h with
    | 'o' -> (
      match t with
      | [] -> fin t
      | h' :: t' -> (
        match h' with
        | '.' -> false
        |  _  -> fin t
      )
    )
    |  _  -> fin t
  ) in
  let rec drop = function
  | [] -> []
  | h :: t -> (
    match h with
    | 'o' -> (
      match t with
      | [] -> h :: t
      | h' :: t' -> (
        match h' with
        | '.' -> '.' :: 'o' :: drop t'
        |  _  -> h :: drop t
      )
    )
    |  _  -> h :: drop t
  ) in
  let rec grav lst =
  if fin lst then lst
  else lst |> drop |> grav in
  let rec conv = function
  | [] -> []
  | h :: t -> grav h :: conv t in
  let res = conv nwl in
  for i = 0 to n - 1 do
    for j = 1 to m do
      print_char @@ nth (nth res (m - j)) i
    done; print_newline ()
  done;;
