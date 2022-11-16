open System

let toPigLatin (word: string) =
    let isVowel (c: char) =
        match c with
        | 'a' | 'e' | 'i' |'o' |'u' -> true
        |_ -> false
    
    let len = String.length(word)
    let mutable vow = -1
    let mutable i = -1
    let mutable cont = true

    while i<len-1 && cont do
        i <- i+1
        if isVowel word[i] then
            vow <- i
            cont <- false
    done
    
    if vow = -1 then
        word + "ay"
    else
        word[vow..] + string(word[0..vow-1]) + "ay"

[<EntryPoint>]
let main _ =
    
    let mutable cont = true

    while cont do
        let word = Console.ReadLine()
        if word = "#" then
            cont <- false
        else
            word |> toPigLatin |> Console.WriteLine
    done

    0
