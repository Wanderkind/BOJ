open Scanf
;;
let rec convert pos neg =
  match scanf "%c" @@ fun c -> c with
  | 'X' -> let n = scanf "%d" @@ fun n -> n in convert (pos + (1 lsl (n - 1))) neg
  | '~' -> scanf "%c" @@ fun d -> assert (d = 'X'); let n = scanf "%d" @@ fun n -> n in convert pos (neg + (1 lsl (n - 1)))
  | '\n'-> (pos, neg)
  | _   -> convert pos neg
;;
let sol _ =
  scanf "%d %d\n" @@ fun n m ->
    let nn = 1 lsl n in
    let r x = nn - 1 - x in
    let rec f m = match m with
    | 0 -> []
    | x -> convert 0 0 :: (f @@ x - 1) in
    let l = f m in
    let check pair x = let (a, b) = pair in a land x <> 0 || b land r x <> 0 in
    let rec g x = function
    | [] -> true
    | h :: t -> if not @@ check h x then false else g x t in
    let rec h init =
      if init = nn - 1 then g init l
      else if g init l then true
      else h @@ init + 1 in
    print_endline @@ if h 0 then "satisfiable" else "unsatisfiable"
;;
for i = 1 to read_int () do sol () done
;;
