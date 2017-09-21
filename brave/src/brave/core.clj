(ns brave.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))


(def hello
  "new function"
  (fn [arg] 
    (println "Hello 2")))

(def plus (fn [a b] (+ a b)))

(def factorial
    (fn [n]
      (loop [c n acc 1]
        (if (zero? cnt)
          acc
          (recur  (dec cnt)  (* acc cnt))))))

