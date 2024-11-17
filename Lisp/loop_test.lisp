(format t "this file is loop test~%")

(defun sum (n accumulator)
  (if (<= n 0)
      accumulator
      (sum (- n 1) (+ accumulator n))))

(format t "The sum is: ~A~%" (sum 5 0))  ; 显示结果
