import requests
import html
import random
response = requests.get("https://opentdb.com/api.php", params = {"amount": 20, "category": 17, "type": "multiple"})
data = response.json()
questionList, correctAnswer, answerChoice = [], [], []
for item in list(data['results']):
    questionList.append(html.unescape(item['question']))
    correctAnswer.append(html.unescape(item['correct_answer']))
    answerList = [html.unescape(item['correct_answer'])] + html.unescape(item['incorrect_answers'])
    random.shuffle(answerList)
    answerChoice.append(answerList)