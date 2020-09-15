# Chatbot Project
Project of a chat bot in the overall framework of the developer education program

## To run this program:
* Create a virtual environment in the folder named ***chatbot***;
* Install the required dependencies from file named ***requirements.txt***;
* In the chatbot root folder, create a ***.env*** file to host your Google API key (see details below);
* Type ***flask run***;
* Open your browser at url ***http://localhost:5000/#***.

## To deploy this program:
* This program is currently deployed on Heroku. Therefore some files have been added to make this possible.
They are the following ones:
* nltk.txt
* .nltk_packages
* Procfile
* runtime.txt

## To be noticed:
# Question Parsing
* This program uses ***nltk*** to parse the questions.
You may be confused by some peculiarities while installing nltk.
Here is a link that could be useful, such a situation were to occur:
https://www.pitt.edu/~naraehan/python3/faq.html#Q-nltk-data-path
Be aware that nltk may require a specific installation process when deployed on the server.

* This program uses ***StanfordPOSTagger*** to characterize the words in a question. StanfordPOSTagger works on JAVA. Therefore, for a new deployment you may have to install a SDK Java on the remote server.

# Google API key:
* The API Key is not available on GitHub;
* The user should get his own key;
* Then he creates a file named ***.env*** in chatbot folder;
* Google Key should be named: ***GOOGLE_API_KEY***
* The link to this confidential key is set in **app.controller.api_folder.config.py**
* For a deployement, don't forget to add this key to the environment variables of your server.

# XSS exploit:
* XSS exploit risk is tackled with by a specific script : ***DOMPurify***, available at: 
https://github.com/cure53/DOMPurify


