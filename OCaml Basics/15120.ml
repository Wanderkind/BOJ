open Printf
open Scanf
;;
let rec q a b c d e f=
  let x = a*.1. +. b*.2. +. c*.3. +. d*.4. +. e*.5. +. f*.6. -. 3.5 in
    let m = max a (max b (max c (max d (max e f)))) in x/.m
;;
scanf "%f %f %f %f %f %f\n"
  (fun a b c d e f-> printf "%.3f\n" (abs_float @@ q a b c d e f))
;;
