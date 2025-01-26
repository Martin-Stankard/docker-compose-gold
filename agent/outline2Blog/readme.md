# R & D, A2B generic agent.
## given A make B
- feature >a2b> tests >a2b> comments >a2b> code 
- lotta git commits. 
-- IMPORTANT INSIGHT: subdivide test+ 
-- maybe a lighter than this review analysis, minor a2b steps.?? idk here
-- example, first pass unit tests are hard coded to pass, save git
- morning comes, inspect the passing unit tests, 
-- maybe some meaningful documentation to help demonstrate
-- thumbs up/thumbs down merge feature branch? deploy?


```python ./outline2Blog.py```
- put a simple, one collumn list in outline.txt 

algorithm....I like 4 models on ollama, research no rag, no flowise...

[ 
  llama3.2:latest - 3ish,
  mistral:latest  - 7ish,
  qwen:7B         - 8ish,
  llama3.1        - 8ish 
]

TODO: abstracting out THIS outline AND blog component to....llm feeder "a2b" is a real move.
foreach writing prompt per '>'.
feature > tests > comments > code ..... just 3 writing prompts...can even be a call to write writing prompt given a and b; 
'critique' and 'rewrite' can solidify as generic prompts each leap '>' 
That happens here...overnight, wake up to unit tests; 


...subdividing just making tests, 1st pass hardcode pass. Run tests. Git commit. Like....5.0.0 might be able to efficiently code and not run all tests....
