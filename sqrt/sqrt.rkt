#lang racket

(define (sqrt x)
  (define (is-good-enough? guess)
    (< (abs (- (* guess guess) x)) 0.001))

  (define (average a b)
    (/ (+ a b) 2))

  (define (improve guess)
    (average guess (/ x guess)))

  (define (sqrt-iter guess)
    (if (is-good-enough? guess)
        guess
        (sqrt-iter (improve guess))))

  (sqrt-iter 1.0))

;; Run example
(displayln (sqrt 1234))
