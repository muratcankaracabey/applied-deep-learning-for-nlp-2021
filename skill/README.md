# Skill

This alexa skill uses a custom end-point rather than using the default lambda function provided in an Alexa-hosted-skill template. Therefore, it is developped locally rather than using the Alexa skill console. With the help of [local_debugger.py](local_debugger.py) file, it is possible to debug the alexa code and improve the development experience. 

When a custom endpoint is used, Alexa requires that endpoint having an https protocol. Luckily, `ngrok` is able to serve localhost with https. 

[en-US.json](skill-package/interactionModels/custom/en-US.json) file describes the interaction model such as the intents, slots and the intenhandler names for them. 

All the rest such as handling the intents are defined in [lambda_function.py](skill/lambda/lambda_function.py)
