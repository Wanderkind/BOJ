open Printf;;
Scanf.scanf "%d %d\n" @@ fun a b ->
  printf "%d\n" (a*b/2*2);
  let p x y = printf "%d %d\n" x y in
  for i = 1 to a do p i 1 done;
  if a mod 2 = 0 then
    for i = 0 to a/2 - 1 do
      for j = 2 to b do p (a - 2*i) j done;
      for j = 0 to b - 2 do p (a - 2*i - 1) (b - j) done;
    done
  else (
    for j = 2 to b do p a j done;
    for i = 0 to a/2 - 2 do
      for j = 0 to b - 2 do p (a - 2*i - 1) (b - j) done;
      for j = 2 to b do p (a - 2*i - 2) j done;
    done;
    p 2 b;
    let r = b mod 2 in
    if r = 0 then (
      p 1 b;
    )
    else (
      p 2 (b - 1);
      p 1 (b - 1););
    for j = 1 to b/2 - 1 do
      p 1 (b - 2*j + 1 - r);
      p 2 (b - 2*j + 1 - r);
      p 2 (b - 2*j - r);
      p 1 (b - 2*j - r);
    done)
