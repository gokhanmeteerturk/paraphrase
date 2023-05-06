# Paraphrase

This is a naive way of paraphrasing sentences by replacing verbs(detected with spaCy) with synonyms when possible(using nltk).

## Development Setup
0. Clone this repo:

    `git clone https://github.com/gokhanmeteerturk/paraphrase.git`

1. Create a virtual environment: `python -m venv env`

2. Activate your environment ( for Windows, run .\env\Scripts\activate )

3. install requirements:

    `python -m pip install -r requirements.txt`

4. install required spacy files:

    `python -m spacy download en_core_web_sm`

5. wordnet and stopwords are already included.


## Docker
Instead of following the steps above, you can just use the docker-compose.yml to run a container in seconds:

> docker-compose up

## Usage
Send a POST request to the /process endpoint with a JSON payload containing the key "text" and the sentence you want to paraphrase:
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"My new army will destroy and create new cities.\"}" http://localhost:8000/process
```
The response will be a JSON object with the key "processed_text" containing the paraphrased sentence:

```json
{"processed_text":"My new army will demolish and make new cities."}
```