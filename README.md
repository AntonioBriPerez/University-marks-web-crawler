# University-marks-web-crawler
Web Crawler to refresh the website of my qualifications every x time and in the moment the teacher grades me a screenshot is taken and sent to a telegram bot

## Setting Up the project 🚀
Firstly you will need Google Chrome and its driver. You cand find more information here: https://chromedriver.chromium.org/downloads

Once you have download it, you will need to create a telegram bot. You can find how to do it here: https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
And you also will need to know your chat id, you can also find it in the previous link. 

Ultimately, you will start the script with the command: 
```
$python get_note_from_website.py
```

This script reads the number of the fields Aptos / No aptos so when you get graded it will increment the numbers. For example, if you have no grades the website will look like 0 Aptos / 0 No aptos. If you have 2 grades: 4/10 and 7/10 you will have: 1 Apto / 1 No apto. 
This is an example
![alt_text] (https://github.com/AntonioBriPerez/University-marks-web-crawler/blob/main/notas_TC.png)

So when one of these numbers is greater than zero, the script will take an screenshot and send it to you via telegram. 
