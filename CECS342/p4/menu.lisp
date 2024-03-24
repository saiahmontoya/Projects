(defstruct card suit rank face-up)

(defparameter *deck* '())
(defparameter *table-pile* '())
(defparameter *fibonacci-piles* '())
(defparameter *current-sum* 0)

(defun draw-card (deck)
  (pop deck))

(defun update-sum (card sum)
  (if (numberp (card-rank card))
      (+ sum (card-rank card))
      (+ sum 10)))

(defun is-fibonacci? (num)
  (let* ((fib-list '(0 1))
         (next-fib (+ (first fib-list) (second fib-list))))
    (loop
      (if (= num next-fib) (return t))
      (if (< num next-fib) (return nil))
      (setq fib-list (cons next-fib fib-list))
      (setq next-fib (+ (first fib-list) (second fib-list))))))

(defun discard-pile (pile)
  (push (reverse pile) *fibonacci-piles*)
  (setq *table-pile* '())
  (setq *current-sum* 0))

(defun new-pile ()
  (setq *table-pile* '())
  (setq *current-sum* 0))

(defun display-game-state ()
  (format t "Sum: ~a~%" *current-sum*)
  (format t "Current Pile: ~a~%" *table-pile*))

(defun main-game-loop ()
  (loop
    (display-game-state)
    
    (format t "1) Draw a card~%")
    (format t "2) Exit~%")
    (format t "Enter your choice: ")
    
    (let ((choice (read)))
      (cond
        ((= choice 1)
         (let ((card (draw-card *deck*)))
           (push card *table-pile*)
           (setq *current-sum* (update-sum card *current-sum*))
           (if (is-fibonacci? *current-sum*)
               (discard-pile *table-pile*))))
        ((= choice 2) (return))
        (t (format t "Invalid choice.~%"))))))

(defun play-solitaire ()
  (format t "Welcome to Fibonacci Solitaire!~%")
  (loop
    (new-pile)
    (main-game-loop)
    (if (is-fibonacci? *current-sum*)
        (progn
          (format t "Winner! There are ~a Fibonacci piles.~%" (length *fibonacci-piles*))
          (return))
        (format t "Loser!~%"))))

(play-solitaire)
