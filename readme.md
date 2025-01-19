## Docker Compose Gold
=====================
dev goal: take this up to localstack; an S3 static react app, some db use, some lambda use....
some ... realistic endpoint control...good point to fork per product. Then deploy stuff.

This probably ends up at scratching aws with a security credential ugly hack/test it, see it, tear it down, delete everything I can think of then fork ... then clean up/gussy up my hack as "documentation" here in all likelyhood, and go dark. That is the goal.


### Overview 
- ```docker compose up``` to run it
-- all local, all the time
-- postman.local.cfg && use cases/better than  a readme

- ```docker compose -profile test up``` to test WIP
-- all "normal" automatable tests

- ```docker compose -profile reflexive up``` CURRENT DEFAULT WIP
-- THIS docker compose system, external tests; then "normal" tests

- ```docker compose -profile deploy up``` to run local monitor and deploy to aws WIP
-- different local react app to communicate NUCLEAR LAUNCH GO? runs tests....maybe singleton thingie run from git merge into deploy branch?
== could JUST be a script, phone home github. Redploy deploy branch/ sre break glass...lol....react app calls that script.

- ```docker compose -profile monitor up``` stuff on AWS
-- idk...could be react app just showing shortcuts to aws, local server might make k8s smart/fun. Feels like 26 realistically.


- test with a pytest service.
-- maybe something fancy to connect tests to design docs...I want more ai ppt slides

- test with postman, hopefully automated with a fun manual path.

### Agents
1. Create software creation checklist. json. 3 layers. 
-



### Calendar
- 1/28/25 second to last python 3.13 starts bugfix phase q4-24 - q3-29. as good as it gets

