open Scanf;;
open List;;

let k = read_int();;

let rec f arp n =
    let (a, b) = arp in match n with
    | 1 -> scanf "%d %d\n" @@ fun dir len -> (dir :: a, len :: b)
    | x -> scanf "%d %d\n" @@ fun dir len -> f (dir :: a, len :: b) @@ x - 1;;

let (d, l) = f ([], []) 6;;

let a j = nth d @@ j mod 6;;
let b j = nth l @@ j mod 6;;

let g i =
    a(i)/3     = a(i + 2)/3 && a(i)/3     = a(i + 4)/3 &&
    a(i + 5)/3 = a(i + 3)/3 && a(i + 5)/3 = a(i + 1)/3 &&
    b(i)     = b(i + 2) + b(i + 4) &&
    b(i + 5) = b(i + 3) + b(i + 1);;

let rec sol t =
    if g t then print_int @@ k*(b(t)*b(t + 5) - b(t + 2)*b(t + 3))
    else sol @@ t + 1;;

sol 0;;
