open Scanf
open Printf;;

scanf "%f %f\n" (fun h v ->
  let t = atan(v/.h)/.2. in
    printf "%.2f %.2f\n" (h/.cos(t)/.2.) (v*.cos(t)-.h*.sin(t))
)
