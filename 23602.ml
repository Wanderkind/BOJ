Scanf.scanf "%f %f %f\n%f %f %f\n" @@ fun aa bb cc a b c ->
  let (kk, k) = (cc/.(aa*.aa +. bb*.bb), c/.(a*.a +. b*.b)) in
  let (pp, qq, p, q) = (kk*.aa, kk*.bb, k*.a, k*.b) in
  let h a b c d = hypot a b +. hypot c d +. hypot (a -. c) (b -. d) in
  if a*.bb = aa*.b then print_float @@ h pp qq p q else
    let (x, y) = ((bb*.c -. b*.cc)/.(bb*.a -. b*.aa), (a*.cc -. aa*.c)/.(bb*.a -. b*.aa)) in
    let d ii i =
      let (ss, tt, s, t) = (
        ii*.x +. (1. -. ii)*.pp,
        ii*.y +. (1. -. ii)*.qq,
        i*.x +. (1. -. i)*.p,
        i*.y +. (1. -. i)*.q
      ) in h ss tt s t in
    let u = [
      (0., 0.); (1., 0.); (1., 1.); (0., 1.);
      (-1., 1.); (-1., 0.); (-1., -1.); (0., -1.); (1., -1.)] in
    let rec pow = function 0 -> 0.25 | z -> (pow @@ z - 1)/.2. in
    let rec grad_desc ii i z =
      let w = pow z in
      let rec listify = function
      | [] -> []
      | h :: t -> d (ii +. w*.(fst h)) (i +. w*.(snd h)) :: listify t in
      let l = listify u in
      let rec minl = function
      | [] -> infinity
      | h :: t -> min h @@ minl t in
      let m = minl l in
      let rec find x = function
        | [] -> -1
        | h :: t -> if x = h then 0 else 1 + find x t in
      let index = find m l in
      let (xx, yy) = let pair = List.nth u index in (fst pair, snd pair) in
      if m = List.nth l 0 then
        if z = 20 then d ii i else grad_desc ii i @@ z + 1
      else grad_desc (ii +. xx*.w) (i +. yy*.w) z in
      grad_desc 0.5 0.5 0 |> print_float
