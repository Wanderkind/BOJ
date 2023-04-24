let rec l = function
| 1 -> Scanf.scanf "%s\n" @@ fun s -> [s]
| x -> Scanf.scanf "%s "  @@ fun s -> s :: l (x - 1) in
let lst = l @@ read_int () in
let isCheese s =
  let len = String.length s in
  if len < 6 then false else
  String.sub s (len - 6) 6 = "Cheese" in
let rec f v = function
| [] -> List.length v
| h :: t -> f (if isCheese h && not (List.mem h v) then h :: v else v) t in
print_endline @@ if f [] lst > 3 then "yummy" else "sad"
