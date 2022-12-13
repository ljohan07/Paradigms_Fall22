(ns taxation)

(defn tax [amt rate] (float (/ (* amt rate) 100)))

(println (tax 117 7))

(ns application)
(use 'taxation)
(print "7% tax on 117 is = ")
(printf "%.2f" (taxation/tax 117 7))
