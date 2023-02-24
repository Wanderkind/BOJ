let rec f n =
  match n with
  | 1 -> ["*"]
  | x -> (
    let rec ga = function
    | [] -> []
    | h :: t -> (h ^ h ^ h) :: ga t in
    let rec gb = function
    | [] -> []
    | h :: t -> (
      let rec s = function
      | 0 -> ""
      | x -> s (x - 1) ^ " " in
      let w = s (n/3) in
      (h ^ w ^ h) :: gb t
    ) in
    let z = f @@ x/3 in
    ga z @ gb z @ ga z
  )
;;
read_int() |> f |> let rec p = function [] -> () | h :: t -> print_endline h; p t in p
