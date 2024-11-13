(format t "this file is loop test~%")

(defun sum (n accumulator)
  (if (<= n 0)
      accumulator  ; 当 n <= 0 时，返回累加器的值
      (sum (- n 1) (+ accumulator n))))  ; 否则递归并累加

(sum 5 0)  ; 计算 1 到 5 的和，结果是 15
