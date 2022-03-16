# Email cleanup web service
Simple web service aimed to clean up a body of an email message from unnecessary footers and further chatter.

Build from enclosed Dockerfile. Start:
````
docker run -p 3000:3000 talon
````

To use:
````
curl -X POST http://localhost:3000/ --header "Content-Type: text/plain" --data-binary @email.txt
````
or
````
curl -X POST http://localhost:3000/ --header "Content-Type: text/html" --data-binary @email.html
````
Sample responses:

When accessed via GET:
````
{"alive":"yes","app_id":"talon"}
````

POST:
````
{"response":"Re: Learning Reminder\n\tFrom\n\tSender\n\tTo\n\tSomebody else\n\tRecipients\n\tSomebody\n\nSounds good, thank you sir!\n\n\n\nThanks for the heads up, I'll approve requests as soon as I see them.\n\n\u00a0 _____"}
````
