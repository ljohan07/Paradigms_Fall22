(def tempstr (slurp "temperatures.txt"))

(def tempnum (clojure.string/split tempstr #"\n"))

(def temp (map #(Double/parseDouble %) tempnum))


(def c_temp (map (fn [x] (/ (* 5 (- x 32)) 9)) temp))
(defn avg [array] (double ( / (reduce + array) (count array))))
(println "min= " (apply min c_temp))
(println "max= " (apply max c_temp))
(println "avg= " (avg c_temp))