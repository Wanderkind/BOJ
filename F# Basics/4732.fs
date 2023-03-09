open System


let transpose (halfstep : int) (note : string) =
    let convert = function
    | "B#" | "C"  -> 0
    | "C#" | "Db" -> 1
    | "D"         -> 2
    | "D#" | "Eb" -> 3
    | "E"  | "Fb" -> 4
    | "E#" | "F"  -> 5
    | "F#" | "Gb" -> 6
    | "G"         -> 7
    | "G#" | "Ab" -> 8
    | "A"         -> 9
    | "A#" | "Bb" -> 10
    | "B"  | "Cb" -> 11
    | _ -> -1
    let standard = ["C"; "C#"; "D"; "D#"; "E"; "F"; "F#"; "G"; "G#"; "A"; "A#"; "B"]
    standard[(convert note + halfstep) % 12]
;;

[<EntryPoint>]
let main _ =
    
    let mutable cont = true

    while cont do
        let inp = Console.ReadLine()
        if inp = "***" then
            cont <- false
        else
            let n = Console.ReadLine() |> int
            let lst = inp.Split ' ' |> Array.map string
            for i in lst do
                printf "%s " (transpose n i)
            done
            printf "\n"
    done

    0
