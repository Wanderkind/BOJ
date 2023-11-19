(let ((x(read))) (display
  (if (< x 425) "Violet"
    (if (< x 450) "Indigo"
      (if (< x 495) "Blue"
        (if (< x 570) "Green"
          (if (< x 590) "Yellow"
            (if (< x 620) "Orange"
              "Red"
)))))))) (newline)
