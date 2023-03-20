open Int64;;
Scanf.scanf "%Ld %Ld\n" @@ fun a b ->
  let sq n = mul n n in
  let d = sub b a in
  let rec bitfill n =
    if n < 4L then 2L
    else mul 2L @@ bitfill (div n 4L) in
  let isqrt n =
    if n = 1L then 1L else
    let rec binsearch l r =
      let t = div (add l r) @@ 2L in
      if sq t <= n && n < sq @@ add t 1L then t else
      if sq t > n then binsearch l t
      else binsearch t r in
    binsearch 0L @@ bitfill n in
  let k = sub (isqrt b) (isqrt a) in
  if k = 0L then print_int 0 else
  let rec gcd p = function 0L -> p | q -> gcd q @@ rem p q in
  let g = gcd k d in
  Printf.printf "%Ld/%Ld\n" (div k g) (div d g)
