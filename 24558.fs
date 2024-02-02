open System


let main _ =
    let xyr = Console.ReadLine().Split ' ' |> Array.map double
    let x0, y0, r = xyr[0], xyr[1], xyr[2]
    let l = Console.ReadLine().Split ' ' |> Array.map int |> Array.toList
    let rec plist acc = function
    | [] -> List.rev acc
    | h :: t -> plist <|| (((h - x0), (t[0] - y0)) :: acc, List.tail t)
    let points_pre = List.tail l |> List.map double |> plist []
    let nat2 = points_pre[0] |> (fun (a, b) -> -(atan2 b a))
    let cs, sn = cos nat2, sin nat2
    let transform (p, q) = (p*cs - q*sn, p*sn + q*cs)
    let points = List.map transform points_pre
    let rec info dist ang = function
    | [] -> (List.rev dist, List.rev ang)
    | h :: t ->
        let a, b = h
        let d, g = sqrt (a*a + b*b), atan2 b a
        info <||| (d :: dist, g :: ang, t)
    let dists, angs = points @ [points[0]] |> info [] []
    let area a b p =
        if abs p < 0.00000001 then 0. else
        let c, s = cos p, sin p
        (a*b*(s - p*c) + (a*a + b*b)*(p - s*c)/2.)/(s*a*b)**2.
    let rec sum acc di an =
        match (di, an) with
        | (dh :: dt, ah :: at) ->
            match (dt, at) with
            | (dh' :: _, ah' :: _) -> sum (acc + area dh dh' (ah' - ah)) dt at
            | _ -> acc*r**4./2.
        | _ -> failwith "..."
    let ans = sum 0. dists angs |> abs
    printfn "%.9f" ans

main ()
