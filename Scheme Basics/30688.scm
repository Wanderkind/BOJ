(let ((n (read)) (k (read)))
(print (if (or (>= n (+ k k 2)) (= n (+ k 1)) (= n (+ k 2)) ) "C win\n" "A and B win\n")))
