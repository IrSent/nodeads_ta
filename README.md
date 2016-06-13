Test assignment (Ask.fm)
===============================================

### Register:
`http://mkhimich.com/account/register/`

HOW-TO: You'll be able to operate through api after you register an account
add `-u user:password` to curl

todo:
- create question

QUESTIONS
-----------------------------------------------

| Method | Command | Description|
|:-------|:--------|-----------:|
| GET    | `curl -X GET http://mkhimich.com/api/quiz/questions`| Get all questions |
| POST   | `curl -X POST -d '{"text"="hello world"}' http://mkhimich.com/api/quiz/questions` | Create new question |


| Method | Command | Description|
|:-------|:--------|-----------:|
| GET    | `curl -X GET http://mkhimich.com/api/quiz/questions/1` | Get specific question |
| PUT    | `curl -X PUT -d '{"text"="edited"}' http://mkhimich.com/api/quiz/questions/1` | Edit specific question |
| DELETE | `curl -X DELETE http://mkhimich.com/api/quiz/questions/1` | Delete specific question |
| POST   | `curl -X POST http://mkhimich.com/api/quiz/questions/1/like/` | Like specific question |


ANSWERS
-----------------------------------------------

| Method | Command | Description|
|:-------|:--------|-----------:|
| GET    | `curl -X GET http://mkhimich.com/api/quiz/questions/1/answer/` | Get answer |
| PUT    | `curl -X PUT -d '{"text"="edited"}' http://mkhimich.com/api/quiz/questions/1/answer/` | Edit answer |
| DELETE | `curl -X DELETE http://mkhimich.com/api/quiz/questions/1/answer/` | Delete answer |
| POST   | `curl -X POST http://mkhimich.com/api/quiz/questions/1/answer/like/` | Like answer |



EXAMPLE
-----------------------------------------------
curl -X POST -H "Content-Type: application/json" -d '{"text":"xyz"}' -u someguy:ivanivan http://0.0.0.0:8081/api/quiz/questions/