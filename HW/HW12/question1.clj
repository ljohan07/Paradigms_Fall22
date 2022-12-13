(def number_read (map #(Integer/parseInt %) *command-line-args*))
(def number (first number_read))

(def mylist (range 1 (+ number 1)))

(def mysquares (map (fn [x] (* x x)) mylist))

(doseq [i (range 0 number)] (println (nth mysquares i)))

(def squaresum (reduce + mysquares))
(println "Sum = " squaresum)
