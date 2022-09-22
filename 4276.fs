open System

let f n =
    
    let mutable x = 0L
    let c = string n |> String.length
    
    for k = 0 to c-2 do

        let w = pown 10L k
        let d = (n/w)%10L
        let a = (if d > 0 then w-1L else n%w)
        let t = (int64)(n/(10L*w))*w+a+1L-w

        x <- x+t

    done

    if n < 0 then x <- -1

    x

[<EntryPoint>]
let main _ =
    
    let mutable cont = true

    while cont do 
        
        let arr = Console.ReadLine().Split ' ' |> Array.map int64
        let m = arr.[0]
        let n = arr.[1]
        if n<0 then
            cont <- false
        else 
            let ans = f n - f (m-1L)
            printfn "%d" ans

    done
    
    0
