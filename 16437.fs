open System
open System.IO

let sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()))
let sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()))


type node = {
    Pop: int64
    Children: int list
}

let blank (l: int list) = {
    Pop = 0L
    Children = l
}

let relu (x: int64) = if x < 0L then 0L else x

let main () =
    let u = sr.ReadLine() |> int
    let rec mapper (z: int) (map: Map<int, node>) : Map<int, node> =
        if z = u + 1 then map else
        let t, x, n = sr.ReadLine().Split() |> (fun x -> x[0], int64 x[1], int x[2])
        let newnode =
            match Map.tryFind z map with
            | Some nd ->
                if t = "S" then {Pop = x; Children = nd.Children}
                else {Pop = -x; Children = nd.Children}
            | None ->
                if t = "S" then {Pop = x; Children = []}
                else {Pop = -x; Children = []}
        match Map.tryFind n map with
        | Some nd ->
            Map.add n {nd with Children = z :: nd.Children} map
            |> Map.add z newnode |> mapper (z + 1)
        | None ->
            Map.add n (blank [z]) map
            |> Map.add z newnode |> mapper (z + 1)
    let map: Map<int, node> = mapper 2 <| Map([(1, blank [])])
    let rec calc (z: int) : int64 =
        let nd = Map.find z map
        let s = [for e in nd.Children -> e |> calc |> relu] |> List.sum
        s + nd.Pop |> relu
    calc 1 |> sw.WriteLine

let () = main ()

sr.Close()
sw.Close()
