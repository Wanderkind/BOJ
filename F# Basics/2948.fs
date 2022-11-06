open System

[<EntryPoint>]
let main _ =

    let line = Console.ReadLine().Split ' ' |> Array.map int
    let mutable d = line[0]
    let m = line[1]

    for i=0 to m-2 do
        d <- d+[|31;28;31;30;31;30;31;31;30;31;30;31|][i]
    done

    let s=[|"Mon";"Tues";"Wednes";"Thurs";"Fri";"Satur";"Sun"|]
    printf "%sday" s[(d+2)%7]

    0
