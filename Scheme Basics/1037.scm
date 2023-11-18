(let ((len (read)))

  (define (track cnt min max)
    (if (= cnt len) (* min max)
      (let ((x (read)))
        (track (+ 1 cnt) (if (< x min) x min) (if (< max x) x max))
      )
    )
  )

  (write (track 0 1000000 0))

  (newline)
)
