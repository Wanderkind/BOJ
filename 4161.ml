let knight p q =
  let u, v = abs p, abs q in
  let a, b = if u > v then v, u else u, v in
  if a = 0 && b < 4 then if b mod 2 = 0 then b else 3 else
  if a = b && b < 4 then if b mod 2 = 0 then 2*b else 2 else
  if 2*a <= b then if a mod 2 = 0 then b - 2*(b/4) else b - 1 - 2*((b - 2)/4) else
  let c = a + b in if c mod 2 = 0 then 2*((c/2 + 2)/3) else 1 + 2*((c/2 + 1)/3)
;;

let main () =
  let rec sol () =
    try (Scanf.scanf "%d %d\n" @@ fun x y -> knight x y |> Printf.printf "%d\n"; sol ())
    with | _ -> ()
  in sol ()
;;

let () = main ()
;;
