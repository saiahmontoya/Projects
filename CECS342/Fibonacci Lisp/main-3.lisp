; Saiah Montoya
; CECS 342-07
; Prog 2- Fibonnaci Solitaire using Lisp
; Due Nov. 9 2023
; 
; I certify that this program is my own original work. 
; I did not copy any part this program from any other sources. 
; I further cerrtify that I typed each and every line of code in this program.


(defvar *deck* ())
(defvar *hearts* (list 'AH '2H '3H '4H '5H '6H '7H '8H '9H '10H 'JH 'QH 'KH))
(defvar *spades* (list 'AS '2S '3S '4S '5S '6S '7S '8S '9S '10S 'JS 'QS 'KS))
(defvar *clubs* (list 'AC '2C '3C '4C '5C '6C '7C '8C '9C '10C 'JC 'QC 'KC))
(defvar *diamonds* (list 'AD '2D '3D '4D '5D '6D '7D '8D '9D '10D 'JD 'QD 'KD))

(defun initialize-deck ()
  (setq *deck* (create-deck))
  (setq *table-pile* '())
  (setq *current-sum* 0)
)

(defun concat-lists (seq1 seq2)
  (if (null seq1)
      seq2
      (cons (car seq1) (concat-lists (cdr seq1) seq2))))

(defun create-deck()
  (setq *deck* ())
  (setq *deck* (concat-lists *deck* *diamonds* ))
  (setq *deck* (concat-lists *deck* *hearts* ))
  (setq *deck* (concat-lists *deck* *spades* ))
  (setq *deck* (concat-lists *deck* *clubs* ))
  *deck*)

(defun shuffle-deck()
  (let ((deck-copy (copy-list *deck*)))
    (setq *deck*
          (loop repeat (length deck-copy)
                for i = (random (length deck-copy))
                collect (nth i deck-copy)))))


(defun display-deck ()
  (let ((count 0))
    (mapc (lambda (card)
            (princ card)
            (setq count (+ count 1))
            (if (= (mod count 13) 0)
                (terpri)
                (format t ", ")))
          *deck*)
    (terpri)))


(defun card-value (card)
  (defvar *One* (list 'AH 'AS 'AC 'AD))
  (defvar *Two* (list '2H '2S '2C '2D))
  (defvar *Three* (list '3H '3S '3C '3D))
  (defvar *Four* (list '4H '4S '4C '4D))
  (defvar *Five* (list '5H '5S '5C '5D))
  (defvar *Six* (list '6H '6S '6C '6D))
  (defvar *Seven* (list '7H '7S '7C '7D))
  (defvar *Eight* (list '8H '8S '8C '8D))
  (defvar *Nine* (list '9H '9S '9C '9D))
  (defvar *Ten* (list '10H '10S '10C '10D 'JH 'JS 'JC 'JD 'QH 'QS 'QC 'QD 'KH 'KS 'KC 'KD))
  (cond
    ((member card *One*) 1)
    ((member card *Two*) 2)
    ((member card *Three*) 3)
    ((member card *Four*) 4)
    ((member card *Five*) 5)
    ((member card *Six*) 6)
    ((member card *Seven*) 7)
    ((member card *Eight*) 8)
    ((member card *Nine*) 9)
    ((member card *Ten*) 10)
    (t 0))
)

(defun deal-top ()
  (if (null *deck*)
      (format t "~%The deck is empty.")
      (let ((top-card (pop *deck*)))
        top-card))
)

(defun play-solitaire ()
  (setq point 0)
  (setq cumulate-point 0)
  (setq count 0) ; For checking how many piles from the deck
  (let ((pile-count 0)) ; Declare pile-count inside a let to retain its value

    (do ((current-card nil)
         (current-point 0))
        ((null (setq current-card (deal-top))))
      (setq current-point (card-value current-card))
      (setq cumulate-point (+ cumulate-point current-point))
      (princ current-card)
      (princ " ")
      (incf pile-count) ; Increment pile-count for each card added to the pile

      (if (is-fibo cumulate-point)
          (progn
            (format t "   Fibo: ~a~%" cumulate-point)
            (setq cumulate-point 0)
            (incf count))))

    (if (is-fibo cumulate-point)
        (format t "~&Winner in ~a pile(s)! Cards in the pile: ~a" count pile-count))
    (terpri)))


(defun play-til-win ()
  (setq *games-played* 0) ; Initialize *games-played*
  (setq count 0) ; Initialize count outside the loop
  (loop
    (incf *games-played*) ; Increment games played for each loop iteration
    (format t "Loser in ~a piles -> going for win. Game ~a.~%" count *games-played*) ; Display loser message
    (play-solitaire)
    (if (is-fibo cumulate-point)
        (progn   
          (format t "Games played: ~a~%" *games-played*) ; Display games played
          (terpri)
          (return))
        (progn
          (create-deck)
          (shuffle-deck)
          (setq cumulate-point 0)
          (incf count) ; Increment count for each iteration of the outer loop
          ))))



(defun is-fibo (n)
  (let ((a 0)
        (b 1))
    (loop
      (cond
        ((= n a) (return t)) ; Found a Fibonacci number
        ((< n a) (return nil)) ; n is not a Fibonacci number
        (t (setq c (+ a b))
           (setq a b)
           (setq b c))))))

(defun display-cards-in-pile (pile)
  (when pile
    (let ((card (car pile)))
      (format t "~a, Fibo: ~a~%" card (card-value card))
      (display-cards-in-pile (cdr pile))
    ))
)

(defun fibo (n)
  (let ((a 0)
        (b 1))
    (loop
      (if (= b n)
          (return t))
      (if (> b n)
          (return nil))
      (setq b (+ a b))
      (setq a (- b a))
    )
  )
)


(defun main()
  (format t "1) New Deck~%")
  (format t "2) Display Deck~%")
  (format t "3) Shuffle Deck~%")
  (format t "4) Play Solitaire~%")
  (format t "5) Play until Win~%")
  (format t "6) Exit~%")
  (format t "Enter your choice: ")
  (case (read)
    (1 (create-deck))
    (2 (display-deck))
    (3 (shuffle-deck))
    (4 (play-solitaire))
    (5 (play-til-win))
    (6 (return nil))
  )
  (main)
)


(main)