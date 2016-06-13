QUESTIONS
===============================================

curl -X GET    http://mkhimich.com/api/quiz/
curl -X POST   http://mkhimich.com/api/quiz/    -d '{"text"="hello world"}'

curl -X GET    http://mkhimich.com/api/quiz/questions/1
curl -X PUT    http://mkhimich.com/api/quiz/questions/1   -d '{"text"="I've corrected this a bit"}'
curl -X DELETE http://mkhimich.com/api/quiz/questions/1
curl -X POST   http://mkhimich.com/api/quiz/questions/1/like/

ANSWERS
===============================================
curl -X GET    http://mkhimich.com/api/quiz/questions/1/answer/
curl -X PUT    http://mkhimich.com/api/quiz/questions/1/answer/  -d '{"text"="I've corrected this a bit"}'
curl -X DELETE http://mkhimich.com/api/quiz/questions/1/answer/
curl -X POST   http://mkhimich.com/api/quiz/questions/1/answer/like/


EXAMPLE
curl -X POST -H "Content-Type: application/json" -d '{"text":"xyz"}' -u someguy:ivanivan http://0.0.0.0:8081/api/quiz/questions/