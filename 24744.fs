open System


let binsearch func left right =
    let rec loop l r =
        let t = (l + r)/2.
        let res = func t
        if abs res < 0.000000001 then t else
        if res < 0 then loop t r
        else loop l t
    loop left right

let main _ =
    let l = Console.ReadLine().Split ' ' |> Array.map float
    let ax, bx, by, cx, cy, cz = l[0], l[1], l[2], l[3], l[4], l[5]
    let alpha r = r*(bx*sqrt(cy*cy + cz*cz) + by*cx + sqrt((bx*cy - by*cx)**2 + cz*cz*(bx*bx + by*by)))/by/cz
    let beta r = r*(cy + sqrt(cy*cy + cz*cz))/cz
    let a, b, c, d = by*cz, (ax - bx)*cz, (bx - ax)*cy + (ax - cx)*by, -ax*by*cz
    let plane x y z = a*x + b*y + c*z + d
    let hypot = a*a + b*b + c*c |> sqrt
    let dist r = ((alpha r, beta r, r) |||> plane) / hypot
    let intersect = binsearch dist 0 100
    let sz = binsearch (fun r -> dist r + r) 0 intersect
    let sx, sy = alpha sz, beta sz
    let s = ax*ax - cx*cx - cy*cy - cz*cz
    let v = ax*ax - bx*bx - by*by
    let m = 2.*(a*cz*by - b*cz*(bx - ax) - c*(cx - ax)*by + c*cy*(bx - ax))
    let x = (b*cz*v - c*cy*v + c*s*by - 2.*d*cz*by)/m
    let y = (-a*cz*v + c*(cx - ax)*v - c*s*(bx - ax) + 2.*d*cz*(bx - ax))/m
    let z = (a*cy*v - a*s*by - b*(cx - ax)*v + b*s*(bx - ax) + 2.*d*(cx - ax)*by - 2.*d*cy*(bx - ax))/m
    let brsq = (x - ax)**2 + y*y + z*z
    let perp t = (x + t*a/hypot, y + t*b/hypot, z + t*c/hypot)
    let c_dist t =
        let e, f, g = perp t
        let o, p, q = e - sx, f - sy, g - sz
        (o*o + p*p + q*q |> sqrt) + sz - sqrt (t*t + brsq)
    let ans = binsearch c_dist 0 100
    printf "%.4f %.4f %.4f " <||| perp ans;
    printfn "%.4f" <| sqrt (ans*ans + brsq)

main ()
