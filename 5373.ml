open Scanf
open Printf
;;

type face = {
  s1: char; s2: char; s3: char;
  s4: char; s5: char; s6: char;
  s7: char; s8: char; s9: char
};;

type configuaration = {
           b: face;
  l: face; u: face; r: face; d: face;
           f: face
};;

let initial = {
  b = {
    s1 = 'o'; s2 = 'o'; s3 = 'o';
    s4 = 'o'; s5 = 'o'; s6 = 'o';
    s7 = 'o'; s8 = 'o'; s9 = 'o'};
  l = {
    s1 = 'g'; s2 = 'g'; s3 = 'g';
    s4 = 'g'; s5 = 'g'; s6 = 'g';
    s7 = 'g'; s8 = 'g'; s9 = 'g'};
  u = {
    s1 = 'w'; s2 = 'w'; s3 = 'w';
    s4 = 'w'; s5 = 'w'; s6 = 'w';
    s7 = 'w'; s8 = 'w'; s9 = 'w'};
  r = {
    s1 = 'b'; s2 = 'b'; s3 = 'b';
    s4 = 'b'; s5 = 'b'; s6 = 'b';
    s7 = 'b'; s8 = 'b'; s9 = 'b'};
  d = {
    s1 = 'y'; s2 = 'y'; s3 = 'y';
    s4 = 'y'; s5 = 'y'; s6 = 'y';
    s7 = 'y'; s8 = 'y'; s9 = 'y'};
  f = {
    s1 = 'r'; s2 = 'r'; s3 = 'r';
    s4 = 'r'; s5 = 'r'; s6 = 'r';
    s7 = 'r'; s8 = 'r'; s9 = 'r'}
};;

let clockwise f = {
  s1 = f.s7; s2 = f.s4; s3 = f.s1;
  s4 = f.s8; s5 = f.s5; s6 = f.s2;
  s7 = f.s9; s8 = f.s6; s9 = f.s3
};;

let counterclockwise f = {
  s1 = f.s3; s2 = f.s6; s3 = f.s9;
  s4 = f.s2; s5 = f.s5; s6 = f.s8;
  s7 = f.s1; s8 = f.s4; s9 = f.s7
};;

let rotate config = function
  | "B+" -> (let cl, cu, cr, cd = config.l, config.u, config.r, config.d in
      {config with b = clockwise config.b;
      l = {config.l with s1 = cu.s1; s2 = cu.s2; s3 = cu.s3};
      u = {config.u with s1 = cr.s1; s2 = cr.s2; s3 = cr.s3};
      r = {config.r with s1 = cd.s1; s2 = cd.s2; s3 = cd.s3};
      d = {config.d with s1 = cl.s1; s2 = cl.s2; s3 = cl.s3}})
  | "B-" -> (let cl, cu, cr, cd = config.l, config.u, config.r, config.d in
        {config with b = counterclockwise config.b;
        l = {config.l with s1 = cd.s1; s2 = cd.s2; s3 = cd.s3};
        u = {config.u with s1 = cl.s1; s2 = cl.s2; s3 = cl.s3};
        r = {config.r with s1 = cu.s1; s2 = cu.s2; s3 = cu.s3};
        d = {config.d with s1 = cr.s1; s2 = cr.s2; s3 = cr.s3}})
  | "L+" -> (let cd, cu, cf, cb = config.d, config.u, config.f, config.b in
        {config with l = clockwise config.l;
        d = {config.d with s9 = cf.s1; s6 = cf.s4; s3 = cf.s7};
        f = {config.f with s1 = cu.s1; s4 = cu.s4; s7 = cu.s7};
        u = {config.u with s1 = cb.s1; s4 = cb.s4; s7 = cb.s7};
        b = {config.b with s1 = cd.s9; s4 = cd.s6; s7 = cd.s3}})
  | "L-" -> (let cd, cu, cf, cb = config.d, config.u, config.f, config.b in
        {config with l = counterclockwise config.l;
        d = {config.d with s9 = cb.s1; s6 = cb.s4; s3 = cb.s7};
        f = {config.f with s1 = cd.s9; s4 = cd.s6; s7 = cd.s3};
        u = {config.u with s1 = cf.s1; s4 = cf.s4; s7 = cf.s7};
        b = {config.b with s1 = cu.s1; s4 = cu.s4; s7 = cu.s7}})
  | "U+" -> (let cl, cf, cr, cb = config.l, config.f, config.r, config.b in
        {config with u = clockwise config.u;
        l = {config.l with s3 = cf.s1; s6 = cf.s2; s9 = cf.s3};
        f = {config.f with s1 = cr.s7; s2 = cr.s4; s3 = cr.s1};
        r = {config.r with s1 = cb.s7; s4 = cb.s8; s7 = cb.s9};
        b = {config.b with s7 = cl.s9; s8 = cl.s6; s9 = cl.s3}})
  | "U-" -> (let cl, cf, cr, cb = config.l, config.f, config.r, config.b in
        {config with u = counterclockwise config.u;
        l = {config.l with s3 = cb.s9; s6 = cb.s8; s9 = cb.s7};
        f = {config.f with s1 = cl.s3; s2 = cl.s6; s3 = cl.s9};
        r = {config.r with s1 = cf.s3; s4 = cf.s2; s7 = cf.s1};
        b = {config.b with s7 = cr.s1; s8 = cr.s4; s9 = cr.s7}})
  | "F+" -> (let cl, cu, cr, cd = config.l, config.u, config.r, config.d in
        {config with f = clockwise config.f;
        l = {config.l with s7 = cd.s7; s8 = cd.s8; s9 = cd.s9};
        u = {config.u with s7 = cl.s7; s8 = cl.s8; s9 = cl.s9};
        r = {config.r with s7 = cu.s7; s8 = cu.s8; s9 = cu.s9};
        d = {config.d with s7 = cr.s7; s8 = cr.s8; s9 = cr.s9}})
  | "F-" -> (let cl, cu, cr, cd = config.l, config.u, config.r, config.d in
        {config with f = counterclockwise config.f;
        l = {config.l with s7 = cu.s7; s8 = cu.s8; s9 = cu.s9};
        u = {config.u with s7 = cr.s7; s8 = cr.s8; s9 = cr.s9};
        r = {config.r with s7 = cd.s7; s8 = cd.s8; s9 = cd.s9};
        d = {config.d with s7 = cl.s7; s8 = cl.s8; s9 = cl.s9}})
  | "R+" -> (let cd, cu, cf, cb = config.d, config.u, config.f, config.b in
        {config with r = clockwise config.r;
        d = {config.d with s7 = cb.s3; s4 = cb.s6; s1 = cb.s9};
        f = {config.f with s3 = cd.s7; s6 = cd.s4; s9 = cd.s1};
        u = {config.u with s3 = cf.s3; s6 = cf.s6; s9 = cf.s9};
        b = {config.b with s3 = cu.s3; s6 = cu.s6; s9 = cu.s9}})
  | "R-" -> (let cd, cu, cf, cb = config.d, config.u, config.f, config.b in
        {config with r = counterclockwise config.r;
        d = {config.d with s7 = cf.s3; s4 = cf.s6; s1 = cf.s9};
        f = {config.f with s3 = cu.s3; s6 = cu.s6; s9 = cu.s9};
        u = {config.u with s3 = cb.s3; s6 = cb.s6; s9 = cb.s9};
        b = {config.b with s3 = cd.s7; s6 = cd.s4; s9 = cd.s1}})
  | "D+" -> (let cl, cf, cr, cb = config.l, config.f, config.r, config.b in
        {config with d = clockwise config.d;
        l = {config.l with s1 = cb.s3; s4 = cb.s2; s7 = cb.s1};
        f = {config.f with s7 = cl.s1; s8 = cl.s4; s9 = cl.s7};
        r = {config.r with s3 = cf.s9; s6 = cf.s8; s9 = cf.s7};
        b = {config.b with s1 = cr.s3; s2 = cr.s6; s3 = cr.s9}})
  | "D-" -> (let cl, cf, cr, cb = config.l, config.f, config.r, config.b in
        {config with d = counterclockwise config.d;
        l = {config.l with s1 = cf.s7; s4 = cf.s8; s7 = cf.s9};
        f = {config.f with s7 = cr.s9; s8 = cr.s6; s9 = cr.s3};
        r = {config.r with s3 = cb.s1; s6 = cb.s2; s9 = cb.s3};
        b = {config.b with s1 = cl.s7; s2 = cl.s4; s3 = cl.s1}})
  | _ -> assert false
;;

let rec move config = function
  | [] -> config
  | h :: t -> move (rotate config h) t
;;

let rec arr = function
  | 1 -> [scanf "%s\n" @@ fun s -> s]
  | x -> scanf "%s " @@ fun s -> s :: (arr @@ x - 1)
;;

let sol () =
  let result = move initial @@ scanf "%d\n" @@ fun n -> arr n in
  let top = result.u in
  printf "%c%c%c\n" top.s1 top.s2 top.s3;
  printf "%c%c%c\n" top.s4 top.s5 top.s6;
  printf "%c%c%c\n" top.s7 top.s8 top.s9
;;

let main () = for i = 1 to read_int () do sol () done
;;

let () = main ()
;;
